#! /usr/bin/env python3

import tkinter as tk

keydown="/sys/devices/platform/virt-keyboard.0/keydown"
keyup="/sys/devices/platform/virt-keyboard.0/keyup"

with open(keydown, "w") as skeydown, open(keyup, "w") as skeyup:

    keymap = {
        "A":"30",
        "U":"22",
        "M":"50"
    }

    def send_key_A_down(arg):
        print(keymap["A"])
        skeydown.write(keymap["A"])
        skeydown.flush()

    def send_key_A_up(arg):
        print(keymap["A"])
        skeyup.write(keymap["A"])
        skeyup.flush()


    def send_key_U_down(arg):
        print(keymap["U"])
        skeydown.write(keymap["U"])
        skeydown.flush()

    def send_key_U_up(arg):
        print(keymap["U"])
        skeyup.write(keymap["U"])
        skeyup.flush()


    def send_key_M_down(arg):
        print(keymap["M"])
        skeydown.write(keymap["M"])
        skeydown.flush()

    def send_key_M_up(arg):
        print(keymap["M"])
        skeyup.write(keymap["M"])
        skeyup.flush()


    win = tk.Tk()
    win.geometry("{}x200+0-0".format(win.winfo_screenwidth()))
    win.attributes('-type', 'dock')

    buttonA = tk.Button(text="A", width=15, height=2)
    buttonA.pack()
    buttonA.bind("<ButtonPress>", send_key_A_down)
    buttonA.bind("<ButtonRelease>", send_key_A_up)
    buttonM = tk.Button(text="M", width=15, height=2)
    buttonM.pack()
    buttonM.bind("<ButtonPress>", send_key_M_down)
    buttonM.bind("<ButtonRelease>", send_key_M_up)
    buttonU = tk.Button(text="U", width=15, height=2)
    buttonU.pack()
    buttonU.bind("<ButtonPress>", send_key_U_down)
    buttonU.bind("<ButtonRelease>", send_key_U_up)
    button_exit = tk.Button(text="exit", width=15, height=2, command=exit)
    button_exit.pack()


    win.mainloop()

