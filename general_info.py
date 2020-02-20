#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
general_info.py v0.2
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import PhotoImage
from widgetsClass import CreateButton, CreateEntry, CreateLabel
from mywindowClass import Menu

class GeneralInfo(tk.Frame):
    '''This class will create the general info page'''
    def __init__(self, name):
        tk.Frame.__init__(self)
        self.name = name
        
        # Labels with logo
        gifLogo = tk.PhotoImage(file='ArupLogo.gif')
        CreateLabel(self, text='', image=gifLogo, background='white', height=100, width=600, row=1, column=0, colspan=5, sticky='NSEW')
        
        # Labels for column 0
        CreateLabel(self, text='Job Title: ', image='', background=None, height=2, width=0, row=2, column=0, colspan=1, sticky='W')
        CreateLabel(self, text='Job Number: ', image='', background=None, height=2, width=0, row=3, column=0, colspan=1, sticky='W')
        CreateLabel(self, text='Date: ', image='', background=None, height=2, width=0, row=4, column=0, colspan=1, sticky='W')
        
        # Variables for entries
        sv_entry1 = tk.StringVar()
        sv_entry2 = tk.StringVar()
        sv_entry3 = tk.StringVar()
        sv_entry4 = tk.StringVar()
        sv_entry5 = tk.StringVar()

        lst_entries = [sv_entry1, sv_entry2, sv_entry3, sv_entry4, sv_entry5]
        Menu.lst_entries = lst_entries

        CreateEntry(self, text=sv_entry1, background='white', row=2, column=1, colspan=1, sticky='E')
        CreateEntry(self, text=sv_entry2, background='white', row=3, column=1, colspan=1, sticky='E')
        CreateEntry(self, text=sv_entry3, background='white', row=4, column=1, colspan=1, sticky='E')
        
        # Labels for column 2
        CreateLabel(self, text='Designer: ', image='', background=None, height=2, width=0, row=3, column=2, colspan=1, sticky='W')
        CreateLabel(self, text='Revision: ', image='', background=None, height=2, width=0, row=4, column=2, colspan=1, sticky='W')
        
        # Entries for column 3
        CreateEntry(self, text=sv_entry4, background='white', row=3, column=3, colspan=1, sticky='E')
        CreateEntry(self, text=sv_entry5, background='white', row=4, column=3, colspan=1, sticky='E')
        
        # Create Sections
        CreateLabel(self, text='Section Name: ', image='', background=None, height=0, width=0, row=5, column=0, colspan=1, sticky='W')
        CreateEntry(self, text='test', background='white', row=5, column=1, colspan=1, sticky='E')
        CreateButton(self, text='Create Section', width=0, command=None, row=5, column=2, colspan=1, sticky='NSEW')
        # entry = tk.Entry(self.tabs['General Info'], textvariable=self.section_name_entry, bg='white')
        # self.add_btn = tk.Button(self.tabs['General Info'], text='Criar Nova Secção', width=12, command=self.add_sec)

        # Label for bottom title
        CreateLabel(self, text='''ESN Calc Sheet
        Containment sizing spreadsheet
        Revision 0.3 Feb20''', image='', background='white', height=5, width=0, row=6, column=0, colspan=5, sticky='NSEW')
        