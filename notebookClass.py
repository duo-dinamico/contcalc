#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
notebookClass.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
#from tkinter.filedialog import askopenfilename
from tabClass import MyTab


class Notebook(ttk.Notebook):
    """Class that define the Notebook that will contain all the tabs."""

    def __init__(self, parent):
        """
        Parameters of this class:
        nb: Notebook object
        upper_tabs: List of names of tabs
        tabs: Dict of tabs
        section_name_entry: var of the entry for name of section
        """

        ttk.Notebook.__init__(self, parent)
        #self.nb = ttk.Notebook(parent, width=600, height=400)
        self.grid(row=1, column=0)
        self.upper_tabs = ['General Info', 'Calculation', 'Lookup']
        self.tabs = {}

        # List of the current tab objects
        self.tabs_list = []

        self.section_name_entry = tk.StringVar()



    def create_general_tab():
        """Method to create the General tab"""
        pass

    def create_calc_tab():
        """Method to create one Calculation tab"""

        # Criar a tab e adicionar à lista de Tabs

        # Criar o objecto secção

        # Desenhar a tab, usando as variáveis da secção
        pass

    def add_tab(self):
        for title in self.upper_tabs:
            self.tab = tk.Frame(self, width=600, height=400)
            self.add(self.tab, text=title)
            self.tabs[title] = self.tab
            self.grid(row=1, column=0, sticky='nswe')

    def create_label(self, name, text, image, background, row, column, colspan, sticky):
        label = tk.Label(self.tabs[name], text=text, image=image, bg=background)
        label.grid(row=row, column=column, columnspan=colspan, sticky=sticky)
        return label

    def create_entry(self, name, text, background, row, column, colspan, sticky):
        entry = tk.Entry(self.tabs[name], textvariable=text, bg=background)
        entry.grid(row=row, column=column, columnspan=colspan, sticky=sticky)
        return entry

    def create_botao(self):

        label = tk.Label(self.tabs['General Info'], text='Section Name', bg='white')
        label.grid(row=6, column=0, columnspan=1, sticky='NSEW')

        entry = tk.Entry(self.tabs['General Info'], textvariable=self.section_name_entry, bg='white')
        entry.grid(row=6, column=1, sticky='NSEW')

        self.add_btn = tk.Button(self.tabs['General Info'], text='Criar Nova Secção', width=12, command=self.add_sec)
        self.add_btn.grid(row=6, column=2, columnspan=2, sticky='NSEW')



    def add_sec(self):
        exist = False
        for n in self.tabs_list:
            if n.name == self.section_name_entry.get():
                exist = True
        if self.section_name_entry.get() != '' and exist==False:
            new_tab = MyTab(self, self.section_name_entry.get())
            self.tabs_list.append(new_tab)
            self.select(new_tab)
            self.section_name_entry.set('')

        #self.tab1 = tk.Frame(self.nb)
        #self.nb.add(self.tab1, text='Teste')
