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
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title('Containment Calculation Sheet')
        #self.notebook = Notebook(parent)
        self.lst_entries = []
        self.parent = parent

        # Menu creation
        self.menu = tk.Menu(parent)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Edit', menu=self.editmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=parent.quit)
        self.editmenu.add_command(label='Cut', command=parent.quit)
        self.editmenu.add_command(label='Copy', command=parent.quit)
        self.editmenu.add_command(label='Past', command=parent.quit)
        self.parent.config(menu=self.menu)

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
            print(self.lst_entries, input_file)
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
                print(columns)
                writer.writerow(columns)

