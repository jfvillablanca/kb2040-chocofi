from storage import getmount

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.sticky_keys import StickyKeys
from kmk.modules.tapdance import TapDance

keyboard = KMKKeyboard()

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(split_type=SplitType.UART, split_side=side, use_pio=True, uart_flip=True)

layers = Layers()
holdtap = HoldTap()
sticky_keys = StickyKeys()
tapdance = TapDance()
mousekeys = MouseKeys(
    max_speed = 10,
    acc_interval = 20,
    move_step = 1
)
caps_word=CapsWord(timeout=3000) 
caps_word.keys_ignored = [ KC.COMMA ] 

tapdance.tap_time = 200
keyboard.modules = [holdtap, layers, mousekeys, split, sticky_keys, tapdance, caps_word]

def mkHmr(hold_key):
    return lambda tap_key: KC.HT(tap_key, hold_key, prefer_hold=False, tap_interrupted=False, tap_time=280)

GL = mkHmr(KC.LGUI)
AL = mkHmr(KC.LALT)
SL = mkHmr(KC.LSFT)
CL = mkHmr(KC.LCTL)

GR = mkHmr(KC.RGUI)
AR = mkHmr(KC.RALT)
SR = mkHmr(KC.RSFT)
CR = mkHmr(KC.RCTL)

__________ = KC.TRNS
XXXXXXXXXX = KC.NO

L2 = KC.LT(2, KC.SK(KC.LSFT))
L3 = KC.LT(3, KC.SPC)
L4 = KC.LT(4, KC.BSPC)
L5 = KC.LT(5, KC.ENT)
L6 = KC.LT(6, KC.QUOTE)
# TODO
L7 = KC.LT(0, KC.SK(KC.RSFT))

L2_SFT = KC.TD(L2, KC.TAB)
L3_SPC = KC.TD(L3, KC.ESC)

# fmt:off
keyboard.keymap = [
    [  # 0: BASE
        KC.Q,       KC.W,       KC.F,       KC.P,       KC.G,                                              KC.J,       KC.L,       KC.U,       KC.Y,     KC.SCLN,\
        GL(KC.A),   AL(KC.R),   SL(KC.S),   CL(KC.T),   KC.D,                                              KC.H,   CR(KC.N),   SR(KC.E),   AR(KC.I),    GR(KC.O),\
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,                                              KC.K,       KC.M,    KC.COMM,     KC.DOT,     KC.SLSH,\
                                            L6,         L4,         L2_SFT,                  L3_SPC,         L5,         L7,
    ],
    [  # 1. QWERTY
        KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,                                              KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,\
        KC.A,       KC.S,       KC.D,       KC.F,       KC.G,                                              KC.H,       KC.J,       KC.K,       KC.L,    KC.SCLN,\
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,                                              KC.N,       KC.M,    KC.COMM,     KC.DOT,    KC.SLSH,\
                                            __________, __________, __________,          __________, __________, __________,
    ],
    [  # 2. NAVIGATION
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
        KC.LGUI,    KC.LALT,    KC.LSFT,    KC.LCTL,    XXXXXXXXXX,                                     KC.LEFT,    KC.DOWN,      KC.UP,    KC.RGHT, XXXXXXXXXX,\
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
                                            XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,          XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,
    ],
    [  # 3. SYMBOL
        KC.EQL,     KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,                                          KC.CW, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
        KC.MINS,    KC.DLR,     KC.PERC,    KC.CIRC,    KC.QUOTE,                                    XXXXXXXXXX,    KC.RCTL,    KC.RSFT,    KC.RALT,    KC.RGUI,\
        KC.GRV,     KC.EXLM,    KC.AT,      KC.HASH,    KC.BSLS,                                        KC.CAPS, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
                                            KC.LBRC,    KC.RBRC,    XXXXXXXXXX,          XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,
    ],
    [  # 4. NUMBER
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX,      KC.N7,      KC.N8,      KC.N9, XXXXXXXXXX,\
        KC.LGUI,    KC.LALT,    KC.LSFT,    KC.LCTL,    XXXXXXXXXX,                                  XXXXXXXXXX,      KC.N4,      KC.N5,      KC.N6, XXXXXXXXXX,\
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX,      KC.N1,      KC.N2,      KC.N3, XXXXXXXXXX,\
                                            XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,               KC.N0,     KC.DOT, XXXXXXXXXX,
    ],
    [  # 5. FUNCTION
        KC.F12,     KC.F7,      KC.F8,      KC.F9,      XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
        KC.F11,     KC.F4,      KC.F5,      KC.F6,      XXXXXXXXXX,                                  XXXXXXXXXX,    KC.RCTL,    KC.RSFT,    KC.RALT,    KC.RGUI,\
        KC.F10,     KC.F1,      KC.F2,      KC.F3,      XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
                                            XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,          XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,
    ],
    [  # 6. MOUSE
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
        KC.LGUI,    KC.LALT,    KC.LSFT,    KC.LCTL,    XXXXXXXXXX,                                    KC.MS_LT,   KC.MS_DN,   KC.MS_UP,   KC.MS_RT, XXXXXXXXXX,\
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
                                            XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,           KC.MB_LMB,  KC.MB_RMB,  KC.MB_MMB,
    ],
    # [  # BLANK
    #     XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
    #     XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
    #     XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
    #                                         XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,          XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,
    # ],
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
