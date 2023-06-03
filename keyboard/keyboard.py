#! /usr/bin/env python3

import tkinter as tk
import sys

sysfs = None

if len(sys.argv) > 2:
    sysfs = open(sys.argv[1], "w")

keymap = {
    "A":30,
    "U":22,
    "M":50
}

def send_key_A():
    print(keymap["A"])
    sysfs.write(keymap["A"])

def send_key_U():
    print(keymap["U"])
    sysfs.write(keymap["U"])

def send_key_M():
    print(keymap["M"])
    sysfs.write(keymap["M"])


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

if sysfs != None:
    sysfs.close()