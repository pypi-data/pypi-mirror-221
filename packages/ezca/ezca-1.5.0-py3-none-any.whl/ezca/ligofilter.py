import re
import time
from collections import defaultdict

from . import const
from . import cached
from .errors import LIGOFilterError, EzcaConnectError
from .ezcaPV import EzcaPV
from .ramp import Ramp

_no_value = object()  # unique "None" object

############################################################

def _translate_int_button_name(int_button_name):
    if int_button_name in const.FILTER_MODULE_NUM_RANGE:
        return 'FM'+str(int_button_name)
    raise ValueError

def _translate_button_name(button_name_input):
    try:
        button_name_input = int(button_name_input)
        if isinstance(button_name_input, int):
            return _translate_int_button_name(button_name_input)
    except ValueError:  # button_name_input is not a number
        pass
    if button_name_input in const.WRITE_MASKS:
        return button_name_input
    raise LIGOFilterError("unable to translate button name '%r'." % button_name_input)

############################################################

class SFMask(object):
    """A bit word for each switch channel associated with a filter.

    A SFMask is built by translating button names into
    const.SwitchMask objects.

    """
    def __init__(self, buttons=_no_value):
        # initialize mask to all zero bits
        for sw_name in const.FILTER_SW_NAMES:
            setattr(self, sw_name, 0)

        # update mask based on *buttons
        if buttons is not _no_value:
            self += buttons

    def __iadd__(self, buttons):
        for button in buttons:
            switch_mask = const.ALL_MASKS[button]
            current_switch_value = getattr(self, switch_mask.SW)
            setattr(self, switch_mask.SW, current_switch_value | switch_mask.bit_mask)
        return self

    def __isub__(self, buttons):
        for button in buttons:
            if button not in self.buttons:
                continue
            switch_mask = const.ALL_MASKS[button]
            current_switch_value = getattr(self, switch_mask.SW)
            setattr(self, switch_mask.SW, current_switch_value ^ switch_mask.bit_mask)
        return self

    def __or__(self, other):
        mask = SFMask()
        for sw_name in const.FILTER_SW_NAMES:
            setattr(mask, sw_name, getattr(self, sw_name) | getattr(other, sw_name))
        return mask

    def __xor__(self, other):
        mask = SFMask()
        for sw_name in const.FILTER_SW_NAMES:
            setattr(mask, sw_name, getattr(self, sw_name) ^ getattr(other, sw_name))
        return mask

    def __eq__(self, other):
        for sw_name in const.FILTER_SW_NAMES:
            if getattr(self, sw_name) != getattr(other, sw_name):
                return False
        return True

    def __ne__(self, other):
        return not self == other

    @property
    def buttons(self):
        button_names = []
        used_switch_masks = defaultdict(bool)
        for button_name, switch_mask in const.ALL_MASKS_STRICT.items():
            if used_switch_masks[switch_mask]:
                continue
            used_switch_masks[switch_mask] = True
            if getattr(self, switch_mask.SW) & switch_mask.bit_mask:
                button_names.append(button_name)
        return [b for b in const.BUTTONS_ORDERED if b in button_names]

    def __str__(self):
        return self.abrev
        s = ','.join(self.buttons)
        return s

    @property
    def abrev(self):
        return ','.join([const.BUTTON_ABREV[b] for b in self.buttons])

    @property
    def SWSTAT(self):
        swstat = 0
        for button in self.buttons:
            if button in const.SWSTAT_BITS:
                swstat += const.SWSTAT_BITS[button]
        return swstat

    def __repr__(self):
        s = 'SFMask('+str(self.buttons)+')'
        return s

    def __iter__(self):
        return iter(self.buttons)

    def __contains__(self, button):
        return button in self.buttons

    @classmethod
    def from_sw(cls, SW1, SW2):
        """Return SFMask representing specified switch values.

        """
        mask = cls()
        setattr(mask, 'SW1', int(SW1))
        setattr(mask, 'SW2', int(SW2))
        return mask

    @classmethod
    def from_swstat(cls, SWSTAT):
        """Return SFMask representing specified SWSTAT value.

        """
        mask = cls()
        for button, val in const.SWSTAT_BITS.items():
            if SWSTAT & val:
                mask += [button]
        return mask

    @classmethod
    def for_buttons_engaged(cls, *buttons, **kwargs):
        """Return SFMask representing expected button engaged state.

        Returned SFMask object represents the expected engaged state for
        the specified buttons.

        """
        buttons = [_translate_button_name(b) for b in buttons]
        mask = cls()
        for button in set(buttons):
            mask += [button]
        if kwargs.get('engaged', True):
            for button in set(buttons) & set(const.FILTER_NAMES):
                mask += [button+'_ENGAGED']
        return mask

# FIXME: need to support the old Mask name for backwards compatibility
# with some system that were already referencing it (SEI).  should
# deprecate after transition.
Mask = SFMask

############################################################

class LIGOFilter(metaclass=cached.Cached):
    """LIGO EPICS interface to a standard filter module.

    'filter_name' is the full name of a filter module after any
    previous specified subsystem prefix (see Ezca prefixes).

    'ezca' is an instantiated ezca object which will be used for
    nearly all of the channel access reads and writes that occur in
    this class.

    The LIGOFilter class emulates an interface to the LIGO standard
    filter module that is familiar to anyone who interfaces with the
    filter MEDM screens on most subsystems. It contains methods such
    as 'turn_on', 'press', and 'ramp_gain' which all work as one might
    expect.

    """
    def __init__(self, filter_name, ezca):
        if filter_name:
            self.filter_name = filter_name
            self.prefix = filter_name+'_'
        else:
            self.filter_name = ''
            self.prefix = ''

        self.ezca = ezca

        # Instantiate EzcaPV's for the SW[12][\bSR] channels where \b stands for word boundary.
        for sw_name in const.FILTER_SW_NAMES:
            for end in ['', 'S', 'R']:
                setattr(self, '_'+sw_name+end, EzcaPV(self.prefix+sw_name+end, ezca))

        # Instantiate EzcaPV's for channels associated with filter.
        for s in ['TRAMP','GAIN','OFFSET','LIMIT','INMON','EXCMON',\
                  'OUTMON','OUTPUT','OUT16','RSET','SWSTAT'] \
            + ['Name%02d' % (i-1) for i in const.FILTER_MODULE_NUM_RANGE]:
            setattr(self, s, EzcaPV(self.prefix+s, ezca))

        # Instantiate Ramp objects.
        for ramp_type in ('gain_ramp', 'offset_ramp'):
            # Note that the _RAMP_TYPE keyword argument is used in is_ramping() and start_ramp()
            # for "early binding". Without this "early binding", _RAMP_TYPE would be the last
            # value of _RAMP_TYPE after this loop is finished in every instance of the is_ramping()
            # and start_ramp() functions.
            _RAMP_TYPE = ramp_type.upper()
            def is_ramping(value, _RAMP_TYPE=_RAMP_TYPE):
                return bool(int(value) & const.READONLY_MASKS[_RAMP_TYPE].bit_mask)

            def start_ramp(value, ramp_time, _RAMP_TYPE=_RAMP_TYPE):
                self.TRAMP.put(ramp_time)

                ramp_ezca_pv = getattr(self, _RAMP_TYPE.split('_')[0])
                if ramp_ezca_pv.get() != value:  # do not ramp if already at desired value
                    ramp_ezca_pv.put(value)

            setattr(self, '_'+ramp_type,
                    Ramp(self.prefix+const.READONLY_MASKS[_RAMP_TYPE].SW+'R',
                         is_ramping,
                         start_ramp,
                         self.ezca))

    ##########

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.filter_name, self.ezca)

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.filter_names)

    def get_current_switch_dict(self):
        """Return current switch values as a dict.

        Raises a ValueError if there is a NaN in one of the values.
        This is usually because the switch values could not be read from epics (see __init__())
        """
        return {sw_name: int(getattr(self, '_'+sw_name+'R').get()) for sw_name in const.FILTER_SW_NAMES}

    def get_current_switch_mask(self, rw_only=False):
        """Return a mask representing the current state of the filter."""
        current = SFMask.from_sw(**self.get_current_switch_dict())
        if rw_only:
            current -= list(const.READONLY_MASKS.keys())
        return current
    get_current_state_mask = get_current_switch_mask

    def get_current_swstat_mask(self):
        """Return a mask representing the current SWSTAT state."""
        return SFMask.from_swstat(int(getattr(self, 'SWSTAT').get()))

    ##########

    def turn_off(self, *buttons, **kwargs):
        """Set every button in <buttons> to off.

        In the case of filter buttons, this has the effect of setting
        the request of the filter to off.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.turn_off('INPUT', 'OUTPUT')
        >>> ligo_filter.turn_off('FM1', 'FM3')
        >>> ligo_filter.turn_off(*['FM2', 'FM5'])

        If 'engage_wait=True', the function does not return until all
        buttons have fully disengaged (see is_engaged()).

        """
        buttons = [_translate_button_name(b) for b in buttons]
        self.__switch('off', buttons)
        if kwargs.get('engage_wait', False):
            while any([self.is_engaged(button) for button in buttons]):
                continue
            return True

    switch_off = turn_off

    def turn_on(self, *buttons, **kwargs):
        """Set every button in <buttons> to on.

        In the case of filter buttons, this has the effect of setting
        the request of the filter to on.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.turn_on('INPUT', 'OUTPUT')
        >>> ligo_filter.turn_on('FM1', 'FM3')
        >>> ligo_filter.turn_on(*['FM2', 'FM5'])

        If 'engage_wait=True', the function does not return until all
        buttons have fully engaged (see is_engaged()).

        """
        buttons = [_translate_button_name(b) for b in buttons]
        self.__switch('on', buttons)
        if kwargs.get('engage_wait', False):
            while not all([self.is_engaged(button) for button in buttons]):
                continue
            return True

    switch_on = turn_on

    def all_off(self, **kwargs):
        """Set every button on the filter to off.

        In the case of filter buttons, this has the effect of setting
        every filter request to off.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.all_off()

        See only_on() for options.

        """
        self.only_on(**kwargs)

    def only_on(self, *buttons, **kwargs):
        """Set only the specified buttons to on and all other to off.

        This method ensures that the only the buttons listed in
        <buttons> are on.  If no buttons are specified,

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.turn_on('FM1')
        >>> ligo_filter.only_on('INPUT', 'OUTPUT', 'FM2')
        >>> print ligo_filter.is_engaged('FM1')
        False

        If 'wait=True', functions waits until ezca puts succeed.

        If 'engage_wait=True', the function does not return until all
        buttons have fully engaged (see is_engaged()).

        """
        wait = kwargs.get('wait', True)
        buttons = [_translate_button_name(b) for b in buttons]
        mask = SFMask(buttons)
        self.__put_mask_set(mask, wait=wait)
        if kwargs.get('engage_wait', False):
            expected_mask = SFMask.for_buttons_engaged(*buttons)
            while self.get_current_switch_mask() != expected_mask:
                continue
            return True
        # FIXME: using private method Ezca class.
        if SFMask() == mask:
            self.ezca._logswitch(self.ezca.prefix+self.filter_name, 'ALL OFF')
        else:
            self.ezca._logswitch(self.ezca.prefix+self.filter_name, 'ONLY ON: '+', '.join(buttons))

    def press(self, *buttons, **kwargs):
        """Press specified buttons.

        NOTE: use of this method is not recommended, since the
        resultant state of the module is undefined.

        """
        wait = kwargs.get('wait', True)
        buttons = [_translate_button_name(b) for b in buttons]
        mask = SFMask(buttons)
        self.__put_mask(mask, wait=wait)

    def is_input_on(self):
        """Return True if input is on."""
        return self.is_engaged('INPUT')

    def is_offset_on(self):
        """Return True if offset is on."""
        return self.is_engaged('OFFSET')

    def is_output_on(self):
        """Return True if output is on."""
        return self.is_engaged('OUTPUT')

    def is_loaded(self, bank):
        """Are filter module banks loaded with filters.

        Returns True if the specified filter banks are loaded with
        filter coefficients.

        """
        button_name = _translate_button_name(bank)
        if button_name not in const.FILTER_NAMES:
            raise LIGOFilterError("has_filter_loaded() only accepts filter bank names")
        filter_number = int(re.match(const.FILTER_NAME_REGEX, button_name).group(1))
        return bool(getattr(self, 'Name%02d' % (filter_number - 1)).get())

    def is_engaged(self, button_name):
        """Check whether <button_name> is on.

        This method raises a LIGOFilterError if <button_name> does not
        belong to the keys in const.WRITE_MASKS.

        For filter banks (FM?) the _ENGAGED bit is used to check the
        fully engaged state of the bank.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.is_engaged('FM1')

        """
        try:
            button_name = _translate_button_name(button_name)
        except LIGOFilterError:
            raise
        if button_name not in const.WRITE_MASKS:
            raise LIGOFilterError("is_engaged() only accepts the following buttons: %s" % const.WRITE_MASKS)
        if button_name in const.FILTER_NAMES:
            mask = const.READONLY_MASKS[button_name+'_ENGAGED']
        else:
            mask = const.WRITE_MASKS[button_name]
        return self.__read_switch_mask(mask)

    is_on = is_engaged

    def is_off(self, button_name):
        """Check whether <button_name> is off.

        See is_engaged for more info.

        """
        return not self.is_engaged(button_name)

    def is_requested(self, button_name):
        """Check whether the request status of <button_name> is on.

        This method raises a LIGOFilterError is <button_name> does not
        match const.IS_FM_REGEX.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.turn_on('FM2')
        >>> print ligo_filter.is_requested('FM2')
        True
        >>> ligo_filter.turn_on(1)
        >>> print ligo_filter.is_requested(1)
        True

        """
        try:
            button_name = _translate_button_name(button_name)
        except LIGOFilterError:
            raise
        if button_name not in const.FILTER_NAMES:
            raise LIGOFilterError("is_requested() only accepts filter names (e.g. 'FM1').")
        return self.__read_switch_mask(const.WRITE_MASKS[button_name])

    def __read_switch_mask(self, switch_mask):
        # development assertion that we are actually using a const.SwitchMask instance
        assert(isinstance(switch_mask, const.SwitchMask))
        return bool(switch_mask.bit_mask & self.get_current_switch_dict()[switch_mask.SW])

    def switch(self, *args, **kwargs):
        """Switch buttons (ala old-style ezcaswitch).

        This method changes the settings on the filter by specifying
        list of button names followed by the action to take for each
        of those buttons. The arguments must be of the form

            (<button_name>+, ..., <action>)*

        so that each action is preceded by a non-empty list of button
        names, and the sequence of arguments ends with an action. This
        method raises a LIGOFilterError if this syntax is violated or
        the same button names appears twice.

        The buttons names are defined in const.WRITE_MASKS. The
        actions are ON, OFF, and PRESS. ON and OFF have the same
        effect as the turn_on() and turn_off() methods. PRESS emulates
        pressing the button on an MEDM screen, or switching the button
        from on to off or off to on.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.switch('FM1', 'FM2', 'ON', 'FM3', 'OFF', 'INPUT', 'OUTPUT', 'ON')
        >>> ligo_filter.switch('FM4', 'PRESS', 'FM5', 'FM6', 'OFF')

        If no arguments are provided, the list of currently enabled
        buttons is returned.

        """
        # return current button list if no arguments provided
        if not args:
            buttons = self.get_current_switch_mask().buttons
            return [button for button in const.BUTTONS_ORDERED if button in buttons]

        wait = kwargs.get('wait', True)
        switch_actions = LIGOFilter.__get_switch_actions(args)
        mask = SFMask(switch_actions['PRESS'])
        mask |= self.__get_mask('on', switch_actions['ON'])
        mask |= self.__get_mask('off', switch_actions['OFF'])
        self.__put_mask(mask, wait=wait)

        for action, buttons in switch_actions.items():
            if buttons:
                # FIXME Using private method Ezca class.
                self.ezca._logswitch(self.ezca.prefix+self.filter_name, action+': '+', '.join(buttons))

    @staticmethod
    def __get_switch_actions(args):
        switch_actions = defaultdict(list)
        button_names = []
        seen_button_names = defaultdict(bool)
        for arg in args:
            arg = arg.upper()

            # If the argument is an actions, extend the list of button names for which
            # the action will be applied.
            if arg in const.ACTIONS:
                action_name = arg
                if not button_names:
                    raise LIGOFilterError("no buttons given for action '%s'." % action_name)
                switch_actions[action_name].extend(button_names)
                button_names = []
                continue

            # If the argument is a button name, append it to the list of button names.
            # Here we raise an exception if we have seen the button before.
            if arg in const.WRITE_MASKS:
                button_name = arg
                if seen_button_names[button_name]:
                    raise LIGOFilterError("button name '%s' appeared twice in arguments." % button_name)
                seen_button_names[button_name] = True
                button_names.append(button_name)
                continue

            # FMALL is a macro for FM[1-9]. This addresses guardian bug 631.
            if arg == 'FMALL':
                for button_name in const.FILTER_NAMES:
                    if seen_button_names[button_name]:
                        raise LIGOFilterError("'FMALL' and '%s' both appeared in arguments." % button_name)
                    seen_button_names[button_name] = True
                    button_names.append(button_name)
                continue

            raise LIGOFilterError("'%s' is not a valid button name or action." % arg)

        if button_names:
            raise LIGOFilterError("switch arguments must end with an action.")

        return switch_actions

    def is_offset_ramping(self):
        """Return whether the filter module's offset is currently ramping.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.is_offset_ramping()

        """
        return self._offset_ramp.is_ramping()

    def is_gain_ramping(self):
        """Return whether the filter module's gain is currently ramping.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.is_gain_ramping()

        """
        return self._gain_ramp.is_ramping()

    def ramp_gain(self, value, ramp_time, wait=True):
        """Ramp gain to <value> over <ramp_time>.

        Starts a ramp on the filter module's gain from the current
        value to <value> that lasts for <ramp_time> seconds. If <wait>
        is false, then this method will start the ramp and immediately
        return.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.ramp_gain(0, ramp_time=3, wait=True)
        >>> ligo_filter.ramp_gain(1, ramp_time=3, wait=False)
        >>> print ligo_filter.is_gain_ramping()
        True

        """
        self._gain_ramp.start_ramp(value=value, ramp_time=ramp_time, wait=wait)

    def ramp_offset(self, value, ramp_time, wait=True):
        """Ramp offset to <value> over <ramp_time>.

        Starts a ramp on the filter module's offset from the current
        value to <value> that lasts for <ramp_time> seconds. If <wait>
        is false, then this method will start the ramp and immediately
        return.

        >>> ligo_filter = LIGOFilter('TEST', ezca)
        >>> ligo_filter.ramp_offset(0, ramp_time=3, wait=True)
        >>> ligo_filter.ramp_offset(1, ramp_time=3, wait=False)
        >>> print ligo_filter.is_offset_ramping()
        True

        """
        self._offset_ramp.start_ramp(value=value, ramp_time=ramp_time, wait=wait)

    def __get_mask(self, on_or_off, buttons):
        """Private method that returns the masked value indicating which bits
        should be flipped so that all of the <buttons> are on or off.

        """
        mask = SFMask(buttons)
        for sw_name, current_value in self.get_current_switch_dict().items():
            if on_or_off == 'on':
                current_value = ~current_value
            elif on_or_off == 'off':
                pass
            else:
                # development Exception
                raise Exception('wrong on_or_off specified in call to __switch')
            setattr(mask, sw_name, current_value & getattr(mask, sw_name))
        return mask

    def __switch(self, on_or_off, buttons):
        """Private method that ensures that requests all of the <buttons> to
        be on or off.

        """
        mask = self.__get_mask(on_or_off, buttons)
        self.__put_mask(mask, wait=True)
        self.ezca._logswitch(self.ezca.prefix+self.filter_name,
                             on_or_off.upper() + ': ' + ', '.join(buttons))

    def __put_mask(self, mask, wait=True):
        """Private method that applies <mask> to the filter module
        buttons. It iteratively applies the mask to each of the SW
        channels listed in const.FILTER_SW_NAMES.

        """
        if not self.ezca.ca_enable_write:
            return
        current_mask = self.get_current_swstat_mask()
        for sw_name in const.FILTER_SW_NAMES:
            read_ezca_pv = getattr(self, '_'+sw_name+'R')
            write_ezca_pv = getattr(self, '_'+sw_name)
            write_value = getattr(mask, sw_name)

            for readonly_channel_name, readonly_switch_mask in const.READONLY_MASKS.items():
                if sw_name == readonly_switch_mask.SW and write_value & readonly_switch_mask.bit_mask:
                    raise LIGOFilterError(
                        const.READONLY_CHANNEL_ERROR_MESSAGE.format(
                            channel_name=write_ezca_pv.channel,
                            write_value=write_value,
                            readonly_channel_name=readonly_channel_name))

            expected_masked_after_write_value \
                = write_value & (int(read_ezca_pv.get()) ^ write_value)

            # FIXME: could this be updated to not busy wait? We could
            # possibly use callback functions and a lock.
            write_ezca_pv.put(write_value, wait=True, monitor=False)
            if wait:
                start_time = time.time()
                while True: # have to busy wait because there is no other way to
                            # check for a correct readValue
                    time.sleep(const.SWITCH_READ_TIME_STEP)
                    # FIXME: what exactly are we checking here and why?
                    if expected_masked_after_write_value\
                            == write_value & int(read_ezca_pv.get()):
                        break
                    if time.time() - start_time > self.ezca.timeout:
                        raise EzcaConnectError(
                            const.SWITCH_EZCA_TIMEOUT_ERROR_MESSAGE.format(
                                channel_name=read_ezca_pv.channel,
                                timeout=self.ezca.timeout))

        # record expected mask in SWSTAT setpoint
        expected_swstat_mask = current_mask ^ mask
        self.ezca._setpoints[self.prefix+'SWSTAT'] = (self.ezca.prefix+self.prefix+'SWSTAT',
                                                      expected_swstat_mask)

    def __put_mask_set(self, mask, wait=True):
        """Private method that sets the filter module buttons to <mask>. It
        uses the SW.S channels to iteratively apply the masks.

        """
        if not self.ezca.ca_enable_write:
            return
        for sw_name in const.FILTER_SW_NAMES:
            read_ezca_pv = getattr(self, '_'+sw_name+'R')
            set_ezca_pv = getattr(self, '_'+sw_name+'S')
            set_value = getattr(mask, sw_name)

            for readonly_channel_name, readonly_switch_mask in const.READONLY_MASKS.items():
                if sw_name == readonly_switch_mask.SW and set_value & readonly_switch_mask.bit_mask:
                    raise LIGOFilterError(
                        const.READONLY_CHANNEL_ERROR_MESSAGE.format(
                            channel_name=set_ezca_pv.channel,
                            write_value=set_value,
                            readonly_channel_name=readonly_channel_name))

            # FIXME: could this be updated to not busy wait? We could
            # possibly use callback functions and a lock.
            set_ezca_pv.put(set_value, wait=True, monitor=False)
            if wait:
                start_time = time.time()
                while True: # have to busy wait because there is no other way to
                            # check for a correct readValue
                    time.sleep(const.SWITCH_READ_TIME_STEP)
                    # FIXME: what exactly are we checking here and why?
                    if not (set_value ^ (~const.WHOLE_READONLY_BIT_MASK[sw_name] & int(read_ezca_pv.get()))):
                        break
                    if time.time() - start_time > self.ezca.timeout:
                        raise EzcaConnectError(
                            const.SWITCH_EZCA_TIMEOUT_ERROR_MESSAGE.format(
                                channel_name=self.prefix+sw_name+'R',
                                timeout=self.ezca.timeout))

        # record requested mask in SWSTAT setpoint
        self.ezca._setpoints[self.prefix+'SWSTAT'] = (self.ezca.prefix+self.prefix+'SWSTAT',
                                                      mask)

############################################################

# FIXME add ramp_type and up_or_down argument wrapper checker
class LIGOFilterManager(metaclass=cached.Cached):
    """LIGO EPICS interface to a set of standard filter modules.

    'filter_names' is a list of full names of filter modules. Each of
    these will appear after the subsystem prefix.

    'ezca' is an instantiated ezca object which will be used for
    nearly all of the channel access reads and writes that occur in
    this class.

    The LIGOFilterManager class allows LIGOFilter modules to be
    collected into a single object so that changes can be made and
    ramps can be requested on multiple modules with a single method
    call.

    """
    def __init__(self, filter_names, ezca):
        self.ezca = ezca
        self.filter_names = filter_names

        # instantiate and save filters in a dictionary
        self.filter_dict = dict()
        for filter_name in self.filter_names:
            self.filter_dict[filter_name] = LIGOFilter(filter_name, ezca)

    def __repr__(self):
        return '%s(filter_names=%r, ezca=%r)' % (self.__class__.__name__, self.filter_names, self.ezca)

    def __str__(self):
        return '<%s %s>' % (self.__class__.__name__, self.filter_names)

    def all_do(self, func, *args, **kwargs):
        """Run <func> on each contained LIGOFilter.

        For each LIGOFilter, the LIGOFilter object will be passed as
        the first argument to the function, and *args and **kwargs as
        the remaining arguments.

        >>> filter_manager = LIGOFilterManager(['TEST_1', 'TEST_2', 'TEST_3'], ezca)
        >>> def damp_setup(ligo_filter):
        >>>     ligo_filter.only_on('INPUT','OUTPUT','FM1','DECIMATE')
        >>> filter_manager.all_do(damp_setup)

        """
        if isinstance(func, str):
            func_name = func
            try:
                ligo_filter_func = getattr(LIGOFilter, func_name)
            except AttributeError:
                raise LIGOFilterError("LIGOFilter does not have method '%r'." % func_name)

            def func(ligo_filter, *func_args, **func_kwargs):
                ligo_filter_func(ligo_filter, *func_args, **func_kwargs)

        for f in self.filter_dict.values():
            func(f, *args, **kwargs)

    def __ramp_all(self, value, wait, ramp_type, ramp_time):
        ramp_func = getattr(LIGOFilter, 'ramp_'+ramp_type)

        self.all_do(ramp_func, value=value, ramp_time=ramp_time, wait=False)

        if wait:
            time.sleep(ramp_time)
            for f in self.filter_dict.values():
                while getattr(f, 'is_'+ramp_type+'_ramping')():
                    time.sleep(const.RAMP_READ_TIME_STEP)

    def ramp_gains(self, gain_value, ramp_time, wait=True):
        """Ramp the gain on each contained LIGOFilter.

        >>> filter_manager = LIGOFilterManager(['TEST_1', 'TEST_2', 'TEST_3'], ezca)
        >>> filter_manager.ramp_gains(gain_value=1, ramp_time=3, wait=True)

        """
        self.__ramp_all(value=gain_value, wait=wait, ramp_time=ramp_time,
                        ramp_type='gain')

    def ramp_offsets(self, offset_value, ramp_time, wait=True):
        """Ramp the offset on each contained LIGOFilter.

        >>> filter_manager = LIGOFilterManager(['TEST_1', 'TEST_2', 'TEST_3'], ezca)
        >>> filter_manager.ramp_offsets(offset_value=1, ramp_time=3, wait=True)

        """
        self.__ramp_all(value=offset_value, wait=wait, ramp_time=ramp_time,
                        ramp_type='offset')

    def __any_ramping(self, ramp_type):
        """Private method that returns whether the <ramp_type> of a
        LIGOFilter in the LIGOFilterManager object is currently
        ramping.

        """
        for f in self.filter_dict.values():
            if getattr(f, 'is_'+ramp_type+'_ramping')():
                return True
        return False

    def any_gain_ramping(self):
        """Return whether the gain of any filter is currently ramping."""
        return self.__any_ramping('gain')

    def any_offset_ramping(self):
        """Return whether the offset any filter is currently ramping."""
        return self.__any_ramping('offset')
