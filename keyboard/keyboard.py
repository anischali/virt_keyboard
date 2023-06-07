#! /usr/bin/env python3
from tkinter import *
import keycodes as keycode
from layouts.keymap import Keymap

keydown = "/sys/devices/platform/virt-keyboard.0/keydown"
keyup = "/sys/devices/platform/virt-keyboard.0/keyup"

chZH_keymap = Keymap("chZH")


keymap_lst = {
    "ESC": keycode.KEY_ESC,
    "1": keycode.KEY_1,
    "2": keycode.KEY_2,
    "3": keycode.KEY_3,
    "4": keycode.KEY_4,
    "5": keycode.KEY_5,
    "6": keycode.KEY_6,
    "7": keycode.KEY_7,
    "8": keycode.KEY_8,
    "9": keycode.KEY_9,
    "0": keycode.KEY_0,
    "-": keycode.KEY_MINUS,
    "=": keycode.KEY_EQUAL,
    "Backspace": keycode.KEY_BACKSPACE,
    "Tab": keycode.KEY_TAB,
    "q": keycode.KEY_Q,
    "w": keycode.KEY_W,
    "e": keycode.KEY_E,
    "r": keycode.KEY_R,
    "t": keycode.KEY_T,
    "y": keycode.KEY_Y,
    "u": keycode.KEY_U,
    "i": keycode.KEY_I,
    "o": keycode.KEY_O,
    "p": keycode.KEY_P,
    "[": keycode.KEY_LEFTBRACE,
    "]": keycode.KEY_RIGHTBRACE,
    "Enter": keycode.KEY_ENTER,
    "Ctrl L": keycode.KEY_LEFTCTRL,
    "a": keycode.KEY_A,
    "s": keycode.KEY_S,
    "d": keycode.KEY_D,
    "f": keycode.KEY_F,
    "g": keycode.KEY_G,
    "h": keycode.KEY_H,
    "j": keycode.KEY_J,
    "k": keycode.KEY_K,
    "l": keycode.KEY_L,
    ";": keycode.KEY_SEMICOLON,
    "'": keycode.KEY_APOSTROPHE,
    "|": keycode.KEY_GRAVE,
    "Shift L": keycode.KEY_LEFTSHIFT,
    "\\": keycode.KEY_BACKSLASH,
    "z": keycode.KEY_Z,
    "x": keycode.KEY_X,
    "c": keycode.KEY_C,
    "v": keycode.KEY_V,
    "b": keycode.KEY_B,
    "n": keycode.KEY_N,
    "m": keycode.KEY_M,
    ",": keycode.KEY_COMMA,
    ".": keycode.KEY_DOT,
    "/": keycode.KEY_SLASH,
    "Shift R.": keycode.KEY_RIGHTSHIFT,
    "": keycode.KEY_KPASTERISK,
    "Alt L": keycode.KEY_LEFTALT,
    "Space": keycode.KEY_SPACE,
    "Caps": keycode.KEY_CAPSLOCK,
    "F1": keycode.KEY_F1,
    "F2": keycode.KEY_F2,
    "F3": keycode.KEY_F3,
    "F4": keycode.KEY_F4,
    "F5": keycode.KEY_F5,
    "F6": keycode.KEY_F6,
    "F7": keycode.KEY_F7,
    "F8": keycode.KEY_F8,
    "F9": keycode.KEY_F9,
    "F10": keycode.KEY_F10,
    "Num.": keycode.KEY_NUMLOCK,
    "": keycode.KEY_SCROLLLOCK,
    ".KP7": keycode.KEY_KP7,
    ".KP8": keycode.KEY_KP8,
    ".KP9": keycode.KEY_KP9,
    ".KPMINUS": keycode.KEY_KPMINUS,
    ".KP4": keycode.KEY_KP4,
    ".KP5": keycode.KEY_KP5,
    ".KP6": keycode.KEY_KP6,
    ".KPPLUS": keycode.KEY_KPPLUS,
    ".KP1": keycode.KEY_KP1,
    ".KP2": keycode.KEY_KP2,
    ".KP3": keycode.KEY_KP3,
    ".KP0": keycode.KEY_KP0,
    ".KPDOT": keycode.KEY_KPDOT,
    ".ZEN": keycode.KEY_ZENKAKUHANKAKU,
    ".102": keycode.KEY_102ND,
    "F11": keycode.KEY_F11,
    "F12": keycode.KEY_F12,
    ".R0": keycode.KEY_RO,
    ".KATAKANA": keycode.KEY_KATAKANA,
    ".HIRAGANA": keycode.KEY_HIRAGANA,
    ".HENKAN": keycode.KEY_HENKAN,
    ".KATAKANAHIRAGANA": keycode.KEY_KATAKANAHIRAGANA,
    ".MUHENKAN": keycode.KEY_MUHENKAN,
    ".KPJPCOMMA": keycode.KEY_KPJPCOMMA,
    ".KPENTER": keycode.KEY_KPENTER,
    "Ctrl R.": keycode.KEY_RIGHTCTRL,
    ".KPSLASH": keycode.KEY_KPSLASH,
    ".SYSRQ": keycode.KEY_SYSRQ,
    "Alt R.": keycode.KEY_RIGHTALT,
    "Home": keycode.KEY_HOME,
    "Up": keycode.KEY_UP,
    "PgUp": keycode.KEY_PAGEUP,
    "Left": keycode.KEY_LEFT,
    "Right": keycode.KEY_RIGHT,
    "End": keycode.KEY_END,
    "Down": keycode.KEY_DOWN,
    "pgDown": keycode.KEY_PAGEDOWN,
    "Insert": keycode.KEY_INSERT,
    "Del": keycode.KEY_DELETE,
    ".MACRO": keycode.KEY_MACRO,
    ".MUTE": keycode.KEY_MUTE,
    ".VOLUMEDOWN": keycode.KEY_VOLUMEDOWN,
    ".VOLUMEUP": keycode.KEY_VOLUMEUP,
    ".POWER": keycode.KEY_POWER,
    ".KPEQUAL": keycode.KEY_KPEQUAL,
    ".KPPLUSMINUS": keycode.KEY_KPPLUSMINUS,
    ".PAUSE": keycode.KEY_PAUSE,
    ".KPCOMMA": keycode.KEY_KPCOMMA,
    ".HANGUEL": keycode.KEY_HANGUEL,
    ".HANJA": keycode.KEY_HANJA,
    ".YEN": keycode.KEY_YEN,
    ".LEFTMETA": keycode.KEY_LEFTMETA,
    ".RIGHTMETA": keycode.KEY_RIGHTMETA,
    ".COMPOSE": keycode.KEY_COMPOSE,
    ".STOP": keycode.KEY_STOP,
    ".CALC": keycode.KEY_CALC,
    ".SETUP": keycode.KEY_SETUP,
    ".SLEEP": keycode.KEY_SLEEP,
    ".WAKEUP": keycode.KEY_WAKEUP,
    ".PROG1": keycode.KEY_PROG1,
    ".SCREENLOCK": keycode.KEY_SCREENLOCK,
    ".MAIL": keycode.KEY_MAIL,
    ".BOOKMARKS": keycode.KEY_BOOKMARKS,
    ".COMPUTER": keycode.KEY_COMPUTER,
    ".BACK": keycode.KEY_BACK,
    ".FORWARD": keycode.KEY_FORWARD,
    ".EJECTCLOSECD": keycode.KEY_EJECTCLOSECD,
    ".NEXTSONG": keycode.KEY_NEXTSONG,
    ".PLAYPAUSE": keycode.KEY_PLAYPAUSE,
    ".PREVIOUSSONG": keycode.KEY_PREVIOUSSONG,
    ".STOPCD": keycode.KEY_STOPCD,
    ".HOMEPAGE": keycode.KEY_HOMEPAGE,
    ".REFRESH": keycode.KEY_REFRESH,
    ".F13": keycode.KEY_F13,
    ".F14": keycode.KEY_F14,
    ".F15": keycode.KEY_F15,
    ".F21": keycode.KEY_F21,
    ".SUSPEND": keycode.KEY_SUSPEND,
    ".CAMERA": keycode.KEY_CAMERA,
    ".EMAIL": keycode.KEY_EMAIL,
    ".SEARCH": keycode.KEY_SEARCH,
    ".BRIGHTNESSDOWN": keycode.KEY_BRIGHTNESSDOWN,
    ".BRIGHTNESSUP": keycode.KEY_BRIGHTNESSUP,
    ".MEDIA": keycode.KEY_MEDIA,
    ".SWITCHVIDEOMODE": keycode.KEY_SWITCHVIDEOMODE,
    ".BATTERY": keycode.KEY_BATTERY,
    ".UNKNOWN": keycode.KEY_UNKNOWN,
}


with open(keydown, "w") as skeydown, open(keyup, "w") as skeyup:

    def send_keycode(kcode, status):
        print("keycode: {} event: {}".format(kcode, status))

        if status:
            skeydown.write(str(kcode))
            skeydown.flush()
        else:
            skeyup.write(str(kcode))
            skeyup.flush()

    def toggle_key(key):
        if key.hold == False:
            skeydown.write(str(key.keycode.keycode))
            skeydown.flush()
            key.hold = True
        else:
            skeyup.write(str(key.keycode.keycode))
            skeyup.flush()
            key.hold = False

    def make_event(k, s):
        return lambda kcode=k: send_keycode(kcode, s)

    win = Tk()
    win.geometry("{}x250+0-0".format(win.winfo_screenwidth()))
    win.attributes('-type', 'dock')
    win.configure(background=chZH_keymap.background.to_hex())

    buttons = []
    for i in range(0, len(chZH_keymap.keys)):
        buttons.append([])
        for j in range(0, len(chZH_keymap.keys[i])):
            c = chZH_keymap.keys[i][j]
            b = Button(text=c.keycode.text,  width=3, height=2)
            if str(c.keycode.keycode).isdigit() and int(c.keycode.key_type) == 1:
                b.bind("<ButtonPress>", lambda eventp, key=c: toggle_key(key))
            else:
                b.bind("<ButtonPress>", lambda eventp,
                       kcode=c.keycode.keycode: send_keycode(kcode, 1))
                b.bind("<ButtonRelease>", lambda eventr,
                       kcode=c.keycode.keycode: send_keycode(kcode, 0))

            b.configure(background=c.key_style.background.to_hex(),
                        foreground="white")
            buttons[i].append(b)
            buttons[i][j].grid(row=i, column=j, sticky=N+S+E+W)
            if (c.keycode.text == "hide"):
                b.bind("<ButtonPress>", lambda eventp: exit(0))

    win.mainloop()
