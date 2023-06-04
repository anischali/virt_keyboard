#! /usr/bin/env python3

import tkinter as tk
import sys

with open(sys.argv[1], "w") as key:

    keymap = {
        "A":"30",
        "U":"22",
        "M":"50"
    }

    def send_key_A():
        print(keymap["A"])
        key.write(keymap["A"])
        key.flush()


    def send_key_U():
        print(keymap["U"])
        key.write(keymap["U"])
        key.flush()


    def send_key_M():
        print(keymap["M"])
        key.write(keymap["M"])
        key.flush()


    win = tk.Tk()
    win.geometry("{}x300+0-0".format(win.winfo_screenwidth()))
    win.attributes('-type', 'dock')

    buttonA = tk.Button(text="A", width=15, height=2, command=send_key_A)
    buttonA.pack()
    buttonM = tk.Button(text="M", width=15, height=2, command=send_key_M)
    buttonM.pack()
    buttonU = tk.Button(text="U", width=15, height=2, command=send_key_U)
    buttonU.pack()
    button_exit = tk.Button(text="exit", width=15, height=2, command=exit)
    button_exit.pack()


    win.mainloop()

