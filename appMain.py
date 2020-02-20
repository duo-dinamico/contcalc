#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
test_class_tk.py v0.2
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from mywindowClass import MyWindow, Menu
from notebookClass import Notebook
from tabClass import MyTab
from widgetsClass import CreateButton, CreateEntry, CreateLabel

# Create main window
root = tk.Tk()

# Title and Icon of the window
root.title('Containment Calculation Sheet')
root.iconbitmap('calc.ico')

# Create the main frame of the window
mw = MyWindow(root)
menu = Menu(root)
root.config(menu=menu)

# Global variables to be added here
#upper_tabs = ['General Info', 'Calculation', 'Lookup']
#tabs = {}

# Notebook and Tabs
nb = Notebook(root)

nb.create_botao()

root.mainloop()
