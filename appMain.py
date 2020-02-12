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
from tkinter.filedialog import askopenfilename
from mywindowClass import MyWindow
from notebookClass import Notebook

root = tk.Tk()
mw = MyWindow(root)

# Global variables to be added here
#upper_tabs = ['General Info', 'Calculation', 'Lookup']
#tabs = {}
gifLogo = tk.PhotoImage(file='ArupLogo.gif')

# Notebook and Tabs
nb = Notebook(root)
nb.add_tab()

# Labels with logo
logoLabel = nb.create_label(
    'General Info', '', gifLogo, 'white', 2, 0, 5, 'NSEW')

# Labels for column 0
headers_col0 = ['Job Title: ', 'Job Number: ', 'Date: ']
for i in range(0, len(headers_col0)):
    nb.create_label(
        'General Info', headers_col0[i], '', None, i+3, 0, 1, 'W'
        )

# Variables for entries
sv_entry1 = tk.StringVar()
sv_entry2 = tk.StringVar()
sv_entry3 = tk.StringVar()
sv_entry4 = tk.StringVar()
sv_entry5 = tk.StringVar()

lst_entries = [sv_entry1, sv_entry2, sv_entry3, sv_entry4, sv_entry5]
mw.lst_entries = lst_entries

for i in range(0, 3):
    nb.create_entry('General Info', lst_entries[i], 'white', i+3, 1, 1, 'E')

# Labels for column 2
headers_col2 = ['Designer: ', 'Revision: ']
for i in range(0, len(headers_col2)):
    nb.create_label(
        'General Info', headers_col2[i], '', None, i+4, 2, 1, 'W'
        )

# Entries for column 3
for i in range(3,5):
    nb.create_entry('General Info', lst_entries[i], 'white', i+1, 3, 1, 'E')

# Label for bottom title
titleLabel = nb.create_label(
    'General Info',
    '''ESN Calc Sheet
    Containment sizing spreadsheet
    Revision 0.1 Feb20''',
    '', 'white', 7, 0, 5, 'NSEW'
    )

nb.create_botao()

root.mainloop()
