#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
menuClass.py v1.0
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import platform
import json

class Menu(tk.Menu):
    """Class that create the menu.

    INPUT: self
    OUTPUT: no output
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        self.filemenu = tk.Menu(self, tearoff=0)
        self.editmenu = tk.Menu(self, tearoff=0)
        self.helpmenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=self.filemenu)
        self.add_cascade(label='Edit', menu=self.editmenu)
        self.add_cascade(label='Help', menu=self.helpmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save as...', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=parent.quit)
        self.editmenu.add_command(label='Cut', command=parent.quit)
        self.editmenu.add_command(label='Copy', command=parent.quit)
        self.editmenu.add_command(label='Past', command=parent.quit)
        self.helpmenu.add_command(label='About', command=self.about_menu)

    def open_file(self):
        """Method for opening files.
        INPUT: self
        OUTPUT: no output
        """
        filepath = askopenfilename(
            filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'r') as input_file:
            data = json.load(input_file)
            for i, myline in zip(self.lst_entries, data):
                i.set(myline.strip())
        filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {filename[-1]}')

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: no output
        """
        lst_toSave = []
        filepath = asksaveasfilename(
            filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'w') as save_file:
            for i in self.lst_entries:
                lst_toSave.append(str(i.get()))
            json.dump(lst_toSave, save_file)

    def about_menu(self):
        """Method for versions.
        INPUT: self
        OUTPUT: no output
        """
        py_version_compact = platform.python_version()
        tkinter_version = tk.TkVersion
        contcalc_version = 0.2
        messagebox.showinfo(title='About', message=(f'This tools versions is: {contcalc_version}\nYour python version is: {py_version_compact}\nYour tkinter version is: {tkinter_version}'))
