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
from tabClass import MyTab
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
            for i, myline in zip(self.parent.nb.lst_entries, data[0]):
                i.set(myline.strip())
            for d in data[1]:
                new_tab = MyTab(self.parent.nb, d)
                self.dict = {d: new_tab}
                self.parent.nb.tabs_list.update(self.dict)
        filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {filename[-1]}')

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: no output
        """
        lst_entries = []
        lst_tabs = []
        lst_toSave = [lst_entries, lst_tabs]
        filepath = asksaveasfilename(
            filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        if '.txt' in filepath:
            filepath = filepath.replace('.txt', '')
        with open(filepath + '.txt', 'w') as save_file:
            for i in self.parent.nb.lst_entries:
                lst_entries.append(str(i.get()))
            for k in self.parent.nb.tabs_list:
                if k == 'Main Page':
                    pass
                else:
                    lst_tabs.append(k)
            json.dump(lst_toSave, save_file)
        filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {filename[-1]}')

    def about_menu(self):
        """Method for versions.
        INPUT: self
        OUTPUT: no output
        """
        py_version_compact = platform.python_version()
        tkinter_version = tk.TkVersion
        contcalc_version = 0.2
        messagebox.showinfo(title='About', message=(f'This tools versions is: {contcalc_version}\nYour python version is: {py_version_compact}\nYour tkinter version is: {tkinter_version}'))
