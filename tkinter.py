#https://tkdocs.com/tutorial
import random
from tkinter import *
from tkinter import ttk

from vikingsClasses import Soldier, Viking, Saxon, War

#Setting up the Main Application Window
root = Tk()
root.title("Viking War")

#Creating a Content Frame
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1) #the frame should expand to fill any extra space if the window is resized
root.rowconfigure(0, weight=1) #the frame should expand to fill any extra space if the window is resized

#Creating the Entry Widget
viking_army = StringVar()
viking_army_entry = ttk.Entry(mainframe, width=7, textvariable=viking_army)
viking_army_entry.grid(column=2, row=1, sticky=(W, E))

#Creating the Remaining Widgets
meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#Adding Some Polish
for child in mainframe.winfo_children(): #Adds a little bit of padding around the widgets within the content frame
    child.grid_configure(padx=5, pady=5)
viking_army_entry.focus() #Puts the focus on the entry widget, so the cursor will start in that field
root.bind("<Return>", calculate) #If Return key is pressed (Enter), it will call calculate