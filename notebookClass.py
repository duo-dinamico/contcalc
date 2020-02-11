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

class Notebook(ttk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.nb = ttk.Notebook(parent, width=600, height=400)
        self.nb.grid(row=1, column=0)
        self.upper_tabs = ['General Info', 'Calculation', 'Lookup']
        self.tabs = {}

    def add_tab(self):
        for title in self.upper_tabs:
            self.tab = tk.Frame(self.nb, width=600, height=400)
            self.nb.add(self.tab, text=title)
            self.tabs[title] = self.tab
            self.nb.grid(row=1, column=0, sticky='nswe')

    def create_label(self, name, text, image, background, row, column, colspan, sticky):
        label = tk.Label(self.tabs[name], text=text, image=image, bg=background)
        label.grid(row=row, column=column, columnspan=colspan, sticky=sticky)
        return label

    def create_entry(self, name, text, background, row, column, colspan, sticky):
        entry = tk.Entry(self.tabs[name], textvariable=text, bg=background)
        entry.grid(row=row, column=column, columnspan=colspan, sticky=sticky)
        return entry
