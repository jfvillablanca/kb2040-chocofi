from storage import getmount

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType

keyboard = KMKKeyboard()

side = SplitSide.RIGHT if str(getmount('/').label)[-1] == 'R' else SplitSide.LEFT
split = Split(split_type=SplitType.UART, split_side=side, use_pio=True, uart_flip=True)

layers = Layers()
holdtap = HoldTap()

keyboard.modules = [layers, holdtap, split]

__________ = KC.TRNS
XXXXXXXXXX = KC.NO

ESCAPE = KC.HT(KC.ESC, KC.LGUI) 

NAV = KC.LT(2, KC.TAB)
SYMBOL = KC.LT(3, KC.ENT) 
BSPC = KC.LT(4, KC.BSPC)

# fmt:off
keyboard.keymap = [
    [  # 0: BASE
        KC.Q,       KC.W,       KC.F,       KC.P,       KC.G,                                              KC.J,       KC.L,      KC.U,       KC.Y,     KC.SCLN,\
        KC.A,       KC.R,       KC.S,       KC.T,       KC.D,                                              KC.H,       KC.N,      KC.E,       KC.I,        KC.O,\
        KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,                                              KC.K,       KC.M,   KC.COMM,     KC.DOT,     KC.SLSH,\
                                            ESCAPE,     BSPC,       NAV,                     KC.SPC,     SYMBOL,    KC.RSFT,
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
        KC.EQL,     KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,                                     XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
        KC.MINS,    KC.DLR,     KC.PERC,    KC.CIRC,    KC.PLUS,                                     XXXXXXXXXX,    KC.RCTL,    KC.RSFT,    KC.RALT,    KC.RGUI,\
        KC.GRV,     KC.EXLM,    KC.AT,      KC.HASH,    KC.BSLS,                                     XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
                                            KC.LBRC,    KC.RBRC,    XXXXXXXXXX,          XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,
    ],
    [  # 4. NUMBER
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX,      KC.N7,      KC.N8,      KC.N9, XXXXXXXXXX,\
        KC.LGUI,    KC.LALT,    KC.LSFT,    KC.LCTL,    XXXXXXXXXX,                                  XXXXXXXXXX,      KC.N4,      KC.N5,      KC.N6, XXXXXXXXXX,\
        XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,                                  XXXXXXXXXX,      KC.N1,      KC.N2,      KC.N3, XXXXXXXXXX,\
                                            XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,          XXXXXXXXXX,     KC.DOT,      KC.N0,
    ],
    [  # 5. FUNCTION
        KC.F12,     KC.F7,      KC.F8,      KC.F9,      XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
        KC.F11,     KC.F4,      KC.F5,      KC.F6,      XXXXXXXXXX,                                  XXXXXXXXXX,    KC.RCTL,    KC.RSFT,    KC.RALT,    KC.RGUI,\
        KC.F10,     KC.F1,      KC.F2,      KC.F3,      XXXXXXXXXX,                                  XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,\
                                            XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,          XXXXXXXXXX, XXXXXXXXXX, XXXXXXXXXX,
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
