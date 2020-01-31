#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
main.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

# Here we'll have all the imports necessary for tkinter
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

# Here we'll import local mods
from pageGeneral import *
from pageCalculation import *
from pageLookup import *


# Here begins the main function
def main():
    root = tk.Tk()
    root.title("Containment Calculation Sheet")
    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook
    # first page, which would get widgets gridded into it
    pageGeneral = ttk.Frame(nb)
    L1 = Label(pageGeneral, text="Job Title") .grid(row=0, column=0)
    # L1.pack(expand=1, fill="both")
    E1 = Entry(pageGeneral, bd =5) .grid(row=0, column=1)
    # E1.pack(expand=1, fill="both")

    # second page
    pageCalculation = ttk.Frame(nb)
    text = ScrolledText(pageCalculation)
    text.pack(expand=1, fill="both")

    # third page
    pageLookup = ttk.Frame(nb)

    nb.add(pageGeneral, text='General Data')
    nb.add(pageCalculation, text='Calculation')
    nb.add(pageLookup, text='Lookup Tables')

    nb.pack(expand=1, fill="both")

    root.mainloop()

# Main loop running

if __name__ == "__main__":
    main()
