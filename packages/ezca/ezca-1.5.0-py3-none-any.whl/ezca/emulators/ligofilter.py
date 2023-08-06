import os
import re
import time
import random
import threading

from pcaspy import SimpleServer, Driver

from .. import const as top_const
from ..ligofilter import SFMask, LIGOFilter
from . import const as emu_const

prefix = emu_const.TEST_FILTER_PREFIX
pvdb = dict()

def _get_filter_channel_name(filter_number):
    return 'Name'+('%02d' % filter_number)

for sw_name in top_const.FILTER_SW_NAMES:
    pvdb[sw_name] = dict(type='int', value=0)
    pvdb[sw_name+'R'] = dict(type='int', value=0)
    pvdb[sw_name+'S'] = dict(type='int', value=0)

for i in top_const.FILTER_MODULE_NUM_RANGE:
    pvdb[_get_filter_channel_name(i-1)] = dict(type='string', value='')

for writable_channel in top_const.FILTER_WRITABLE_CHANNELS:
    pvdb[writable_channel] = dict(type='float', value=0)

READBACKS = ['INMON', 'EXCMON', 'OUTMON', 'OUTPUT', 'OUT16']
for readback in READBACKS:
    pvdb[readback] = dict(type='float', value=0)
pvdb['SWSTAT'] = {
    'type': 'float', # FIXME: should be int
    'value': 0,
    }

def _log(string):
    if os.getenv('LFM_LOG', False):
        print(string)

class myDriver(Driver):
    def __init__(self):
        super(myDriver, self).__init__()
        self.lock = threading.Lock()
        self.filter_lock = [threading.Lock() for i in top_const.FILTER_MODULE_NUM_RANGE]
        self.ramp_lock = dict()
        for ramp_name in top_const.FILTER_RAMP_NAMES:
            self.ramp_lock[ramp_name] = threading.Lock()

        # calculated signal values
        self._IN1 = 0
        self._EXC = 0
        self._IN2 = 0
        self._OUT = 0

    def read(self, reason):
        _log("R: %s" % (reason))
        value = self.getParam(reason)
        _log('%s = %s' % (reason, value))
        return value

    def __affects_readonly_bit(self, reason, put_value):
        if put_value & top_const.WHOLE_READONLY_BIT_MASK[reason]:
            return True
        return False

    def __engage_filter(self, filter_number):
        if self.getParam(_get_filter_channel_name(filter_number-1)):
            filter_engaged_mask = top_const.READONLY_MASKS['FM'+str(filter_number)+'_ENGAGED']
            with self.filter_lock[filter_number-1]:
                time.sleep(random.uniform(*emu_const.TEST_FILTER_RANDOM_ENGAGE_BOUNDS))
                with self.lock:
                    current_value = self.getParam(filter_engaged_mask.SW+'R')
                    self.setParam(filter_engaged_mask.SW+'R',
                            current_value | filter_engaged_mask.bit_mask)
                    self.updatePVs()

    def __disengage_filter(self, filter_number):
        if self.getParam(_get_filter_channel_name(filter_number-1)):
            filter_engaged_mask = top_const.READONLY_MASKS['FM'+str(filter_number)+'_ENGAGED']
            with self.filter_lock[filter_number-1]:
                time.sleep(random.uniform(*emu_const.TEST_FILTER_RANDOM_DISENGAGE_BOUNDS))
                with self.lock:
                    current_value = self.getParam(filter_engaged_mask.SW+'R')
                    self.setParam(filter_engaged_mask.SW+'R',
                            current_value & ~filter_engaged_mask.bit_mask)
                    self.updatePVs()

    def __change_filter_status(self, filter_number):
        if self.getParam(_get_filter_channel_name(filter_number-1)):
            filter_switch_mask = top_const.WRITE_MASKS['FM'+str(filter_number)]
            current_value = self.getParam(filter_switch_mask.SW+'R')
            if current_value & filter_switch_mask.bit_mask:
                self.__engage_filter(filter_number)
            else:
                self.__disengage_filter(filter_number)

    def __get_affected_filter_modules(self, reason, put_value):
        affected_filter_modules = []
        for i in top_const.FILTER_MODULE_NUM_RANGE:
            switch_mask = top_const.WRITE_MASKS['FM'+str(i)]
            if reason == switch_mask.SW and put_value & switch_mask.bit_mask:
                affected_filter_modules.append(i)
        return affected_filter_modules

    def __ramp_filter(self, ramp_name):
        switch_mask = top_const.READONLY_MASKS[ramp_name+'_RAMP']
        with self.ramp_lock[ramp_name]:
            with self.lock:
                current_value = self.getParam(switch_mask.SW+'R')
                self.setParam(switch_mask.SW+'R', current_value | switch_mask.bit_mask)
                self.updatePVs()
            time.sleep(self.getParam('TRAMP'))
            with self.lock:
                current_value = self.getParam(switch_mask.SW+'R')
                self.setParam(switch_mask.SW+'R', current_value & ~switch_mask.bit_mask)
                self.updatePVs()

    def write(self, reason, put_value):
        _log("                  W: %s %s" % (reason, put_value))

        if reason in top_const.FILTER_SW_NAMES:
            if self.__affects_readonly_bit(reason, put_value):
                return False

            affected_filter_modules = self.__get_affected_filter_modules(reason, put_value)
            with self.lock:
                read_value = self.getParam(reason+'R')
                self.setParam(reason+'R', read_value ^ put_value)
                self.setParam(reason+'S', read_value ^ put_value)
                self.updatePVs()

            if affected_filter_modules:
                for filter_number in affected_filter_modules:
                    t = threading.Thread(target=self.__change_filter_status, args=(filter_number,))
                    t.daemon = True
                    t.start()
            return True

        if reason in [name+'S' for name in top_const.FILTER_SW_NAMES]:
            reason = reason[:-1]

            with self.lock:
                self.setParam(reason+'S', put_value)
                read_value = self.getParam(reason+'R')
                read_only_mask = top_const.WHOLE_READONLY_BIT_MASK[reason]
                self.setParam(reason+'R', (~read_only_mask & put_value) | (read_only_mask & read_value))
                self.updatePVs()

            affected_filter_modules = self.__get_affected_filter_modules(reason, read_value ^ put_value)

            if affected_filter_modules:
                for filter_number in affected_filter_modules:
                    t = threading.Thread(target=self.__change_filter_status, args=(filter_number,))
                    t.daemon = True
                    t.start()
            return True

        if re.match(r'^Name(\d*)$', reason):
            self.setParam(reason, put_value)
            self.updatePVs()
            return True

        if reason in top_const.FILTER_WRITABLE_CHANNELS:
            with self.lock:
                different = self.getParam(reason) != put_value
                self.setParam(reason, put_value)
                self.updatePVs()

            if reason in top_const.FILTER_RAMP_NAMES and different:
                t = threading.Thread(target=self.__ramp_filter, args=(reason,))
                t.daemon = True
                t.start()

            if reason == 'RSET':
                self.setParam(reason, put_value)
                self.setParam(reason, 0)
                self.updatePVs()

            return True

        # allow "actuation" of input channels
        if reason in ['INMON', 'EXCMON']:
            self.setParam(reason, put_value)
            self.updatePVs()

        return False

    def setParam(self, reason, value):
        _log('%s -> %s' % (reason, value))
        super(myDriver, self).setParam(reason, value)

    def __is_engaged(self, button):
        mask = top_const.WRITE_MASKS[button]
        sw_val = self.getParam(mask.SW+'R')
        return bool(mask.bit_mask & int(sw_val))

    def updatePVs(self):
        SW1 = self.getParam('SW1R')
        SW2 = self.getParam('SW2R')
        # FIXME: this should set the SWSTAT independently, and NOT use
        # LIGOFilter, since that's what we're supposed to be testing.
        self.setParam('SWSTAT', SFMask.from_sw(SW1, SW2).SWSTAT)
        self._IN1 = self.getParam('INMON')
        self._EXC = self.getParam('EXCMON')
        self._IN2 = self._EXC
        if self.__is_engaged('INPUT'):
            self._IN2 += self._IN1
        self._OUT = self._IN2
        if self.__is_engaged('OFFSET'):
            self._OUT += self.getParam('OFFSET')
        self._OUT *= self.getParam('GAIN')
        if self.__is_engaged('LIMIT') and self._OUT > self.getParam('LIMIT'):
            self._OUT = self.getParam('LIMIT')
        self.setParam('OUTMON', self._OUT)
        if self.__is_engaged('OUTPUT'):
            self.setParam('OUTPUT', self._OUT)
            self.setParam('OUT16', self._OUT)
        else:
            self.setParam('OUTPUT', 0)
            self.setParam('OUT16', 0)
        super(myDriver, self).updatePVs()

def start_emulator(prefix=prefix):
    server = SimpleServer()
    server.createPV(prefix, pvdb)
    driver = myDriver()
    _log(prefix)
    _log(list(pvdb.keys()))
    while True:
        server.process(emu_const.TEST_FILTER_PROCESS_TIME)

##################################################

if __name__ == '__main__':
    import sys

    medm = False

    argc = 1
    while True:
        if argc >= len(sys.argv):
            break
        elif '-m' in sys.argv[argc]:
            medm = True
        else:
            break
        argc += 1

    try:
        prefix = sys.argv[argc]
    except IndexError:
        prefix = prefix

    if medm:
        import multiprocessing
        screen = os.path.join(os.path.dirname(__file__), 'TEST_FILTER.adl')
        cmd = ('medm', 'medm', '-x',
               '-macro', 'PREFIX=%s' % prefix, '-attach',
               '-displayFont', '-misc-fixed-medium-r-normal--8-60-100-100-c-50-iso8859-1',
               screen)
        medm_proc = multiprocessing.Process(target=os.execlp, args=cmd)
        medm_proc.daemon = True
        medm_proc.start()

    try:
        start_emulator(prefix)
    except KeyboardInterrupt:
        medm_proc.terminate()
        medm_proc.join()
        raise SystemExit()
