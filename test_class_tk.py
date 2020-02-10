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

class MyWindow(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title('Containment Calculation Sheet')
        self.notebook = Notebook(parent)
        self.menu(parent)
        
    def menu(self, parent):
        self.parent = parent
        file_menu = ['Open', 'Save', '', 'Exit']
        edit_menu = ['Cut', 'Copy', 'Paste']
        self.menu = tk.Menu(parent)
        self.filemenu = tk.Menu(self.menu, tearoff=0)
        self.editmenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.menu.add_cascade(label='Edit', menu=self.editmenu)
        for item in file_menu:
            if item == '':
                self.filemenu.add_separator()
            else:
                self.filemenu.add_command(label=item, command=root.quit)
        for item in edit_menu:
            if item == '':
                self.editmenu.add_separator()
            else:
                self.editmenu.add_command(label=item, command=root.quit)
        self.parent.config(menu=self.menu)


class Notebook(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.nb = ttk.Notebook(parent)
        self.nb.grid(row=1, column=0)

    def add_tab(self):
        self.tabControl = self.nb
        for title in upper_tabs:
            self.tab = tk.Frame(self.tabControl)
            self.tabControl.add(self.tab, text=title)
            tabs[title] = self.tab
            self.tabControl.grid(row=1, column=0, sticky='nswe')  

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

entry_col1 = ['Project Churchill', '200000', '2020/02/02']
for i in range(0, len(entry_col1)):
    nb.create_entry('General Info', entry_col1[i], 'white', i+3, 1, 1, 'E')

headers_col2 = ['Designer: ', 'Revision: ']
for i in range(0, len(headers_col2)):
    nb.create_label('General Info', headers_col2[i], '', None, i+4, 2, 1, 'W')

entry_col3 = ['JJ', 'P01']
for i in range(0, len(entry_col3)):
    nb.create_entry('General Info', entry_col3[i], 'white', i+4, 3, 1, 'E')

titleLabel = nb.create_label('General Info', 'ESN Calc Sheet\nContainment sizing spreadsheet\nRevision 0.1 Feb20', '', 'white', 6, 0, 5, 'NSEW')

logoLabel2 = nb.create_label('Calculation', 'pagina 2', '', 'white', 3, 0, 1, 'W')

root.mainloop()