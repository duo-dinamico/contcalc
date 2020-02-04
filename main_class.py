#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
main_class.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

# Import tkinter and tkinter modules
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import PhotoImage

# Import our own modules
import pageGeneral
import pageCalculation
import pageLookup

# Assign variables to our modules
pageG = pageGeneral
pageC = pageCalculation
pageL = pageLookup

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.title('Containment Calculation Sheet')


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
