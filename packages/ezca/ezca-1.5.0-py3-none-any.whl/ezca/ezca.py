import os
import re
import sys
import logging

import ezca.errors

if sys.version_info.major > 2:
    import builtins
else:
    import __builtin__ as builtins

import epics

from . import const
from . import cached
from .errors import EzcaError, EzcaConnectError
from .ligofilter import SFMask, LIGOFilter, LIGOFilterManager

_no_value = object()  # unique "None" object

SPM_MOMENTARY_SUFFIXES = [
    '_RSET',
    '_LOAD_MATRIX',
]

############################################################

def ligo_channel_prefix(ifo, subsys=None):
    """Make LIGO channel prefix given an ifo and (potentially compound) subsystem.

    'ifo' argument is required.  If 'subsys' is not specified, the
    returned prefix is ifo-rooted (e.g. 'H1:').

    """
    # FIXME: somehow check for "valid" subsys (no bad characters, etc.)
    separators = '-_'
    delim = None
    prefix = ifo.upper().rstrip(':') + ':'
    if subsys:
        if subsys[-1] in separators:
            delim = subsys[-1]
        subsys = subsys.upper().strip(separators)
        ss = subsys.split('-')
        if len(ss) == 1 or ss[1] == '':
            subsys = ss[0]
            delim = delim or '-'
        else:
            subsys = ss[0] + '-' + ss[1]
            delim = delim or '_'
        prefix += subsys + delim
    return prefix


def parse_ifo_prefix(ifo, prefix):
    """Munge user-supplied ifo and prefix into full channel access prefix.

    'prefix' is a channel prefix, consisting of either just a
    subsystem ('SUS-ETMX') or ifo and subsystem ('H1:SUS-ETMX').
    'ifo' is an interferometer specifier.  The ifo and subsystem will
    be parsed from the 'prefix' and 'ifo' arguments to make a full
    LIGO channel access prefix.  The ifo for the resultant channel
    access prefix will be selected with the following priority:

      * specified in 'prefix' argument (e.g prefix='H1:SYS')
      * 'ifo' argument (e.g. ifo='H1')

    The chosen ifo will be combined with the specified subsystem part
    to form the full channel access prefix.

    """
    # parse prefix with ifo:subsys form
    if prefix and len(prefix.split(':')) > 1:
        _ifo = prefix.split(':')[0]
        _subsys = prefix.split(':')[1]
    else:
        _ifo = None
        _subsys = prefix
    # use ifo from keyword argument
    if ifo:
        _ifo = ifo
    # if ifo still not specified assume prefix is ifo
    if not _ifo and _subsys:
        _ifo = _subsys
        _subsys = None
    _prefix = ''
    if _ifo:
        _prefix = ligo_channel_prefix(_ifo, _subsys)
    return _ifo, _prefix

############################################################

class EzcaLogger(logging.LoggerAdapter):
    def __init__(self, logger):
        super(EzcaLogger, self).__init__(logger, {'prefix': 'ezca:'})

    def process(self, msg, kwargs):
        msg = '%s %s' % (self.extra['prefix'], msg)
        return (msg, kwargs)


# FIXME: should this inherit directly from epics.Device, but there
# seems to be an unfortunate interaction with the logging module that
# causes long delays and log messages to not be written, but no errors
# thrown either.
#class Ezca(epics.Device):
class Ezca(metaclass=cached.Cached):
    """LIGO EPICS channel access interface.

    Ezca is a LIGO-specific wrapper around the EPICS channel access
    library.  It is designed to more easily handle the specific form
    of LIGO EPICS channel names, and the parameters they expose.  It
    provides standard channel read() and write() methods, as well as
    LIGO-specific methods, such as for interacting with standard
    filter modules (SFM) (see the LIGOFilter class).

    A channel access prefix can be specified for all channel access
    calls using the 'prefix' and 'ifo' arguments.  See
    ezca.parse_ifo_prefix for information on how the ultimate channel
    access prefix is chosen from 'prefix' and 'ifo'.  If 'ifo' is not
    specified, the value of the 'IFO' environment variable will be
    used.  If no prefix at all is desired, even if the IFO environment
    is set, specify ifo=None (prefix=None by default) e.g.:

    >>> ezca.Ezca(ifo=None)
    Ezca(prefix='')

    'logger' is a logging object that will be used to log channel
    writes.

    """

    def export(self):
        """export this Ezca instance into the __builtin__ namespace."""
        builtins.ezca = self

    def __init__(self, prefix=None,
                 ifo=os.getenv('IFO'),
                 timeout=float(os.getenv('EZCA_TIMEOUT', const.CA_TIMEOUT)),
                 logger=True):
        #super(Ezca, self).__init__(prefix, delim='')

        self._ifo, self._prefix = parse_ifo_prefix(ifo, prefix)

        self._dev = epics.Device(self._prefix, delim='')
        if not logger:
            self._log = logging.getLogger()
            self._log.addHandler(logging.NullHandler())
        elif logger is True:
            self._log = logging.getLogger('ezca')
            self._log.setLevel('INFO')
            self._log.addHandler(logging.StreamHandler())
        else:
            self._log = EzcaLogger(logger)

        self._timeout = timeout
        self._setpoints = {}

        self.ca_enable_read = True
        self.ca_enable_write = True
        self.ca_fail_no_connect = True
        ca_enable = os.getenv('EZCA_CA', 'TRUE').upper()
        if ca_enable in ['ENABLE', 'TRUE', 'ON']:
            pass
        elif ca_enable == 'READONLY':
            self._log.warning("channel access READONLY.")
            self.ca_enable_write = False
        elif ca_enable in ['DISABLE', 'FALSE', 'OFF']:
            self._log.warning("channel access DISABLED.")
            self.ca_enable_read = False
            self.ca_enable_write = False
        elif ca_enable == 'NOFAIL':
            self._log.warning("channel access NOFAIL.")
            self.ca_fail_no_connect = False
        else:
            raise EzcaError("Unknown EZCA_CA value: %s" % (ca_enable))

    def __repr__(self):
        return '%s(prefix=%r)'\
                % (self.__class__.__name__, self._prefix)

    def __str__(self):
        return '<%s %r, %d channels>'\
                % (self.__class__.__name__, self._prefix, len(self.pvs))

    ##########

    @property
    def timeout(self):
        """Channel access connection timeout (in seconds)"""
        return self._timeout

    @property
    def ifo(self):
        """IFO string"""
        return self._ifo

    @property
    def prefix(self):
        """Full channel prefix string"""
        return self._dev._prefix

    @property
    def pvs(self):
        """Dictionary of device PVs and their status"""
        return self._dev._pvs

    ##########

    # FIXME: remove this
    def _a2s(self, value):
        if type(value) in [int, float]:
            return '%.3f' % value
        else:
            return value

    def _logget(self, pv, log=False):
        message = "%s == %s" % (pv.pvname, pv.get())
        if log:
            self._log.warning(message)
        else:
            self._log.log(5, message)

    def _logput(self, pv, value=None):
        if value is None:
            value = pv.get()
        message = "%s => %s" % (pv.pvname, value)
        self._log.warning(message)

    def _logswitch(self, filt, switches):
        message = "%s => %s" % (filt, switches)
        self._log.warning(message)

    ##########

    def connect(self, channel):
        """Open a connection to the specified channel.

        If a successful connection is made, the channel is registered
        with the EPICS device and a persistent connection is
        maintained.  If not, the channel is not registered and an
        EzcaError is raised.

        If a connection to the channel already exists, the connection
        will be checked for connection status, and an EzcaError will
        be thrown if the connection is dead.

        """
        if channel in self._dev._pvs:
            pv = self._dev._pvs[channel]
            if not pv.connected:
                raise EzcaConnectError("Channel disconnected: %s" % (pv.pvname))
            return pv
        # handle ifo-rooted channels (begin with ':')
        if channel[0] == ':':
            # if no prefix was specified, just remove the : from the
            # channel and continue
            if self.prefix[-1] == ':':
                channel = channel[1:]
            # otherwise add a new non-prefixed pv for the channel
            elif self._ifo:
                fullchannel = self._ifo + channel
                self._log.warning("connecting to ifo-rooted channel: %s" % fullchannel)
                self._dev.add_pv(fullchannel, channel)
            else:
                raise EzcaError("IFO not specified, can not connect to ifo-rooted channel")
        pv = self._dev.PV(channel, connect=True, timeout=self._timeout)
        if not pv.wait_for_connection():
            name = pv.pvname
            del self._dev._pvs[channel]
            if self.ca_fail_no_connect:
                raise EzcaConnectError("Could not connect to channel (timeout=%ds): %s" % (self._timeout, name))
        return pv

    def check_connections(self):
        """Return list of non-connected channels."""
        channels = []
        for channel, pv in self._dev._pvs.items():
            if not pv.connected:
                channels.append(pv.pvname)
        return channels

    ########################################
    ########################################

    def read(self, channel, log=False, **kw):
        """Read channel value.

        See connect() for more info.

        """
        if not self.ca_enable_read:
            return float('nan')
        pv = self.connect(channel)
        if not pv.connected and not self.ca_fail_no_connect:
            return float('nan')
        value = pv.get(**kw)
        if value is None:
            raise EzcaConnectError("Could not get value from channel: %s" % (pv.pvname))
        self._logget(pv, log=log)
        return value

    def __getitem__(self, channel):
        return self.read(channel)

    ########################################

    def write(self, channel, value, wait=True, monitor=True, setpoint=None, log=True, **kw):
        """Write channel value.

        If `wait` is not True, the write will not wait for
        confirmation from the server that the write was accepted.

        If `monitor` is True, all writes are recorded in a setpoint
        cache.  See check_setpoints() for checking current settings
        against setpoints.  `setpoint` can set a setpoint value for
        this write different than the actual write value.

        If `log` is False logging is disabled for this write call.

        See connect() for more info.

        """
        if not self.ca_enable_write:
            return
        kw['wait'] = wait
        pv = self.connect(channel)
        if not pv.connected and not self.ca_fail_no_connect:
            return
        oldvalue = pv.get()
        pv.put(value, **kw)
        # only log if value is changing
        if value != oldvalue and log:
            self._logput(pv, value)
        # record setpoints into cache
        if setpoint:
            pv._setpoint = setpoint
        else:
            pv._setpoint = value
        if monitor:
            record = True
            # skip known momentary channels
            for s in SPM_MOMENTARY_SUFFIXES:
                if pv.pvname[-len(s):] == s:
                    record = False
                    break
            if record:
                self._setpoints[channel] = (pv.pvname, value)

    def __setitem__(self, channel, value):
        return self.write(channel, value)

    ########################################

    def init_setpoints(self, table, init=False):
        """Initialize setpoint table.

        Initialize setpoint table from a list of channels.  If a list
        element is a (channel_name, setpoint_value) tuple the setpoint
        will be initialized with the specified setpoint value.
        Otherwise, the current value of the specified channel will be
        used.

        """
        if init:
            self._setpoints = {}
        for data in table:
            setpoint = None
            if type(data) is str:
                channel = data
            else:
                if len(data) != 2:
                    raise EzcaError("Setpoint intialization must be channel name string or (chan, value) tuple: %s" % str(data))
                channel = data[0]
                setpoint = data[1]
                if type(setpoint) in [tuple, list]:
                    try:
                        setpoint = SFMask(setpoint)
                    except:
                        raise EzcaError("Setpoint intialization invalid button list for '%s': %s" % (channel, str(setpoint)))
            pv = self.connect(channel)
            if not setpoint:
                setpoint = pv.get()
            self._setpoints[channel] = (pv.pvname, setpoint)

    @property
    def setpoints(self):
        """Dictionary of all current setpoints"""
        return self._setpoints

    def check_setpoints(self):
        """Return tuple of channels that have changed relative to their last set point.

        All channels in the set point cache are checked against their
        current values.  Each element in the return is a tuple with
        the following elements:

           (full_channel_name, setpoint_value, current_value, difference)

        For switch settings, a SFMask of the SWSTAT value is stored, the
        difference is calculated as "setpoint ^ current", and a string
        representation of the buttons is returned.

        """
        changed = ()
        for channel, spdata in self._setpoints.items():
            full, setpoint = spdata

            try:
                if type(setpoint) is str:
                    current = self.read(channel, as_string=True)
                    test = current == setpoint
                elif type(setpoint) is SFMask:
                    current = SFMask.from_swstat(int(self.read(channel)))
                    test = current.SWSTAT == setpoint.SWSTAT
                else:
                    current = self.read(channel)
                    test = current == setpoint
            except EzcaConnectError:
                changed += ((full, '', 'DEAD', ''),)
                continue

            if not test:
                if type(setpoint) is str:
                    setpoint = "'%s'" % setpoint
                    current = "'%s'" % current
                    diff = ''
                elif type(setpoint) is SFMask:
                    diff = (setpoint ^ current).abrev
                    setpoint = setpoint.abrev
                    current = current.abrev
                else:
                    diff = current - setpoint
                changed += ((full, setpoint, current, diff),)
        return changed

    ########################################

    def setpoint_snap(self, snapfile):
        """Record setpoints to a file.

        """
        with open(snapfile, 'w') as f:
            for channel, spdata in self._setpoints.items():
                line = '%s %s\n' % spdata
                f.write(line)

    def burtrb(self, snapfile):
        """Record all PVs to BURT snapshot file.

        """
        with open(snapfile, 'w') as f:
            # FIXME: write header
            for channel, pv in self.pvs.items():
                try:
                    value = pv._setpoint
                    flag = ''
                except AttributeError:
                    value = pv.char_value
                    flag = 'RO '
                line = '%s%s %d %s\n' % (flag, pv.pvname, pv.count, value)
                f.write(line)

    def burtwb(self, burtfile, wait=True):
        """Apply settings from BURT snapshot file.

        Read-only lines beginning with ['-', 'RO', 'RON'] are skipped.
        See the following for BURT snapshot file specification:

        http://www.aps.anl.gov/epics/EpicsDocumentation/ExtensionsManuals/Burt/Components.html#REF92638

        """
        inheader = False
        plen = len(self.prefix)
        with open(burtfile, 'r') as f:
            # FIXME: we should maybe quickly slurp the entire file
            # into memory and then parse, so we don't have to worry
            # about the file changing underneath us as we apply
            for line in f:
                line = line.strip()
                if line == '--- Start BURT header':
                    inheader = True
                    continue
                elif line == '--- End BURT header':
                    inheader = False
                    continue
                if inheader:
                    continue
                data = line.split()
                # if line is specified RO skip
                if data[0] in ['-', 'RO', 'RON']:
                    continue
                channel = data[0]
                # FIXME: use count appropriately?
                count = data[1]
                value = data[2]
                try:
                    # try to convert the value to a float
                    value = float(value)
                except ValueError:
                    # if that fails, write the value as a string as is
                    value = value
                # FIXME: what about additional fields?
                # strip leading prefix if there
                index = channel.find(self.prefix)
                if index == 0:
                    channel = channel[plen:]
                # write the value
                self.write(channel, value, wait=wait)

    ########################################

    def switch(self, sfm_name, *args, **kwargs):
        """Manipulate buttons in standard filter module.

        Equivalent to:

          LIGOFilter(sfm_name).switch(*args, **kwargs), except it will ignore value errors
          if ca_fail_no_connect is false

        See help(LIGOFilter.switch) for more info.

        """
        try:
            result = LIGOFilter(sfm_name, self).switch(*args, **kwargs)
        except (ValueError, ezca.errors.EzcaConnectError, ezca.errors.LIGOFilterError) as e:
            if self.ca_fail_no_connect:
                raise e from None
            else:
                self._log.info(f"An exception was caught when switching {sfm_name}, "
                               "but it was ignored because EZCA_CA == NOFAIL.\nThe switch was not written to.")
                return None
        return result

    def is_ramping(self, sfm_ramp_name):
        """Return True if SFM offset or gain is ramping."""
        match = re.match(const.FILTER_RAMP_NAME_RE, sfm_ramp_name)
        if match is None:
            raise EzcaError("'%s' is not a filter module ramp name" % sfm_ramp_name)
        sfm_name = match.group(1)
        ramp_name = match.group(2)
        ligo_filter = LIGOFilter(sfm_name, self)
        return getattr(ligo_filter, 'is_'+ramp_name.lower()+'_ramping')()

    def is_gain_ramping(self, sfm_name):
        """Return True if SFM gain is ramping."""
        return LIGOFilter(sfm_name, self).is_gain_ramping()

    def is_offset_ramping(self, sfm_name):
        """Return True if SFM offset is ramping."""
        return LIGOFilter(sfm_name, self).is_offset_ramping()

    def ramp_gain(self, sfm_name, value, ramp_time=_no_value, wait=True):
        """Ramp the gain in a SFM."""
        LIGOFilter(sfm_name, self).ramp_gain(value=value, ramp_time=ramp_time, wait=wait)

    def ramp_offset(self, sfm_name, value, ramp_time=_no_value, wait=True):
        """Ramp the offset in a SFM"""
        LIGOFilter(sfm_name, self).ramp_offset(value=value, ramp_time=ramp_time, wait=wait)

    def LIGOFilter(self, filter_name):
        """Return LIGOFilter object for the specified SFM."""
        return LIGOFilter(filter_name, self)
    get_LIGOFilter = LIGOFilter

    def LIGOFilterManager(self, filter_names):
        """Return LIGOFilterManager for the specified list of SFM."""
        return LIGOFilterManager(filter_names, self)
    get_LIGOFilterManager = LIGOFilterManager
