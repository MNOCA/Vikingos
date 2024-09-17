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

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))