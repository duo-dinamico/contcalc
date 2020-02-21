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
from widgetsClass import CreateButton, CreateEntry, CreateLabel
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
        self.gifLogo = tk.PhotoImage(file='ArupLogo.gif')        
        self.tabs_list = []
        self.section_name_entry = tk.StringVar()

        self.create_general_tab('General Info')

    def create_general_tab(self, title):  
        """Method to create General Info tab"""
        frame = ttk.Frame(self)
        self.add(frame, text=title) 
        self.grid(row=1, column=0)  
        self.tabs_list.append(title) 
        
        """Labels with logo"""
        CreateLabel(frame, text='', image=self.gifLogo, background='white', height=100, width=600, row=1, column=0, colspan=5, sticky='NSEW')
        
        """Labels for column 0"""
        CreateLabel(frame, text='Job Title: ', image='', background=None, height=2, width=0, row=2, column=0, colspan=1, sticky='W')
        CreateLabel(frame, text='Job Number: ', image='', background=None, height=2, width=0, row=3, column=0, colspan=1, sticky='W')
        CreateLabel(frame, text='Date: ', image='', background=None, height=2, width=0, row=4, column=0, colspan=1, sticky='W')
        
        """Variables for entries"""
        sv_entry1 = tk.StringVar()
        sv_entry2 = tk.StringVar()
        sv_entry3 = tk.StringVar()
        sv_entry4 = tk.StringVar()
        sv_entry5 = tk.StringVar()

        lst_entries = [sv_entry1, sv_entry2, sv_entry3, sv_entry4, sv_entry5]
        Menu.lst_entries = lst_entries

        CreateEntry(frame, text=sv_entry1, background='white', row=2, column=1, colspan=1, sticky='E')
        CreateEntry(frame, text=sv_entry2, background='white', row=3, column=1, colspan=1, sticky='E')
        CreateEntry(frame, text=sv_entry3, background='white', row=4, column=1, colspan=1, sticky='E')
        
        """Labels for column 2"""
        CreateLabel(frame, text='Designer: ', image='', background=None, height=2, width=0, row=3, column=2, colspan=1, sticky='W')
        CreateLabel(frame, text='Revision: ', image='', background=None, height=2, width=0, row=4, column=2, colspan=1, sticky='W')
        
        """Entries for column 3"""
        CreateEntry(frame, text=sv_entry4, background='white', row=3, column=3, colspan=1, sticky='E')
        CreateEntry(frame, text=sv_entry5, background='white', row=4, column=3, colspan=1, sticky='E')
        
        """Create Sections"""
        CreateLabel(frame, text='Section Name: ', image='', background=None, height=0, width=0, row=5, column=0, colspan=1, sticky='W')
        CreateEntry(frame, text=self.section_name_entry, background='white', row=5, column=1, colspan=1, sticky='E')
        CreateButton(frame, text='Create Section', width=0, command=self.add_sec, row=5, column=2, colspan=1, sticky='NSEW')

        """Label for bottom title"""
        CreateLabel(frame, text='''ESN Calc Sheet
        Containment sizing spreadsheet
        Revision 0.3 Feb20''', image='', background='white', height=5, width=0, row=6, column=0, colspan=5, sticky='NSEW')

    def create_calc_tab(self):
        """Method to create one Calculation tab"""

        # Criar a tab e adicionar à lista de Tabs

        # Criar o objecto secção

        # Desenhar a tab, usando as variáveis da secção
        pass
    
    def add_sec(self):
        for n in self.tabs_list:
            if n == self.section_name_entry.get():
                messagebox.showwarning(title='Error', message='That section name already exist.')
                return
        if self.section_name_entry.get() != '':
            new_tab = MyTab(self, self.section_name_entry.get())
            self.tabs_list.append(new_tab)
            self.select(new_tab)
            self.section_name_entry.set('')
        else:
            messagebox.showwarning(title='Error', message='You must insert a section name.')
