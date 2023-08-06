import time
from epics.pv import PV
from . import const

_no_value = object()

class Ramp(object):
    def __init__(self, ramp_monitor_channel_name, is_ramping_func, start_ramp_func, ezca):
        self.ezca = ezca
        self.ramp_monitor_channel_name = ramp_monitor_channel_name

        # This function takes a single argument that is the current value of
        # <ramp_monitor_channel_name>.
        self.__is_ramping = is_ramping_func

        # This function will take the arguments passed to self.start_ramp.
        self.__start_ramp = start_ramp_func

        self.__last_status = False
        self.__last_call_time = _no_value
        self.__last_start_time = _no_value

        self.rampmon_pv = PV(self.ezca.prefix + self.ramp_monitor_channel_name)
        self.rampmon_pv.add_callback(self.__note_ramp_change)

    def __repr__(self):
        return 'Ramp(%r, %r, %r, %r)'\
                % (self.ramp_monitor_channel_name, self.__is_ramping, self.__start_ramp, self.ezca)

    def __current_ramp_status(self):
        return self.__is_ramping(self.rampmon_pv.get())

    def __note_ramp_change(self, pvname, value, **kwargs):
        status = self.__is_ramping(value)
        if status and not self.__last_status:
            self.__last_start_time = time.time()
        self.__last_status = status

    def start_ramp(self, *args, **kwargs):
        if 'wait' in kwargs:
            wait = kwargs.pop('wait')
        else:
            wait = False

        self.__start_ramp(*args, **kwargs)
        self.__last_call_time = time.time()

        if wait:
            while self.is_ramping():
                time.sleep(const.RAMP_READ_TIME_STEP)

    def is_ramping(self):
        # This while loop is finite because of condition (**)
        while True:
            last_ramp_call_time = self.__last_call_time
            last_ramp_start_time = self.__last_start_time

            # (*)
            # If we don't know about a ramp call, then return the current
            # status of the ramp.
            if last_ramp_call_time is _no_value:
                return self.__current_ramp_status()

            # (**)
            # If last ramp call occurred too long ago to affect filter, then
            # return the current status of the ramp.
            if time.time() - last_ramp_call_time > self.ezca.timeout:
                return self.__current_ramp_status()

            # This final condition is crucial. At this point, we know that
            # last_ramp_call_time occurred "not too long ago," and so it must
            # be the case that we are waiting for a recent last_ramp_start_time
            # to appear. Thus, we have the condition that last_ramp_start_time
            # was assigned a value and it is after last_ramp_call_time.
            if last_ramp_start_time is not _no_value\
                    and last_ramp_call_time <= last_ramp_start_time:
                    return self.__current_ramp_status()

            time.sleep(const.RAMP_READ_TIME_STEP)
