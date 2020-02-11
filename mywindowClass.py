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
#from tkinter import PhotoImage
from tkinter.filedialog import askopenfilename

class MyWindow(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title('Containment Calculation Sheet')
        #self.notebook = Notebook(parent)
        self.menu(parent)
        self.lst_entries = []


    def menu(self, parent):
        self.parent = parent
        self.menu = tk.Menu(parent)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Edit', menu=self.editmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=parent.quit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=parent.quit)
        self.editmenu.add_command(label='Cut', command=parent.quit)
        self.editmenu.add_command(label='Copy', command=parent.quit)
        self.editmenu.add_command(label='Past', command=parent.quit)
        self.parent.config(menu=self.menu)

    # Function to open file
    def open_file(self):
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'rt') as input_file:
            for i, myline in zip(self.lst_entries, input_file):
                i.set(myline)
        self.parent.title(f'Containment Calculation Sheet - {filepath}')
