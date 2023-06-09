#! /usr/bin/env python3
from tkinter import *
import keycodes as keycode
from layouts.keymap import Keymap





class Keyboard(object):
    keydown = "/sys/devices/platform/virt-keyboard.0/keydown"
    keyup = "/sys/devices/platform/virt-keyboard.0/keyup"
    
    def __init__(self) -> None:
        self.keymaps = {}
        self.skey_down = open(Keyboard.keydown, "w")
        self.skey_up = open(Keyboard.keyup, "w")

    def add_language(self, lang, description):
        self.keymaps[lang] = {
            "description": description,
            "keymap": Keymap(lang)
        }
    
    def send_keycode(self, kcode, status):
        print("keycode: {} event: {}".format(kcode, status))

        if status:
            self.skey_down.write(str(kcode))
            self.skey_down.flush()
        else:
            self.skey_up.write(str(kcode))
            self.skey_up.flush()
    
    def toggle_key(self, key):
        if key.hold == False:
            self.skey_down.write(str(key.keycode.keycode))
            self.skey_down.flush()
            key.hold = True
        else:
            self.skey_up.write(str(key.keycode.keycode))
            self.skey_up.flush()
            key.hold = False
    
    def get_keymap(self, lang):
        
        if lang in self.keymaps.keys():
            return self.keymaps[lang]["keymap"]
    
    
    def close(self):
        self.skey_down.close()
        self.skey_up.close()
    
    
    

        




keyboard = Keyboard()
keyboard.add_language("chCN", "Simplified Chinese")
keyboard.add_language("chZH", "Traditional Chinese")

keymap = keyboard.get_keymap("chCN")
print(keymap)

win = Tk()
win.geometry("{}x250+0-0".format(win.winfo_screenwidth()))
win.attributes('-type', 'dock')
win.configure(background=keymap.background.to_hex())

ws = Frame(win, bg=keymap.background.to_hex(), padx=1, pady= 1)
for i in range(0, len(keymap.keys)):
    
    for j in range(0, len(keymap.keys[i])):
        c = keymap.keys[i][j]
        b = Button(ws, text=c.keycode.text,  width=3, height=2, highlightthickness=0, bd=0)
        if str(c.keycode.keycode).isdigit() and int(c.keycode.key_type) == 1:
            b.bind("<ButtonPress>", lambda eventp, key=c: keyboard.toggle_key(key))
        else:
            b.bind("<ButtonPress>", lambda eventp,
                   kcode=c.keycode.keycode: keyboard.send_keycode(kcode, 1))
            b.bind("<ButtonRelease>", lambda eventr,
                   kcode=c.keycode.keycode: keyboard.send_keycode(kcode, 0))
        print(c.key_style.background.to_hex())
        b.configure(background=c.key_style.background.to_hex(),
                    foreground="white", activebackground="blue")
        
        if (c.keycode.text == "hide"):
            b.bind("<ButtonPress>", lambda eventp: exit(0))
        b.grid(row=i, column=j)

ws.pack(expand=True)
win.mainloop()
