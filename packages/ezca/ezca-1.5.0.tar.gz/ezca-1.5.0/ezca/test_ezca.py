import unittest
import os
import time
import multiprocessing
from collections import defaultdict

from .ezca import Ezca, EzcaError
from .ligofilter import LIGOFilter, SFMask, LIGOFilterError, LIGOFilterManager
from . import const as top_const

from .emulators import const as emu_const
from .emulators.ligofilter import start_emulator

##################################################

os.environ['EPICS_CAS_INTF_ADDR_LIST'] = "localhost"
os.environ['EPICS_CAS_SERVER_PORT'] = "58800"
os.environ['EPICS_CA_ADDR_LIST'] = "localhost:58800"

##################################################

def check_sw_write_ezca(write_channel_name, value, ezca):
    read_channel_name = write_channel_name+'R'
    expected_after_write_value = ezca.read(read_channel_name) ^ value
    ezca.write(write_channel_name, value, wait=True)
    time.sleep(2*top_const.TEST_FILTER_PROCESS_TIME)
    return ezca.read(read_channel_name) == expected_after_write_value

def set_bank(ezca, bank, name):
    """Load filter with name into bank"""
    ezca.write(emu_const.TEST_FILTER_NAME+'_Name'+('%02d' % (bank-1)),
               name)

def load_banks(ezca, *banks):
    """Load filters into banks"""
    for bank in banks:
        set_bank(ezca, bank, 'FAKE')

def unload_banks(ezca, *banks):
    """Unload filters from banks"""
    for bank in banks:
        set_bank(ezca, bank, '')

##################################################

emulator_proc = None

def setUpModule():
    # start the ligofilter emulator
    global emulator_proc
    emulator_proc = multiprocessing.Process(target=start_emulator)
    emulator_proc.daemon = True
    emulator_proc.start()

def tearDownModule():
    global emulator_proc
    emulator_proc.terminate()
    emulator_proc.join()


class TestEzcaPrefix(unittest.TestCase):
    def test_prefixifo(self):
        self.assertEqual(Ezca(prefix='T1', ifo=None).prefix,
                         'T1:')

    def test_noprefix(self):
        ifo = ''
        if os.getenv('IFO'):
            ifo = os.getenv('IFO')+':'
        self.assertEqual(Ezca().prefix,
                         ifo)

    def test_prefixifoc(self):
        self.assertEqual(Ezca(prefix='T1:', ifo=None).prefix,
                         'T1:')

    def test_prefixifocsys(self):
        self.assertEqual(Ezca(prefix='T1:SYS', ifo=None).prefix,
                         'T1:SYS-')

    def test_prefixifocsyssub(self):
        self.assertEqual(Ezca(prefix='T1:SYS-SUB', ifo=None).prefix,
                         'T1:SYS-SUB_')

    def test_prefixifocsyssubu(self):
        self.assertEqual(Ezca(prefix='T1:SYS-SUB_', ifo=None).prefix,
                         'T1:SYS-SUB_')

    def test_prefix_ifo(self):
        self.assertEqual(Ezca(prefix='T1:SYS-SUB_', ifo='T2').prefix,
                         'T2:SYS-SUB_')

    def test_ifo(self):
        self.assertEqual(Ezca(ifo='T2').prefix,
                         'T2:')

    def test_ifo_prefixsys(self):
        self.assertEqual(Ezca(ifo='T2', prefix='SYS').prefix,
                         'T2:SYS-')

    def test_ifo_prefixcsys(self):
        self.assertEqual(Ezca(ifo='T2', prefix=':SYS').prefix,
                         'T2:SYS-')

    def test_ifo_prefixsyssub(self):
        self.assertEqual(Ezca(ifo='T2', prefix='SYS-SUB').prefix,
                         'T2:SYS-SUB_')

class TestEzca(unittest.TestCase):
    def setUp(self):
        self.ezca = Ezca(ifo=emu_const.TEST_IFO_NAME, prefix=emu_const.TEST_SUBSYS_NAME)
        load_banks(self.ezca, *top_const.FILTER_MODULE_NUM_RANGE)
    
    def test_switch_press(self):
        for button, switch_mask in top_const.WRITE_MASKS.items():
            whole_write_mask = top_const.WHOLE_WRITE_BIT_MASK[switch_mask.SW]
            read_channel_name = emu_const.TEST_FILTER_NAME+'_'+switch_mask.SW+'R'
            expected_after_write_value =\
                    whole_write_mask & (self.ezca.read(read_channel_name) ^ switch_mask.bit_mask)
            self.ezca.switch(emu_const.TEST_FILTER_NAME, button, 'PRESS')
            self.assertEqual(expected_after_write_value,
                    whole_write_mask & self.ezca.read(read_channel_name))

            self.ezca.switch(emu_const.TEST_FILTER_NAME, button, 'PRESS')
            self.assertEqual(expected_after_write_value ^ switch_mask.bit_mask,
                    whole_write_mask & self.ezca.read(read_channel_name))

    def test_switch_fmall(self):
        fmall_bit_mask = defaultdict(int)
        read_sw_channel_name = dict()
        for sw_name in top_const.FILTER_SW_NAMES:
            read_sw_channel_name[sw_name] = emu_const.TEST_FILTER_NAME+'_'+sw_name+'R'
            for fm_name in top_const.FILTER_NAMES:
                if top_const.WRITE_MASKS[fm_name].SW == sw_name:
                    fmall_bit_mask[sw_name] |= top_const.WRITE_MASKS[fm_name].bit_mask

        # FMALL ON
        self.ezca.switch(emu_const.TEST_FILTER_NAME, 'FMALL', 'ON')
        for sw_name in top_const.FILTER_SW_NAMES:
            before_change_value = self.ezca.read(read_sw_channel_name[sw_name]) & top_const.WHOLE_WRITE_BIT_MASK[sw_name]
            self.assertEqual(fmall_bit_mask[sw_name] | before_change_value,
                    self.ezca.read(read_sw_channel_name[sw_name]) & top_const.WHOLE_WRITE_BIT_MASK[sw_name])

        # FMALL OFF
        self.ezca.switch(emu_const.TEST_FILTER_NAME, 'FMALL', 'OFF')
        for sw_name in top_const.FILTER_SW_NAMES:
            before_change_value = self.ezca.read(read_sw_channel_name[sw_name]) & top_const.WHOLE_WRITE_BIT_MASK[sw_name]
            self.assertEqual(~fmall_bit_mask[sw_name] & before_change_value,
                    self.ezca.read(read_sw_channel_name[sw_name]) & top_const.WHOLE_WRITE_BIT_MASK[sw_name])

    def test_switch_on_off(self):
        for button, switch_mask in top_const.WRITE_MASKS.items():
            read_channel_name = emu_const.TEST_FILTER_NAME+'_'+switch_mask.SW+'R'
            whole_write_mask = top_const.WHOLE_WRITE_BIT_MASK[switch_mask.SW]

            before_change_value = self.ezca.read(read_channel_name) & whole_write_mask
            self.ezca.switch(emu_const.TEST_FILTER_NAME, button, 'ON')
            self.assertEqual(switch_mask.bit_mask | before_change_value,
                    self.ezca.read(read_channel_name) & whole_write_mask)

            before_change_value = self.ezca.read(read_channel_name) & whole_write_mask
            self.ezca.switch(emu_const.TEST_FILTER_NAME, button, 'OFF')
            self.assertEqual(~switch_mask.bit_mask & before_change_value,
                    self.ezca.read(read_channel_name) & whole_write_mask)

    def test_switch_random(self):
        import random

        for seed in range(20):
            # First construct a random switch argument by shuffling the list of buttons
            # and choosing a random action after popping each button from the list.
            random.seed(seed)

            switch_args = [emu_const.TEST_FILTER_NAME]
            random_buttons = list(top_const.WRITE_MASKS_BASIC.keys())
            random.shuffle(random_buttons)

            command = defaultdict(list)
            while random_buttons:
                action = random.choice(top_const.ACTIONS)
                button = random_buttons.pop()
                command[action].append(button)

                # If the next command has the same action as the previous, randomly
                # decide whether to tack the button onto the previous command or
                # create a new one
                # (e.g. ['FM7', 'INPUT', 'ON'] vs. ['FM7', 'ON', 'INPUT', 'ON'])
                if switch_args[-1] == action:
                    if random.choice([1,2]) == 1:
                        switch_args.insert(-1, button)
                        continue
                switch_args += [button, action]

            # Quick sanity check that switch_args was actually constructed.
            self.assertGreater(len(switch_args), 1)

            read_channel_name = dict()
            before_change_value = dict()
            expected_value = dict()
            for sw_name in top_const.FILTER_SW_NAMES:
                read_channel_name[sw_name] = emu_const.TEST_FILTER_NAME+'_'+sw_name+'R'
                before_change_value[sw_name] = self.ezca.read(read_channel_name[sw_name]) & top_const.WHOLE_WRITE_BIT_MASK[sw_name]

                expected_value[sw_name] = 0
                for action in top_const.ACTIONS:
                    if action == 'ON':
                        for button in command[action]:
                            if top_const.WRITE_MASKS[button].SW == sw_name:
                                expected_value[sw_name] |= top_const.WRITE_MASKS[button].bit_mask
                        continue
                    if action == 'OFF':
                        # There is nothing to do here since expected_value[sw_name] is
                        # initialized as zero.
                        continue
                    if action == 'PRESS':
                        bits_to_change = 0
                        for button in command[action]:
                            if top_const.WRITE_MASKS[button].SW == sw_name:
                                bits_to_change |= top_const.WRITE_MASKS[button].bit_mask
                        expected_value[sw_name] |= bits_to_change & (bits_to_change ^ before_change_value[sw_name])
                        continue
                    self.fail("Unrecognized action: %r." % action)

            self.ezca.switch(*tuple(switch_args))

            for sw_name in top_const.FILTER_SW_NAMES:
                self.assertEqual(expected_value[sw_name],
                        self.ezca.read(read_channel_name[sw_name]) & top_const.WHOLE_WRITE_BIT_MASK[sw_name])

    def test_caching_ezca(self):
        a = Ezca(ifo=emu_const.TEST_IFO_NAME, prefix=emu_const.TEST_SUBSYS_NAME)
        self.assertIs(a, self.ezca)

    def test_caching_ligofilter(self):
        a = self.ezca.get_LIGOFilter(emu_const.TEST_FILTER_NAME)
        b = self.ezca.get_LIGOFilter(emu_const.TEST_FILTER_NAME)
        self.assertIs(a, b)

    def test_ramping_no_wait(self):
        channel_to_be_ramped= emu_const.TEST_FILTER_NAME+'_GAIN'
        self.ezca.ramp_gain(emu_const.TEST_FILTER_NAME,
                self.ezca.read(channel_to_be_ramped)+1, emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=False)
        time.sleep(emu_const.TEST_FILTER_RAMP_TEST_TIME/2.)  # FIXME if we don't wait long enough, the ramp may not have started...
        self.assertTrue(self.ezca.is_gain_ramping(emu_const.TEST_FILTER_NAME))
        time.sleep(emu_const.TEST_FILTER_RAMP_TEST_TIME+1)
        self.assertFalse(self.ezca.is_gain_ramping(emu_const.TEST_FILTER_NAME))

        channel_to_be_ramped= emu_const.TEST_FILTER_NAME+'_OFFSET'
        self.ezca.ramp_offset(emu_const.TEST_FILTER_NAME,
                self.ezca.read(channel_to_be_ramped)+1, emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=False)
        time.sleep(emu_const.TEST_FILTER_RAMP_TEST_TIME/2.)  # FIXME if we don't wait long enough, the ramp may not have started...
        self.assertTrue(self.ezca.is_offset_ramping(emu_const.TEST_FILTER_NAME))
        time.sleep(emu_const.TEST_FILTER_RAMP_TEST_TIME+1)
        self.assertFalse(self.ezca.is_offset_ramping(emu_const.TEST_FILTER_NAME))


    def test_ramping_wait(self):
        channel_to_be_ramped = emu_const.TEST_FILTER_NAME+'_GAIN'
        
        start_time = time.time()
        self.ezca.ramp_gain(emu_const.TEST_FILTER_NAME,
                self.ezca.read(channel_to_be_ramped)+1, emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.assertGreater(time.time(), start_time+emu_const.TEST_FILTER_RAMP_TEST_TIME)

        channel_to_be_ramped = emu_const.TEST_FILTER_NAME+'_OFFSET'
        start_time = time.time()
        self.ezca.ramp_offset(emu_const.TEST_FILTER_NAME,
                self.ezca.read(channel_to_be_ramped)+1, emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.assertGreater(time.time(), start_time+emu_const.TEST_FILTER_RAMP_TEST_TIME)


class TestLIGOFilter(unittest.TestCase):
    def setUp(self):
        self.ezca = Ezca(ifo=emu_const.TEST_IFO_NAME, prefix=emu_const.TEST_SUBSYS_NAME)
        self.ligo_filter = LIGOFilter(emu_const.TEST_FILTER_NAME, self.ezca)

    def test_build_mask(self):
        for button, switch_mask in top_const.WRITE_MASKS.items():
            built_mask = SFMask([button])
            self.assertEqual(getattr(built_mask, switch_mask.SW), switch_mask.bit_mask)

    def test_mask_equality(self):
        mask_1 = SFMask(['FM1'])
        mask_2 = SFMask(['FM1'])
        self.assertEqual(mask_1, mask_2)

    def test_mask_methods(self):
        buttons = ['FM1', 'OUTPUT']
        mask = SFMask(buttons)
        self.assertEqual(sorted(mask.buttons), sorted(buttons))
        self.assertTrue('FM1' in mask)
        self.assertFalse('FM2' in mask)
        mask += ['FM2']
        self.assertTrue('FM2' in mask)

    def check_is_engaged(self, button, should_be_on):
        return check_is_engaged_list([button], should_be_on)

    def check_is_engaged_list(self, button_list, should_be_on):
        for button in button_list:
            direct_bool = bool(top_const.WRITE_MASKS[button].bit_mask\
                    & self.ezca.read(emu_const.TEST_FILTER_NAME+'_'+top_const.WRITE_MASKS[button].SW+'R'))
            if button in top_const.FILTER_NAMES:
                ligo_filter_bool = self.ligo_filter.is_requested(button)
            else:
                ligo_filter_bool = self.ligo_filter.is_engaged(button)
            if not (direct_bool == ligo_filter_bool and direct_bool == should_be_on):
                return False
        return True

    def test_turn_on_and_off_single_buttons(self):
        for button in top_const.WRITE_MASKS.keys():
            self.test_turn_on_and_off_multiple_buttons(lists=[[button]])

    def test_is_engaged_syntax(self):
        try:
            for button in top_const.WRITE_MASKS:
                self.ligo_filter.is_engaged(button)
            for button in top_const.FILTER_MODULE_NUM_RANGE:
                self.ligo_filter.is_engaged(button)
            for button in top_const.FILTER_MODULE_NUM_RANGE:
                self.ligo_filter.is_engaged(str(button))
        except LIGOFilterError:
            self.fail("LIGOFilter.is_engaged() raised exception on %r" % button)

        with self.assertRaises(LIGOFilterError):
            self.ligo_filter.is_engaged(top_const.FILTER_MODULE_NUM_RANGE[-1]+1)
        with self.assertRaises(LIGOFilterError):
            self.ligo_filter.is_engaged('FM'+str(top_const.FILTER_MODULE_NUM_RANGE[-1]+1))
        with self.assertRaises(LIGOFilterError):
            self.ligo_filter.is_engaged('blah')

    def test_is_requested_syntax(self):
        for button in top_const.WRITE_MASKS:
            if button in top_const.FILTER_NAMES:
                try:
                    self.ligo_filter.is_requested(button)
                except LIGOFilterError:
                    self.fail("LIGOFilter.is_requested() raised exception on %r" % button)
                continue
            with self.assertRaises(LIGOFilterError):
                self.ligo_filter.is_requested(button)

        for i in top_const.FILTER_MODULE_NUM_RANGE:
            try:
                self.ligo_filter.is_requested(i)
                self.ligo_filter.is_requested(str(i))
            except LIGOFilterError:
                self.fail("LIGOFilter.is_requested() raised exception on %r" % i)

    def test_turn_on_and_off_multiple_buttons(self, lists=None):
        if lists is None:
            lists = emu_const.TEST_MULTIPLE_BUTTON_LISTS

        for button_list in lists:
            # change input button status
            self.ligo_filter.turn_on(*button_list)

            # read current input button status again
            self.assertTrue(self.check_is_engaged_list(button_list, True))

            # change input button status
            self.ligo_filter.turn_off(*button_list)

            # read current input button status again
            self.assertTrue(self.check_is_engaged_list(button_list, False))

    def test_put_mask_writable(self):
        for switch_mask in top_const.WRITE_MASKS.values():
            mask = SFMask()
            setattr(mask, switch_mask.SW, switch_mask.bit_mask)
            read_channel_name = emu_const.TEST_FILTER_NAME+'_'+switch_mask.SW+'R'
            expected_masked_after_write_value =\
                    switch_mask.bit_mask & (self.ezca.read(read_channel_name) ^ switch_mask.bit_mask)
            self.ligo_filter._LIGOFilter__put_mask(mask, wait=True)
            self.assertEqual(expected_masked_after_write_value,
                    switch_mask.bit_mask & self.ezca.read(read_channel_name))

    def test_put_mask_set(self):
        for switch_mask in top_const.WRITE_MASKS.values():
            mask = SFMask()
            setattr(mask, switch_mask.SW, switch_mask.bit_mask)
            read_channel_name = emu_const.TEST_FILTER_NAME+'_'+switch_mask.SW+'R'
            self.ligo_filter._LIGOFilter__put_mask_set(mask, wait=True)
            read_only_mask = 0
            for sm in [sm for sm in iter(top_const.READONLY_MASKS.values()) if sm.SW == switch_mask.SW]:
                read_only_mask |= sm.bit_mask
            self.assertEqual(switch_mask.bit_mask,
                    ~read_only_mask & self.ezca.read(read_channel_name))

    def test_put_mask_readonly(self):
        for readonly_switch_mask in top_const.READONLY_MASKS.values():
            mask = SFMask()
            setattr(mask, readonly_switch_mask.SW, readonly_switch_mask.bit_mask)
            with self.assertRaises(LIGOFilterError):
                self.ligo_filter._LIGOFilter__put_mask(mask, wait=True)

    #@unittest.skip('')  # decorator to skip filter engagement test
    def test_filter_engagement(self):
        load_banks(self.ezca, *top_const.FILTER_MODULE_NUM_RANGE)

        self.ligo_filter.all_off(engage_wait=True)

        # engage each filter
        for filter_number, filter_name in enumerate(top_const.FILTER_NAMES):
            self.ligo_filter.turn_on(filter_name, engage_wait=True)
            # FIXME: why is this wait not sufficient to sure bank engaged?
            # time.sleep(emu_const.TEST_FILTER_RANDOM_ENGAGE_BOUNDS[1]+1)
            self.assertTrue(self.ligo_filter.is_engaged(filter_name))
            self.assertTrue(self.ligo_filter.is_engaged(filter_number+1))
            self.assertTrue(self.ligo_filter.is_engaged(str(filter_number+1)))

        # disengage each filter
        for filter_number, filter_name in enumerate(top_const.FILTER_NAMES):
            self.ligo_filter.turn_off(filter_name, engage_wait=True)
            # FIXME: why is this wait not sufficient to sure bank engaged?
            # time.sleep(emu_const.TEST_FILTER_RANDOM_DISENGAGE_BOUNDS[1]+1)
            self.assertFalse(self.ligo_filter.is_engaged(filter_name))
            self.assertFalse(self.ligo_filter.is_engaged(filter_number+1))
            self.assertFalse(self.ligo_filter.is_engaged(str(filter_number+1)))

    def test_is_loaded(self):
        unload_banks(self.ezca, *top_const.FILTER_MODULE_NUM_RANGE)
        for num in top_const.FILTER_MODULE_NUM_RANGE:
            print(num)
            self.assertFalse(self.ligo_filter.is_loaded('FM%d' % num))

        load_banks(self.ezca, *top_const.FILTER_MODULE_NUM_RANGE)
        for num in top_const.FILTER_MODULE_NUM_RANGE:
            self.assertTrue(self.ligo_filter.is_loaded('FM%d' % num))

    # FIXME only testing gain ramping
    def test_is_ramping_wait(self):
        # check that ramping is done upon return
        self.ligo_filter.ramp_gain(1, ramp_time=emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.ligo_filter.ramp_gain(2, ramp_time=emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.assertFalse(self.ligo_filter.is_gain_ramping())

    def test_same_ramp_wait(self):
        self.ligo_filter.ramp_gain(1, ramp_time=emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.ligo_filter.ramp_gain(1, ramp_time=emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.assertFalse(self.ligo_filter.is_gain_ramping())

    def test_is_ramping_no_wait(self):
        # check that filter ramps during times that it should be
        self.ligo_filter.ramp_gain(1, ramp_time=emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=True)
        self.ligo_filter.ramp_gain(2, ramp_time=emu_const.TEST_FILTER_RAMP_TEST_TIME, wait=False)
        self.assertTrue(self.ligo_filter.is_gain_ramping())
        time.sleep(emu_const.TEST_FILTER_RAMP_TEST_TIME/3.)
        self.assertTrue(self.ligo_filter.is_gain_ramping())
        time.sleep(emu_const.TEST_FILTER_RAMP_TEST_TIME*2./3.+self.ligo_filter.ezca.timeout)
        self.assertFalse(self.ligo_filter.is_gain_ramping())

    def test_mask_equality(self):
        self.assertTrue(SFMask() == SFMask())
        self.assertTrue(SFMask(['FM1']) == SFMask(['FM1']))
        self.assertTrue(SFMask(['INPUT', 'FM1', 'DECIMATE']) == SFMask(['INPUT', 'DECIMATE', 'FM1']))

    def test_mask_inequality(self):
        self.assertFalse(SFMask(['FM1']) == SFMask())
        self.assertFalse(SFMask(['FM1']) == SFMask(['FM2']))
        self.assertFalse(SFMask(['INPUT', 'FM3', 'DECIMATE']) == SFMask(['INPUT', 'DECIMATE', 'FM1']))

    def test_get_current_state_mask(self):
        self.ligo_filter.only_on('FM1','FM2','DECIMATE', wait=False)
        self.assertTrue(SFMask(['FM1','FM2','DECIMATE']), self.ligo_filter.get_current_state_mask())
        time.sleep(1)
        self.assertTrue(SFMask(['FM1','FM2','FM1_ENGAGED','FM2_ENGAGED','DECIMATE']), self.ligo_filter.get_current_state_mask())


class TestLIGOFilterManager(unittest.TestCase):
    def setUp(self):
        self.ezca = Ezca(ifo=emu_const.TEST_IFO_NAME, prefix=emu_const.TEST_SUBSYS_NAME)
        self.ligo_filter_manager = LIGOFilterManager([emu_const.TEST_FILTER_NAME], self.ezca)

    def test_all_do_custom_func(self):
        def f(lf):
            lf.turn_on('INPUT')
        self.ligo_filter_manager.all_do(f)

        for lf_name, lf in self.ligo_filter_manager.filter_dict.items():
            self.assertTrue(lf.is_engaged('INPUT'))

    def test_all_do_ligofilter_method_basic(self):
        self.ligo_filter_manager.all_do('switch', 'INPUT', 'ON')

        for lf_name, lf in self.ligo_filter_manager.filter_dict.items():
            self.assertTrue(lf.is_engaged('INPUT'))

    def test_all_do_ligofilter_method_harder(self):
        self.ligo_filter_manager.all_do('switch', 'INPUT', 'OFFSET', 'FM2', 'ON', 'FM1', 'OFF')
        print(self.ligo_filter_manager.filter_dict)
        for lf_name, lf in self.ligo_filter_manager.filter_dict.items():
            self.assertTrue(lf.is_engaged('INPUT'))
            self.assertTrue(lf.is_engaged('OFFSET'))
            self.assertTrue(lf.is_requested('FM2'))
            self.assertTrue(lf.is_off('FM1'))

        self.ligo_filter_manager.all_do('turn_off', 'INPUT')
        for lf_name, lf in self.ligo_filter_manager.filter_dict.items():
            self.assertTrue(lf.is_off('INPUT'))

        self.ligo_filter_manager.all_do('turn_on', 'INPUT')
        for lf_name, lf in self.ligo_filter_manager.filter_dict.items():
            self.assertTrue(lf.is_engaged('INPUT'))

        class FAIL(Exception): pass
        self.ligo_filter_manager.all_do('all_off')
        for lf_name, lf in self.ligo_filter_manager.filter_dict.items():
            for button in top_const.WRITE_MASKS:
                try:
                    if button in top_const.FILTER_NAMES:
                        if lf.is_requested(button):
                            raise FAIL
                    else:
                        if lf.is_engaged(button):
                            raise FAIL
                except FAIL:
                    self.fail("all_do('all_off') failed to turn off %r" % button)

    def test_all_do_bad_method(self):
        with self.assertRaises(LIGOFilterError):
            self.ligo_filter_manager.all_do('abda', 'hello')

    def test_ramping_usage(self):
        self.ligo_filter_manager.ramp_gains(0, 1, wait=True)
        self.ligo_filter_manager.ramp_gains(1, 1, wait=True)
        self.ligo_filter_manager.ramp_offsets(0, 1, wait=True)
        self.ligo_filter_manager.ramp_offsets(1, 1, wait=True)

##################################################

if __name__ == '__main__':
    unittest.main(verbosity=5, failfast=False, buffer=True)
