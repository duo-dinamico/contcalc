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
# from widgetsClass import CreateButton, CreateEntry, CreateLabel

class GeneralInfo(tk.Frame):
    '''This class will create the general info page'''
    def __init__(self, parent):
        super().__init__(parent)
        self.tab = tk.Frame(self)
        self.parent = parent
        # Labels with logo
        # gifLogo = tk.PhotoImage(file='ArupLogo.gif')
        # CreateLabel('General Info', '', gifLogo, 'white', 2, 0, 5, 'NSEW')
        
        # # Labels for column 0
        # headers_col0 = ['Job Title: ', 'Job Number: ', 'Date: ']
        # for i in range(0, len(headers_col0)):
        #     CreateLabel('General Info', headers_col0[i], '', None, i+3, 0, 1, 'W')

        # # Variables for entries
        # sv_entry1 = tk.StringVar()
        # sv_entry2 = tk.StringVar()
        # sv_entry3 = tk.StringVar()
        # sv_entry4 = tk.StringVar()
        # sv_entry5 = tk.StringVar()

        # lst_entries = [sv_entry1, sv_entry2, sv_entry3, sv_entry4, sv_entry5]
        # Menu.lst_entries = lst_entries

        # for i in range(0, 3):
        #     CreateEntry('General Info', lst_entries[i], 'white', i+3, 1, 1, 'E')

        # # Labels for column 2
        # headers_col2 = ['Designer: ', 'Revision: ']
        # for i in range(0, len(headers_col2)):
        #     CreateLabel('General Info', headers_col2[i], '', None, i+4, 2, 1, 'W')

        # # Entries for column 3
        # for i in range(3,5):
        #     CreateEntry('General Info', lst_entries[i], 'white', i+1, 3, 1, 'E')

        # # Label for bottom title
        # CreateLabel(
        #     'General Info',
        #     '''ESN Calc Sheet
        #     Containment sizing spreadsheet
        #     Revision 0.1 Feb20''',
        #     '', 'white', 7, 0, 5, 'NSEW'
        #     )
        
        # Create Sections
        # CreateLabel('General Info', 'Section Name', '', 'white', 6, 0, 1, 'NSEW')
        # CreateEntry('General Info', )
        # entry = tk.Entry(self.tabs['General Info'], textvariable=self.section_name_entry, bg='white')
    #     entry.grid(row=6, column=1, sticky='NSEW')
