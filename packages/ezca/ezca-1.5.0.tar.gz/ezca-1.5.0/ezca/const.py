from functools import reduce

SWITCH_READ_TIME_STEP = 0.125
RAMP_READ_TIME_STEP = SWITCH_READ_TIME_STEP
SWITCH_EZCA_TIMEOUT_ERROR_MESSAGE = "Did not observe effect of writing value to switch channel "\
        +"{channel_name} within EZCA_TIMEOUT ({timeout}s)."
READONLY_CHANNEL_ERROR_MESSAGE = "Cannot write {write_value} to {channel_name} because the bit for "\
        +"{readonly_channel_name} is read-only."

FILTER_SW_NAMES = ('SW1','SW2')
FILTER_MODULE_NUM_RANGE = list(range(1, 10+1))
FILTER_NAMES = ['FM'+str(i) for i in FILTER_MODULE_NUM_RANGE]
FILTER_NAME_REGEX = r'FM([1-9]|10)'
FILTER_RAMP_NAMES = ('GAIN', 'OFFSET')
FILTER_RAMP_NAME_RE = r'(.*)_(GAIN|OFFSET)'
FILTER_WRITABLE_CHANNELS = ('OFFSET', 'TRAMP', 'GAIN', 'LIMIT', 'RSET')

CA_TIMEOUT = 2  # seconds
MEDM_AND_CAS_TIMEOUT = 5  # seconds
EMULATOR_STARTUP_TIMEOUT = 5  # seconds

# FIXME make immutable
class SwitchMask(object):
    """
    Represents a single mask for a filter switch channel. Note that the attributes of
    this class is designed to be "immutable" in the sense that 
    """

    def __init__(self, switch_name, bit_mask):
        # private assertion that switch_name is known
        assert(switch_name in FILTER_SW_NAMES)
        self.__switch_name = switch_name

        # private development assertion that bit_mask is a power of 2
        #     http://graphics.stanford.edu/~seander/bithacks.html#DetermineIfPowerOf2
        assert(bit_mask > 0 and (bit_mask & (bit_mask-1)) == 0)
        self.__bit_mask = bit_mask

    def __repr__(self):
        s = "SwitchMask('%s', '%s')" % (self.__switch_name, self.__bit_mask)
        return s

    @property
    def SW(self):
        return self.__switch_name

    @property
    def bit_mask(self):
        return self.__bit_mask

    def __eq__(self, other):
        assert(isinstance(other, SwitchMask))
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.__switch_name, self.__bit_mask))


ACTIONS = ('ON', 'OFF', 'PRESS')

# the following masks are defined according to LIGO-T0900606
WRITE_MASKS_BASIC = dict(
    COEFF_RESET = SwitchMask('SW1', 1<<0),
    MASTER_RESET = SwitchMask('SW1', 1<<1),
    INPUT = SwitchMask('SW1', 1<<2),
    OFFSET = SwitchMask('SW1', 1<<3),
    FM1 = SwitchMask('SW1', 1<<4),
    FM2 = SwitchMask('SW1', 1<<6),
    FM3 = SwitchMask('SW1', 1<<8),
    FM4 = SwitchMask('SW1', 1<<10),
    FM5 = SwitchMask('SW1', 1<<12),
    FM6 = SwitchMask('SW1', 1<<14),

    FM7 = SwitchMask('SW2', 1<<0),
    FM8 = SwitchMask('SW2', 1<<2),
    FM9 = SwitchMask('SW2', 1<<4),
    FM10 = SwitchMask('SW2', 1<<6),
    LIMIT = SwitchMask('SW2', 1<<8),
    DECIMATION = SwitchMask('SW2', 1<<9),
    OUTPUT = SwitchMask('SW2', 1<<10),
    HOLD = SwitchMask('SW2', 1<<11),
    )

WRITE_MASK_ALIASES = dict(
    IN = WRITE_MASKS_BASIC['INPUT'],
    DECIMATE = WRITE_MASKS_BASIC['DECIMATION'],
    OUT = WRITE_MASKS_BASIC['OUTPUT'],
    )

WRITE_MASKS = dict(WRITE_MASKS_BASIC, **WRITE_MASK_ALIASES)

READONLY_MASKS = dict(
    FM1_ENGAGED = SwitchMask('SW1', 1<<5),
    FM2_ENGAGED = SwitchMask('SW1', 1<<7),
    FM3_ENGAGED = SwitchMask('SW1', 1<<9),
    FM4_ENGAGED = SwitchMask('SW1', 1<<11),
    FM5_ENGAGED = SwitchMask('SW1', 1<<13),
    FM6_ENGAGED = SwitchMask('SW1', 1<<15),

    FM7_ENGAGED = SwitchMask('SW2', 1<<1),
    FM8_ENGAGED = SwitchMask('SW2', 1<<3),
    FM9_ENGAGED = SwitchMask('SW2', 1<<5),
    FM10_ENGAGED = SwitchMask('SW2', 1<<7),
    GAIN_RAMP = SwitchMask('SW2', 1<<12),
    OFFSET_RAMP = SwitchMask('SW2', 1<<13),
    UNUSED_1 = SwitchMask('SW2', 1<<14),
    UNUSED_2 = SwitchMask('SW2', 1<<15),
    )


ALL_MASKS = dict(WRITE_MASKS, **READONLY_MASKS)
ALL_MASKS_STRICT = dict(WRITE_MASKS_BASIC, **READONLY_MASKS)


def __get_whole_bit_mask(masks):
    return dict(
        SW1=reduce(lambda a, b: a | b.bit_mask,
                   [sm for sm in list(masks.values()) if sm.SW == 'SW1'], 0),
        SW2=reduce(lambda a, b: a | b.bit_mask,
                   [sm for sm in list(masks.values()) if sm.SW == 'SW2'], 0),
        )

WHOLE_WRITE_BIT_MASK = __get_whole_bit_mask(WRITE_MASKS)
WHOLE_READONLY_BIT_MASK = __get_whole_bit_mask(READONLY_MASKS)

BUTTONS_ORDERED = [
    'INPUT',
    'OFFSET',
    'FM1',
    'FM1_ENGAGED',
    'FM2',
    'FM2_ENGAGED',
    'FM3',
    'FM3_ENGAGED',
    'FM4',
    'FM4_ENGAGED',
    'FM5',
    'FM5_ENGAGED',
    'FM6',
    'FM6_ENGAGED',
    'FM7',
    'FM7_ENGAGED',
    'FM8',
    'FM8_ENGAGED',
    'FM9',
    'FM9_ENGAGED',
    'FM10',
    'FM10_ENGAGED',
    'LIMIT',
    'OUTPUT',
    'DECIMATION',
    'HOLD',
    ]

SWSTAT_BITS = {
    'FM1': 1<<0,
    'FM2': 1<<1,
    'FM3': 1<<2,
    'FM4': 1<<3,
    'FM5': 1<<4,
    'FM6': 1<<5,
    'FM7': 1<<6,
    'FM8': 1<<7,
    'FM9': 1<<8,
    'FM10': 1<<9,
    'INPUT': 1<<10,
    'OFFSET': 1<<11,
    'OUTPUT': 1<<12,
    'LIMIT': 1<<13,
    'DECIMATION': 1<<15,
    'HOLD': 1<<16,
    }
SWSTAT_BITS_ALL = sum(SWSTAT_BITS.values())

BUTTON_ABREV = {
    'FM1': '1',
    'FM2': '2',
    'FM3': '3',
    'FM4': '4',
    'FM5': '5',
    'FM6': '6',
    'FM7': '7',
    'FM8': '8',
    'FM9': '9',
    'FM10': '10',
    'INPUT': 'IN',
    'OFFSET': 'OF',
    'OUTPUT': 'OT',
    'LIMIT': 'LT',
    'DECIMATION': 'DC',
    'HOLD': 'HD',
    }
