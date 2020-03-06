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
from tabClass import MyTab
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

    def test_dic(self):
        filepath = askopenfilename(
            filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'r') as input_file:
            data = json.load(input_file)
            print(data)
            for i, myline in zip(self.parent.nb.lst_entries, data['Project Info'].values()):
                i.set(myline)

    def open_file(self):
        """Method for opening files.
        INPUT: JSON file with entries and tabs
        OUTPUT: no output
        """
        filepath = askopenfilename(
            filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        with open(filepath, 'r') as input_file:
            data = json.load(input_file)
            for i, myline in zip(self.parent.nb.lst_entries, data[0]):
                i.set(myline.strip())
            for d in data[1]:
                new_tab = MyTab(self.parent.nb, d)
                self.dict = {d: new_tab}
                self.parent.nb.tabs_list.update(self.dict)
        self.filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {self.filename[-1]}')
        self.filemenu.entryconfigure(1, state='normal')

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        # lst_entries = []
        # lst_tabs = []
        # lst_toSave = []
        try:
            if self.filename:
                filepath = 'json/' + self.filename[-1]
                with open(filepath + '.txt', 'w') as save_file:
                    # for i in self.parent.nb.lst_entries:
                    #     lst_entries.append(str(i.get()))
                    # for k in self.parent.nb.tabs_list:
                    #     if k == 'Main Page':
                    #         pass
                    #     else:
                    #         lst_tabs.append(k)
                    json.dump(self.to_save(), save_file)
        except AttributeError:
            pass
        self.filemenu.entryconfigure(1, state='disabled')
            
    def saveas_file(self):
        """Method for saving files as.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        # lst_entries = []
        # lst_tabs = []
        # lst_toSave = []
        filepath = asksaveasfilename(
            filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
        )
        if not filepath:
            return
        if '.txt' in filepath:
            filepath = filepath.replace('.txt', '')
        with open(filepath + '.txt', 'w') as save_file:
            # for i in self.parent.nb.lst_entries:
            #     lst_entries.append(str(i.get()))
            # for k in self.parent.nb.tabs_list:
            #     if k == 'Main Page':
            #         pass
            #     else:
            #         lst_tabs.append(k)
            json.dump(self.to_save(), save_file)
        self.filename = filepath.split('/')
        self.parent.title(f'Containment Calculation Sheet - {self.filename[-1]}')
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

        # The following makes the tabs into a dictionary and adds them to the save list
        # lst_tabs = []
        # for k in self.parent.nb.tabs_list:
        #     if k == 'Main Page':
        #         pass
        #     else:
        #         lst_tabs.append(k)
        # dict_info_headers = {}
        # for h in lst_tabs:
        #     dict_info_headers.update({h: ''})
        # dict_tabs = {'Project Tabs': dict_info_headers}
        # to_save.update(dict_tabs)
        
        dict_tabs = {}
        for k, v in self.parent.nb.tabs_list.items():
            if k == 'Main Page':
                pass
            else:
                tmp_dict = {k: v.list_cables()}
                dict_tabs.update(tmp_dict)
        # print(lst_tabs)

        # dict_info_headers = {}
        # for h in lst_tabs:
        #     dict_info_headers.update({h: ''})
        # dict_tabs = {'Project Tabs': dict_info_headers}
        to_save.update(dict_tabs)

        # The following make the list of cables into a dictionary and adds them to the save list
        # lst_obj_tabs = []
        # for i in self.parent.nb.tabs_list.values():
        #     lst_obj_tabs.append(i)
        # lst_obj_tabs = lst_obj_tabs[1:]
        # lst_cables = []
        # for o in lst_obj_tabs:
        #     lst_cables.append(o.list_cables())
        # # print(lst_cables)
        # try:
        #     dict_cables_headers = {}
        #     for c in lst_cables:
        #         dict_cables_headers = {'Type': c[1], 'Number of cables': c[2], 'CSA': c[3], 'No Parallels': c[4], 'CPC CSA': c[5]}
        #         print(dict_cables_headers)
        # except IndexError:
        #     pass
        return(to_save)

    def about_menu(self):
        """Method for versions.
        INPUT: self
        OUTPUT: no output
        """
        py_version_compact = platform.python_version()
        tkinter_version = tk.TkVersion
        contcalc_version = 0.2
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
