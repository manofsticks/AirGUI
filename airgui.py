#!/usr/bin/python
from Tkinter import *
import tkMessageBox
import Tkinter
import subprocess
top = Tkinter.Tk()
# Code to add widgets will go here...


#listbox
#option = Listbox(top)
#option.insert(1, "Andromedae")
#option.insert(2, "Pavonis")
#option.insert(3, "Arrakis")
#option.insert(4, "Librae")
#option.insert(5, "Sirius")

#option.pack()

v = IntVar()

Radiobutton(top, text="Andromedae", variable=v, value=1).pack(anchor=W)
Radiobutton(top, text="Pavonis", variable=v, value=2).pack(anchor=W)
Radiobutton(top, text="Arrakis", variable=v, value=3).pack(anchor=W)
Radiobutton(top, text="Librae", variable=v, value=4).pack(anchor=W)
Radiobutton(top, text="Sirius", variable=v, value=5).pack(anchor=W)

#onoff

def turnOn():
   subprocess.call(["skype"])

on = Tkinter.Button(top, text ="On", command = turnOn)

on.pack()


def turnOff():
	subprocess.call(["pidgin"])

off = Tkinter.Button(top, text="Off", command = turnOff)

off.pack()

#onButton = Tkinter.Button(top, text="On") #command = makeCommandHere
#onButton.Pack()
#offButton = Tkinter.Button(top, text="Off")
#offButton.Pack()

#end
top.mainloop()
