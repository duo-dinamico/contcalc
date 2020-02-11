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

class MyWindow(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title('Containment Calculation Sheet')
        self.notebook = Notebook(parent)
        self.menu(parent)
        
    def menu(self, parent):
        self.parent = parent
        self.menu = tk.Menu(parent)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Edit', menu=self.editmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=root.quit)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=root.quit)
        self.editmenu.add_command(label='Cut', command=root.quit)
        self.editmenu.add_command(label='Copy', command=root.quit)
        self.editmenu.add_command(label='Past', command=root.quit)
        self.parent.config(menu=self.menu)
    
    # Function to open file
    def open_file(self):
        filepath = askopenfilename(
            filetypes=[('Text Files', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'rt') as input_file:
            for i, myline in zip(lst_entries, input_file):
                i.set(myline)
        root.title(f'Containment Calculation Sheet - {filepath}')

class Notebook(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.nb = ttk.Notebook(parent, width=600, height=400)
        self.nb.grid(row=1, column=0)

    def add_tab(self):
        for title in upper_tabs:
            self.tab = tk.Frame(self.nb, width=600, height=400)
            self.nb.add(self.tab, text=title)
            tabs[title] = self.tab
            self.nb.grid(row=1, column=0, sticky='nswe')  

    def create_label(self, name, text, image, background, row, column, colspan, sticky):
        label = tk.Label(tabs[name], text=text, image=image, bg=background)
        label.grid(row=row, column=column, columnspan=colspan, sticky=sticky)
        return label

    def create_entry(self, name, text, background, row, column, colspan, sticky):
        entry = tk.Entry(tabs[name], textvariable=text, bg=background)
        entry.grid(row=row, column=column, columnspan=colspan, sticky=sticky)
        return entry
    

root = tk.Tk()
MyWindow(root)

# Global variables to be added here
upper_tabs = ['General Info', 'Calculation', 'Lookup']
tabs = {}
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