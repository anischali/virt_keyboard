#! /usr/bin/env python3



from tkinter import *
from layouts.keymap import Keymap




class Keyboard(Frame):
    #keydown = "/sys/devices/platform/virt-keyboard.0/keydown"
    #keyup = "/sys/devices/platform/virt-keyboard.0/keyup"
    
    keydown = "./keydown"
    keyup = "./keyup"
    
    def __init__(self, window, *args, **kwargs) -> None:
        Frame.__init__(self, window, *args, **kwargs)
        self.window = window
        self.keymaps = {}
        self.skey_down = open(Keyboard.keydown, "w")
        self.skey_up = open(Keyboard.keyup, "w")
        self.current_lang = "enUS"
        self.curr_keymap = self.get_keymap(self.current_lang)
        self.ws = None
        self.hidden = True

    def add_language(self, lang):
        self.keymaps[lang] = Keymap(lang)
    
    def change_language(self):
        pass
    
    def send_keycode(self, key, status):
        print("keycode: {} event: {}".format(key.keycode.keycode, status))

        if status:
            self.skey_down.write(str(key.keycode.keycode))
            self.skey_down.flush()
        else:
            self.skey_up.write(str(key.keycode.keycode))
            self.skey_up.flush()
    
    def toggle_key(self, key):
        if key.hold == False:
            self.skey_down.write(str(key.keycode.keycode))
            self.skey_down.flush()
            key.key_button.configure(activebackground=self.curr_keymap.active_bg.to_hex(), background=self.curr_keymap.active_bg.to_hex())
            key.hold = True
        else:
            self.skey_up.write(str(key.keycode.keycode))
            self.skey_up.flush()
            key.key_button.configure(background=key.key_style.background.to_hex())
            key.hold = False
        
    def get_keymap(self, lang):
        
        if lang in self.keymaps.keys():
            return self.keymaps[lang]
    
    def hide_keyboard(self, hide):
        
        if hide != self.hidden:
            self.hidden = hide
            self.window.geometry("{}x{}+0-0".format(win.winfo_screenwidth(), (3 if hide else 250)))
        
    
    def setup_view(self):
        self.curr_keymap = self.get_keymap(self.current_lang)
        self.window.configure(background=self.curr_keymap.background.to_hex())
        self.configure(bg=self.curr_keymap.background.to_hex())
        
        
        for i in range(0, len(self.curr_keymap.keys)):
            row = Frame(self)
            for j in range(0, len(self.curr_keymap.keys[i])):
                c = self.curr_keymap.keys[i][j]
                b = Button(row, text=c.keycode.text, relief="flat",
                            width=c.key_style.width, 
                            height=self.curr_keymap.keys_height,
                            highlightthickness=2, 
                            highlightbackground=self.curr_keymap.background.to_hex())
                
                if str(c.keycode.keycode).isdigit() and int(c.keycode.key_type) == 1:
                    b.bind("<ButtonPress>", lambda eventp, key=c: keyboard.toggle_key(key))
                else:
                    b.bind("<ButtonPress>", lambda eventp,
                       key=c: keyboard.send_keycode(key, 1))
                    b.bind("<ButtonRelease>", lambda eventr,
                       key=c: keyboard.send_keycode(key, 0))

                b.configure(bg=c.key_style.background.to_hex(),
                    foreground="white", activebackground=self.curr_keymap.background.to_hex())
        
                if (c.keycode.text == "hide"):
                    b.bind("<ButtonPress>", lambda eventp: keyboard.hide_keyboard(True))
                
                b.grid(row=0, column=j)
                c.key_button = b
            row.pack(expand=1)
            
        self.pack(expand=True)
        
    
    def close(self):
        self.skey_down.close()
        self.skey_up.close()
    
    
    

        






win = Tk()
keyboard = Keyboard(win)
keyboard.add_language("chCN")
keyboard.add_language("chZH")
keyboard.add_language("enUS")

win.geometry("{}x250+0-0".format(win.winfo_screenwidth()))
win.attributes('-type', 'dock')
keyboard.setup_view()
keyboard.hide_keyboard(False)
win.bind('<Enter>', lambda eventp: keyboard.hide_keyboard(False))

win.mainloop()
