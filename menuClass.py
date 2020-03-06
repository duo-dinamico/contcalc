#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
menuClass.py v1.0
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tabClass import MyTab, MyCable
import platform
import json

class Menu(tk.Menu):
    """Class that create the menu.

    INPUT: self
    OUTPUT: no output
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # The following 14 lines of code create our menu and associate commands to the options
        self.filemenu = tk.Menu(self, tearoff=0)
        self.editmenu = tk.Menu(self, tearoff=0)
        self.helpmenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=self.filemenu)
        self.add_cascade(label='Edit', menu=self.editmenu)
        self.add_cascade(label='Help', menu=self.helpmenu)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        self.filemenu.entryconfigure(1, state='disabled')
        self.filemenu.add_command(label='Save as...', command=self.saveas_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.confirm_exit)
        self.editmenu.add_command(label='Add...', command=parent.quit)
        self.helpmenu.add_command(label='About', command=self.about_menu)

    def json_access(self, mode, dialog):
        """Method to load and get data from a json.
        INPUT: JSON file with entries and tabs
        OUTPUT: no output
        """
        self.mode = mode
        self.dialog = dialog

        if self.dialog == asksaveasfilename:
            self.filepath = self.dialog(
                filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
            )
            print(self.filepath)
            if not self.filepath:
                return
        elif self.dialog == askopenfilename:
            self.filepath = self.dialog(
                filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
            )
            print(self.filepath)
            if not self.filepath:
                return
        else:
            self.filemenu.entryconfigure(1, state='disabled')
        
        with open(self.filepath, self.mode) as json_file:
            if self.dialog == askopenfilename:
                data = json.load(json_file)
                self.filemenu.entryconfigure(1, state='normal')
            else:
                json.dump(self.to_save(), json_file)
                data = ''
                self.filemenu.entryconfigure(1, state='disabled')
        return data

    def open_file(self):
        """Method for opening files.
        INPUT: JSON file with entries and tabs
        OUTPUT: no output
        """
        data = self.json_access('r', askopenfilename)
        for k, v in self.parent.nb.tabs_list.items():
            if k == 'Main Page':
                pass
            else:
                v.destroy()
        for i, myline in zip(self.parent.nb.lst_entries, data['Project Info'].values()):
            i.set(myline)
        for d in data['Project Tabs']:
            new_tab = MyTab(self.parent.nb, d)
            self.dict = {d: new_tab}
            self.parent.nb.tabs_list.update(self.dict)
        for k, v in self.parent.nb.tabs_list.items():
            if k == 'Main Page':
                pass
            else:
                try:
                    for z in range(0, len(data['Project Tabs'][k])):
                        cable = MyCable(data['Project Tabs'][k][z][0], data['Project Tabs'][k][z][1], data['Project Tabs'][k][z][2], data['Project Tabs'][k][z][3], data['Project Tabs'][k][z][4], data['Project Tabs'][k][z][5])
                        v.cable_list.append(cable)
                        v.populate_list()
                        v.print_result()
                        v.clear_cable()
                        # print(v)
                except IndexError:
                        pass
        self.filename_state_normal()

    def filename_state_normal(self):
        self.filename = self.filepath.split('/')[-1].replace('.txt', '')
        self.parent.title(f'Containment Calculation Sheet - {self.filename}')
        self.filemenu.entryconfigure(1, state='normal')

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        try:
            if self.filename:
                self.json_access('w', '')
        except AttributeError:
            pass
               
    def saveas_file(self):
        """Method for saving files as.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        self.json_access('w', asksaveasfilename)
        self.filename = self.filepath.split('/')[-1].replace('.txt', '')
        self.parent.title(f'Containment Calculation Sheet - {self.filename}')
        self.filemenu.entryconfigure(1, state='normal')

    def to_save(self):
        to_save = {
            # 'Project Info':{
            #     'Job Title':'',
            #     'Job Number':'',
            #     'Designer':'',
            #     'Date':'',
            #     'Revision':''
            # },
            # 'Project Tabs':{
            #     'Tab':{
            #         'Reference':{
            #            'Type':'',
            #            'Number of cables':'',
            #            'CSA':'',
            #            'No Parallels':'',
            #            'CPC CSA':''
            #           }
            #     }
            # }
        }
        # The following makes the entries in the main page a dictionary and adds them to the save list
        lst_entries = []
        for i in self.parent.nb.lst_entries:
                lst_entries.append(str(i.get()))
        dict_info_headers = {'Job Title': lst_entries[0], 'Job Number': lst_entries[1], 'Designer': lst_entries[2], 'Date': lst_entries[3], 'Revision': lst_entries[4]}
        dict_info = {'Project Info': dict_info_headers}
        to_save.update(dict_info)

        # The following makes the tabs and their cables into a dictionary and adds them to the save list
        dict_cables = {}
        dict_tabs = {'Project Tabs': dict_cables}
        for k, v in self.parent.nb.tabs_list.items():
            if k == 'Main Page':
                pass
            else:
                tmp_dict = {k: v.list_cables()}
                dict_cables.update(tmp_dict)
        to_save.update(dict_tabs)

        return(to_save)

    def about_menu(self):
        """Method for versions.
        INPUT: self
        OUTPUT: no output
        """
        py_version_compact = platform.python_version()
        tkinter_version = tk.TkVersion
        contcalc_version = 0.9
        messagebox.showinfo(title='About', message=(f'This tools versions is: {contcalc_version}\nYour python version is: {py_version_compact}\nYour tkinter version is: {tkinter_version}'))

    def confirm_exit(self):
        """Method to get warning box about exiting.
        INPUT: no input
        OUTPUT: no output
        """
        self.confirm_exit_dialog = messagebox.askyesnocancel(title='Save on close', message='Do you want to save before quiting?', default=tk.messagebox.YES, icon='question')
        
        try:
            if self.confirm_exit_dialog and self.filename:
                self.save_file()
                self.parent.quit()
            elif self.confirm_exit_dialog is None:
                return
            else:
                self.parent.quit()
        except AttributeError:
            if self.confirm_exit_dialog:
                self.saveas_file()
                self.parent.quit()
            elif self.confirm_exit_dialog is None:
                return
            else:
                self.parent.quit()
