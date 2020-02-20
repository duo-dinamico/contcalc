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
from tabClass import MyTab
from tkinter import messagebox
from general_info import GeneralInfo


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
        ttk.Notebook.__init__(self)
        self.nb = ttk.Notebook(parent)
        self.grid(row=1, column=0)
        self.upper_tabs = ['General Info', 'Calculation', 'Lookup']
        self.tabs = {}
        self.create_general_tab()
        self.parent = parent

        # List of the current tab objects
        self.tabs_list = []

        self.section_name_entry = tk.StringVar()

    def create_general_tab(self):
        """Method to create the General tab"""
        tab1 = GeneralInfo(self)
        self.add(tab1, text='General Info')

    def create_calc_tab(self):
        """Method to create one Calculation tab"""

        # Criar a tab e adicionar à lista de Tabs

        # Criar o objecto secção

        # Desenhar a tab, usando as variáveis da secção
        pass
    
    def create_botao(self):
        pass
        # self.add_btn = tk.Button(self.tabs['General Info'], text='Criar Nova Secção', width=12, command=self.add_sec)

    def add_sec(self):
        for n in self.tabs_list:
            if n.name == self.section_name_entry.get():
                messagebox.showwarning(title='No name', message='That section name already exist.')
                return
        if self.section_name_entry.get() != '':
            new_tab = MyTab(self, self.section_name_entry.get())
            self.tabs_list.append(new_tab)
            self.select(new_tab)
            self.section_name_entry.set('')
        else:
            messagebox.showwarning(title='No name', message='You must insert a section name.')


        #self.tab1 = tk.Frame(self.nb)
        #self.nb.add(self.tab1, text='Teste')
