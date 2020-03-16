#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
notebookClass.py v1.0
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import PhotoImage
from tabClass import MyTab
from tkinter import messagebox
from widgetsClass import CreateButton, CreateEntry, CreateLabel, CreateLabelframe
from menuClass import Menu

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
        self.create_general_tab('Main Page')

    def create_general_tab(self, title):
        """Method to create General Info tab"""
        frame = ttk.Frame(self)
        title = title
        main_dict = {title: frame}
        self.add(frame, text=title)
        self.grid(row=1, column=0)
        self.tabs_list.update(main_dict)

        self.info = CreateLabelframe(frame, text='General Info', row=1, column=0, colspan=4, sticky='NSWE', ipadx=0, ipady=0, padx=20, pady=20)
        self.cSection = CreateLabelframe(frame, text='Create New Section', row=2, column=0, colspan=4, sticky='NSWE', ipadx=0, ipady=0, padx=20, pady=20)
        """Labels with logo"""
        CreateLabel(frame, text='', image=self.gifLogo, background='white', height=200, width=1020, row=0, column=0, colspan=4, sticky='NSEW')

        """Labels for column 0"""
        CreateLabel(self.info, text='Job Title: ', image='', background=None, height=3, width=0, row=0, column=0, colspan=1, sticky='EW')
        CreateLabel(self.info, text='Job Number: ', image='', background=None, height=3, width=0, row=1, column=0, colspan=1, sticky='NSEW')
        CreateLabel(self.info, text='Date: ', image='', background=None, height=3, width=0, row=2, column=0, colspan=1, sticky='NSEW')

        self.e_job_title = CreateEntry(self.info, background='white', row=0, column=1, colspan=3, sticky='EW')
        self.e_job_number = CreateEntry(self.info, background='white', row=1, column=1, colspan=1, sticky='EW')
        self.e_date = CreateEntry(self.info, background='white', row=2, column=1, colspan=1, sticky='EW')

        """Labels for column 3"""
        CreateLabel(self.info, text='Designer: ', image='', background=None, height=3, width=0, row=1, column=2, colspan=1, sticky='NSEW')
        CreateLabel(self.info, text='Revision: ', image='', background=None, height=3, width=0, row=2, column=2, colspan=1, sticky='NSEW')

        """Entries for column 4"""
        self.e_designer = CreateEntry(self.info, background='white', row=1, column=3, colspan=1, sticky='EW')
        self.e_revision = CreateEntry(self.info, background='white', row=2, column=3, colspan=1, sticky='EW')

        self.lst_entries = [self.e_job_title.text, self.e_job_number.text, self.e_date.text, self.e_designer.text, self.e_revision.text]

        """Create Sections"""
        CreateLabel(self.cSection, text='Section Name: ', image='', background=None, height=3, width=0, row=0, column=0, colspan=1, sticky='EW')
        self.e_create_section = CreateEntry(self.cSection, background='white', row=0, column=1, colspan=2, sticky='EW')
        CreateButton(self.cSection, text='Create Section', height=1, width=0, command=self.add_sec, row=0, column=3, colspan=1, sticky='EW')
        self.e_create_section.grid_columnconfigure(1, weight=1)
        # CreateButton(self.cSection, text='Test', height=1, width=0, command=self.parent.menu.test_dic, row=0, column=4, colspan=1, sticky='EW')
        """Label for bottom title"""
        self.footer_label = tk.Label(frame, text=f'Submains Containment Calculation Sheet\n\nContainment sizing spreadsheet\n\nVersion {self.parent.contcalc_version} 2020', font=('TkFixedFont', 10), background='white', height=10)
        self.footer_label.grid(row=3, column=0, columnspan=4, sticky='NSEW')
        # CreateLabel(frame, text=f'Submains Containment Calculation Sheet\n\nContainment sizing spreadsheet\n\nVersion {self.parent.contcalc_version} 2020', image='', background='white', height=10, width=0, row=3, column=0, colspan=4, sticky='NSEW')

    def create_calc_tab(self):
        """Method to create one Calculation tab"""

        # Criar a tab e adicionar à lista de Tabs

        # Criar o objecto secção

        # Desenhar a tab, usando as variáveis da secção
        pass

    def add_sec(self):
        name = self.e_create_section.get().strip()
        for k in self.tabs_list:
            if k == name:
                messagebox.showwarning(title='Error', message='That section name already exist.')
                return
        
        if name != '':
            self.tab_create(name)
            self.e_create_section.text.set('')
        else:
            messagebox.showwarning(title='Error', message='You must insert a section name.')

    def tab_create(self, tab_name):
        new_tab = MyTab(self, tab_name)
        self.dict = {tab_name: new_tab}
        self.tabs_list.update(self.dict)
        self.select(new_tab)

        return new_tab

    def get_notebook_dict(self, with_results):
        """ Method that return a dictionary with data of the notebook. """

        ## Start dict
        result_dict = {
            'Project Info':{
                'Job Title': self.lst_entries[0].get(),
                'Job Number': self.lst_entries[1].get(),
                'Date': self.lst_entries[2].get(),
                'Designer': self.lst_entries[3].get(),
                'Revision': self.lst_entries[4].get(),
                'Software Version': self.parent.contcalc_version
            },
            'Project Tabs': []
        }

        ## Add tab dictionaries to the list
        for tab_name, tab_obj in self.tabs_list.items():
            if tab_name == 'Main Page':
                pass
            else:
                result_dict['Project Tabs'].append(tab_obj.get_tab_dict(with_results))
        print(f'NB: {result_dict}')
        return result_dict
