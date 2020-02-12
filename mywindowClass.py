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
    Menu
    Icon bar
    Status
    """

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.lst_entries = []
        self.parent = parent # ver se funciona sem isto

        self.create_menu()
        # # Menu creation
        # self.menu = tk.Menu(parent)
        # self.filemenu = tk.Menu(self.menu, tearoff=0)
        # self.editmenu = tk.Menu(self.menu, tearoff=0)
        # self.menu.add_cascade(label='File', menu=self.filemenu)
        # self.menu.add_cascade(label='Edit', menu=self.editmenu)
        # self.filemenu.add_command(label='Open', command=self.open_file)
        # self.filemenu.add_command(label='Save', command=self.save_file)
        # self.filemenu.add_separator()
        # self.filemenu.add_command(label='Exit', command=parent.quit)
        # self.editmenu.add_command(label='Cut', command=parent.quit)
        # self.editmenu.add_command(label='Copy', command=parent.quit)
        # self.editmenu.add_command(label='Past', command=parent.quit)
        # self.parent.config(menu=self.menu)




    """Method that create the menu.

    INPUT: self
    OUTPUT: no output
    """
    def create_menu(self):
        # Menu creation
        self.menu = tk.Menu()
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Edit', menu=self.editmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.parent.quit)
        self.editmenu.add_command(label='Cut', command=self.parent.quit)
        self.editmenu.add_command(label='Copy', command=self.parent.quit)
        self.editmenu.add_command(label='Past', command=self.parent.quit)
        self.parent.config(menu=self.menu)


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

    # Function to open file
    def open_file(self):
        filepath = askopenfilename(
            filetypes=[('CSV Files', '*.csv'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'rb') as input_file:
            for i, myline in zip(self.lst_entries, input_file):
                i.set(myline)
            #print(self.lst_entries, input_file)
        filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {filename[-1]}')

    # Function to open file
    def save_file(self):
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
                #print(columns)
                writer.writerow(columns)
