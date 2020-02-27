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
from widgetsClass import CreateButton, CreateEntry, CreateLabel, CreateLabelframe
from mywindowClass import Menu

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
        self.parent = parent
        self.gifLogo = tk.PhotoImage(file='images/Arup_logo.gif')        
        self.tabs_list = {}
        self.section_name_entry = tk.StringVar()
        """Variables for entries"""
        self.sv_entry1 = tk.StringVar()
        self.sv_entry2 = tk.StringVar()
        self.sv_entry3 = tk.StringVar()
        self.sv_entry4 = tk.StringVar()
        self.sv_entry5 = tk.StringVar()
        self.lst_entries = [self.sv_entry1, self.sv_entry2, self.sv_entry3, self.sv_entry4, self.sv_entry5]
        Menu.lst_entries = self.lst_entries
        self.create_general_tab('Main Page')

    def create_general_tab(self, title):  
        """Method to create General Info tab"""
        frame = ttk.Frame(self)
        self.title = title
        self.dict = {self.title: self}
        self.add(frame, text=self.title) 
        self.grid(row=1, column=0)  
        self.tabs_list.update(self.dict)

        self.info = CreateLabelframe(frame, text='General Info', row=1, column=0, colspan=5, sticky='NSWE', ipadx=0, ipady=0, padx=20, pady=20)
        self.cSection = CreateLabelframe(frame, text='Create New Section', row=2, column=0, colspan=5, sticky='NSWE', ipadx=0, ipady=0, padx=20, pady=20)    
        """Labels with logo"""
        CreateLabel(frame, text='', image=self.gifLogo, background='white', height=300, width=750, row=0, column=0, colspan=5, sticky='NSEW')
        
        """Labels for column 0"""
        CreateLabel(self.info, text='Job Title: ', image='', background=None, height=3, width=0, row=0, column=0, colspan=1, sticky='W')
        CreateLabel(self.info, text='Job Number: ', image='', background=None, height=3, width=0, row=1, column=0, colspan=1, sticky='W')
        CreateLabel(self.info, text='Date: ', image='', background=None, height=3, width=0, row=2, column=0, colspan=1, sticky='W')
                
        CreateEntry(self.info, text=self.sv_entry1, background='white', row=0, column=1, colspan=1, sticky='E')
        CreateEntry(self.info, text=self.sv_entry2, background='white', row=1, column=1, colspan=1, sticky='E')
        CreateEntry(self.info, text=self.sv_entry3, background='white', row=2, column=1, colspan=1, sticky='E')
        
        """Labels for column 3"""
        CreateLabel(self.info, text='Designer: ', image='', background=None, height=3, width=0, row=1, column=3, colspan=1, sticky='W')
        CreateLabel(self.info, text='Revision: ', image='', background=None, height=3, width=0, row=2, column=3, colspan=1, sticky='W')
        
        """Entries for column 4"""
        CreateEntry(self.info, text=self.sv_entry4, background='white', row=1, column=4, colspan=1, sticky='E')
        CreateEntry(self.info, text=self.sv_entry5, background='white', row=2, column=4, colspan=1, sticky='E')
        
        """Create Sections"""
        CreateLabel(self.cSection, text='Section Name: ', image='', background=None, height=3, width=0, row=0, column=0, colspan=1, sticky='W')
        CreateEntry(self.cSection, text=self.section_name_entry, background='white', row=0, column=1, colspan=1, sticky='E')
        CreateButton(self.cSection, text='Create Section', height=1, width=0, command=self.add_sec, row=0, column=2, colspan=1, sticky='')

        """Label for bottom title"""
        CreateLabel(frame, text='''ESN Calc Sheet\n\nContainment sizing spreadsheet\n\nRevision 0.3 Feb20''', image='', background='white', height=10, width=0, row=3, column=0, colspan=5, sticky='NSEW')

    def create_calc_tab(self):
        """Method to create one Calculation tab"""

        # Criar a tab e adicionar à lista de Tabs

        # Criar o objecto secção

        # Desenhar a tab, usando as variáveis da secção
        pass
    
    def add_sec(self):
        for k in self.tabs_list.items():
            if k == self.section_name_entry.get():
                messagebox.showwarning(title='Error', message='That section name already exist.')
                return
        if self.section_name_entry.get() != '':
            new_tab = MyTab(self, self.section_name_entry.get())
            self.dict = {self.section_name_entry.get(): new_tab}
            self.tabs_list.update(self.dict)
            self.select(new_tab)
            self.section_name_entry.set('')
        else:
            messagebox.showwarning(title='Error', message='You must insert a section name.')
