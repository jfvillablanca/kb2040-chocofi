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

_______ = KC.TRNS
XXXXXXX = KC.NO

ESCAPE = KC.HT(KC.ESC, KC.LGUI) 

NAV = KC.LT(2, KC.TAB)
SYMBOL = KC.LT(3, KC.ENT) 
BSPC = KC.LT(4, KC.BSPC)

# fmt:off
keyboard.keymap = [
    [  # 0: BASE
        KC.Q,    KC.W,    KC.F,    KC.P,    KC.G,                            KC.J,    KC.L,    KC.U,    KC.Y, KC.SCLN,\
        KC.A,    KC.R,    KC.S,    KC.T,    KC.D,                            KC.H,    KC.N,    KC.E,    KC.I,    KC.O,\
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                            KC.K,    KC.M, KC.COMM,  KC.DOT, KC.SLSH,\
                                   ESCAPE,  BSPC,    NAV,         KC.SPC,  SYMBOL, KC.RSFT,
    ],
    [  # 1. QWERTY
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                            KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,\
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                            KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN,\
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                            KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH,\
                                   _______, _______, _______,    _______, _______, _______,
    ],
    [  # 2. NAVIGATION
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, XXXXXXX,                      KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                   XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # 3. SYMBOL
        KC.EQL,  KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.MINS, KC.DLR,  KC.PERC, KC.CIRC, KC.PLUS,                      XXXXXXX, KC.RCTL, KC.RSFT, KC.RALT, KC.RGUI,\
        KC.GRV,  KC.EXLM, KC.AT,   KC.HASH, KC.BSLS,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                   KC.LBRC, KC.RBRC, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [  # 4. NUMBER
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX,   KC.N7,   KC.N8,   KC.N9, XXXXXXX,\
        KC.LGUI, KC.LALT, KC.LSFT, KC.LCTL, XXXXXXX,                      XXXXXXX,   KC.N4,   KC.N5,   KC.N6, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                      XXXXXXX,   KC.N1,   KC.N2,   KC.N3, XXXXXXX,\
                                   XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX,  KC.DOT,   KC.N0,
    ],
    [  # 5. FUNCTION
        KC.F12,  KC.F7,   KC.F8,   KC.F9,   XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        KC.F11,  KC.F4,   KC.F5,   KC.F6,   XXXXXXX,                      XXXXXXX, KC.RCTL, KC.RSFT, KC.RALT, KC.RGUI,\
        KC.F10,  KC.F1,   KC.F2,   KC.F3,   XXXXXXX,                      XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                   XXXXXXX, XXXXXXX, XXXXXXX,    XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    # [  # BLANK
    #     XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                       XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #     XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                       XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #     XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                       XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
    #                                XXXXXXX, XXXXXXX, XXXXXXX,     XXXXXXX, XXXXXXX, XXXXXXX,
    # ],
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
