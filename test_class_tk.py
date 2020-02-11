#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
test_class_tk.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename
from mywindowClass import *
from notebookClass import *

root = tk.Tk()
mw = MyWindow(root)

# Global variables to be added here
#upper_tabs = ['General Info', 'Calculation', 'Lookup']
#tabs = {}
gifLogo = tk.PhotoImage(file='ArupLogo.gif')

# Notebook and Tabs
nb = Notebook(root)
nb.add_tab()

# Labels
logoLabel = nb.create_label('General Info', '', gifLogo, 'white', 2, 0, 5, 'NSEW')

headers_col0 = ['Job Title: ', 'Job Number: ', 'Date: ']
for i in range(0, len(headers_col0)):
    nb.create_label('General Info', headers_col0[i], '', None, i+3, 0, 1, 'W')

sv_entry1 = tk.StringVar()
sv_entry2 = tk.StringVar()
sv_entry3 = tk.StringVar()

lst_entries = [sv_entry1,sv_entry2,sv_entry3]
mw.lst_entries = lst_entries
for i in range(0, len(lst_entries)):
    nb.create_entry('General Info', lst_entries[i], 'white', i+3, 1, 1, 'E')

headers_col2 = ['Designer: ', 'Revision: ']
for i in range(0, len(headers_col2)):
    nb.create_label('General Info', headers_col2[i], '', None, i+4, 2, 1, 'W')

entry_col3 = ['JJ', 'P01']
for i in range(0, len(entry_col3)):
    nb.create_entry('General Info', entry_col3[i], 'white', i+4, 3, 1, 'E')

titleLabel = nb.create_label('General Info', 'ESN Calc Sheet\nContainment sizing spreadsheet\nRevision 0.1 Feb20', '', 'white', 6, 0, 5, 'NSEW')

logoLabel2 = nb.create_label('Calculation', 'pagina 2', '', 'white', 3, 0, 1, 'W')

root.mainloop()
