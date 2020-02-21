#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
mywindowClass.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import csv

class MyWindow(ttk.Frame):
    """Class that define the Frame container of the root window,
    and include:
    Icon bar
    Status
    """

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent # ver se funciona sem isto
  
    """Method that create the icon bar.

    INPUT: self
    OUTPUT: no output
    """
    def create_icon_bar(self):
        pass

    """Method that create the status bar.

    INPUT: self
    OUTPUT: no output
    """
    def create_status_bar(self):
        pass


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
        self.add_cascade(label='File', menu=self.filemenu)
        self.add_cascade(label='Edit', menu=self.editmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save as...', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=parent.quit)
        self.editmenu.add_command(label='Cut', command=parent.quit)
        self.editmenu.add_command(label='Copy', command=parent.quit)
        self.editmenu.add_command(label='Past', command=parent.quit)

    def open_file(self):
        """Method for opening files.
        INPUT: self
        OUTPUT: no output
        """
        filepath = askopenfilename(
            filetypes=[('CSV Files', '*.csv'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'r') as input_file:
            for i, myline in zip(self.lst_entries, input_file):
                i.set(myline.strip())
        filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {filename[-1]}')

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: no output
        """
        lst_toSave = []
        filepath = askopenfilename(
            filetypes=[('CSV Files', '*.csv'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'w', newline='') as save_file:
            for i in self.lst_entries:
                lst_toSave.append(str(i.get()))
            writer = csv.writer(save_file, delimiter=',')
            for row in lst_toSave:
                columns = [c.strip() for c in row.strip(', ').split(',')]
                writer.writerow(columns)
