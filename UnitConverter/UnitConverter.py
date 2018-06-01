from tkinter import *
import tkinter.ttk as ttk
from unit_converter.converter import convert, converts
import time

GUI = Tk()

baseunit = StringVar()
var = StringVar()
myParent = GUI

myContainer1 = Frame(GUI)
myContainer1.pack(expand=YES, fill = BOTH)

control_frame = Frame(myContainer1)
control_frame.pack(side = LEFT, expand = NO, padx = 10, pady = 5, ipadx = 5, ipady = 5)

demo_frame = Frame(myContainer1) 
demo_frame.pack(side=RIGHT, expand=YES, fill=BOTH)        
         
top_frame = Frame(demo_frame) 
top_frame.pack(side=TOP, expand=YES, fill=BOTH)

left_frame = Frame(top_frame, borderwidth = 5)
left_frame.pack(side = LEFT, expand = YES, fill = Y)

#dumb_frame = Frame(left_frame).pack()
   
myMessage = "Select a base measurement"
ttk.Label(control_frame, text = myMessage, justify = LEFT).pack(side = TOP, anchor = W)
s = StringVar()
result = StringVar()
def callback(event):
    result = directory.get()

def selected():
    if var.get() == baseunits[0]:
        entries = ["centimeter/sec^2", "foot/sec^2", "meter/sec^2", "millimeter/sec^2"]
        labelText = StringVar()
        labelText.set(entries[0])
        labelDir = Label(left_frame, textvariable = labelText, height = 4).pack(side = TOP)
        directory = StringVar()
        dirname = Entry(left_frame, textvariable = directory, width = 50).pack(side = TOP)
        labelText1 = StringVar()
        labelText1.set(entries[1])
        labelDir1 = Label(left_frame, textvariable = labelText1, height = 4).pack(side = TOP)
        directory1 = StringVar()
        dirname1 = Entry(left_frame, textvariable = directory1, width = 50).pack(side = TOP)
        labelText2 = StringVar()
        labelText2.set(entries[2])
        labelDir2 = Label(left_frame, textvariable = labelText2, height = 4).pack(side = TOP)
        directory2 = StringVar()
        dirname2 = Entry(left_frame, textvariable = directory2, width = 50).pack(side = TOP)
        labelText3 = StringVar()
        labelText3.set(entries[3])
        labelDir3 = Label(left_frame, textvariable = labelText3, height = 4).pack(side = TOP)
        directory3 = StringVar()
        dirname3 = Entry(left_frame, textvariable = directory3, width = 50).pack(side = TOP)
        directory.set('1')
        directory2.set(convert(s + 'cm/s^2','m/s^2'))
        directory3.set(convert(s + 'cm/s^2','mm/s^2'))
        





baseunits = ["Acceleration","Amt. of Substance","Angle","Area","Computer",
        "Concentration","Density","Distance","Energy",
    "Flow","Force","Light", "Mass", "Power","Pressure",
    "Speed","Temperature","Time","Torque","Volume"
    ]
 # radiobuttons containing different unit options
for val, baseunit in enumerate(baseunits):
    ttk.Radiobutton(control_frame, text = baseunit, variable = var, value = baseunit, command = selected).pack(anchor = W)
# created by label
createdby = Label(control_frame,text="created by Kaustubh Rane")
createdby.pack(anchor=W)

# title the GUI
GUI.title("Unit Converter")

# begin the GUI
GUI.mainloop()
