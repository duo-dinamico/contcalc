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
from openpyxl import Workbook

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
        self.filemenu.add_command(label='Export to Excel', command=self.export_excel)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.confirm_exit)
        self.editmenu.add_command(label='Add...', command=parent.quit)
        self.helpmenu.add_command(label='About', command=self.about_menu)

    def json_access(self, mode, dialog):
        """Method to load and dump data from a json.
        INPUT: JSON file with entries and tabs
        OUTPUT: no output
        """
        self.mode = mode # the mode will determine if we're doing Write or Read
        self.dialog = dialog # the dialog will determine if we're doing Save as Filename or Open Filename

        if self.dialog == asksaveasfilename or self.dialog == askopenfilename: # if dialog asks for dialog box, give it to the user
            self.filepath = self.dialog(
                filetypes=[('JSON File', '*.txt'), ('All files', '*.*')]
            )
            if not self.filepath:
                return
        else: # otherwise pass. save only needs the filepath
            pass
        if '.txt' not in self.filepath and self.dialog == asksaveasfilename:
            self.filepath = self.filepath + '.txt'
        else:
            pass
        with open(self.filepath, self.mode) as json_file: # access the json file as Write or Read mode
            if self.dialog == askopenfilename: # if open file, access the file and save it on a variable
                data = json.load(json_file)
                self.filemenu.entryconfigure(1, state='normal') # set menu save to normal
            else:
                json.dump(self.to_save(), json_file) # otherwise just do a dump into the file
                data = '' # set data to empty just for error handling
                self.filemenu.entryconfigure(1, state='disabled') # disable the save menu
        return data # return the data to be used when opening a file

    def open_file(self):
        """Method for opening files.
        INPUT: JSON file with entries and tabs
        OUTPUT: no output
        """
        data = self.json_access('r', askopenfilename) # convert the data into a variable inside the open
        for k, v in self.parent.nb.tabs_list.items(): # cycle through open tabs and destroy them
            if k == 'Main Page':
                pass
            else:
                v.destroy()
        for i, myline in zip(self.parent.nb.lst_entries, data['Project Info'].values()): # cycle through the list of tk entries to fill them with the values from data
            i.set(myline)
        for d in data['Project Tabs']: # cycle through the data on tabs in the file and create them
            new_tab = MyTab(self.parent.nb, d)
            self.dict = {d: new_tab}
            self.parent.nb.tabs_list.update(self.dict)
        for k, v in self.parent.nb.tabs_list.items(): # now cycle through created tabs and try to generate the  list of cables. silently exit if it doesn't find tabs.
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
                except IndexError:
                        pass
        self.filename_state_normal() # function to set title and save menu to enabled

    def filename_state_normal(self):
        self.filename = self.filepath.split('/')[-1].replace('.txt', '') # clean filepath to get filename only
        self.parent.title(f'Containment Calculation Sheet - {self.filename}') # set the title of the window to the filename
        self.filemenu.entryconfigure(1, state='normal') # set save menu to enabled

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        try:
            if self.filename: # if the software has a name, should be able to save it to the filepath. if not, silently pass
                self.json_access('w', '')
                self.filemenu.entryconfigure(1, state='disabled')
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

    def export_excel(self):
        """ Method to export data to Excel. """

        ## Create Workbook
        wb = Workbook()

        ## File to save. Need improvement
        dest_filename = 'empty_book.xlsx'

        ## Get data
        data = self.to_save()

        ## New Workbook always have one sheet, let use that one
        sheet_1 = wb.active
        sheet_1.title = 'Project Info'
        my_row = 1
        for text in list(data['Project Info']):
            sheet_1.cell(row=my_row, column=1, value=text)
            sheet_1.cell(row=my_row, column=2, value=data["Project Info"][text])
            my_row += 1
            #print(f'{x}: {data["Project Info"][x]}')

        ## Check if there are calculation tabs
        print(f'Number of tabs: {len(list(data["Project Tabs"]))}')
        if len(list(data["Project Tabs"])) > 0:

            ## Loop all tables
            for tab in list(data["Project Tabs"]):
                print(f'Tab: {tab}')
                wb.create_sheet(title=tab)

                ## Write data to the cells, from list
                my_row = 1
                for field in data["Project Tabs"][tab]:
                    print(f'Field: {field}')
                    wb[tab].cell(row=my_row, column=1, value=str(field))
                    my_row += 1

        ## Save Workbook to file
        wb.save(dest_filename)


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
            #         'Common': ['Installation type', 'Containment Type', 'Spare Capacity', 'Custom Spacing']
            #         'Reference': [['Type', 'Number of cables', 'CSA', 'No Parallels', 'CPC CSA']]
            #           }
            #     }
            # }


            ## Proposta de alteração:

            # 'Project Info':{
            #     'Job Title':'',
            #     'Job Number':'',
            #     'Designer':'',
            #     'Date':'',
            #     'Revision':''
            # },
            # 'Project Tabs':{
            #     'Tab':{
            #         'Common': {
            #             'Installation type': '',
            #             'Containment Type': '',
            #             'Spare Capacity': '',
            #             'Custom Spacing': ''
            #         },
            #         'Cables': [
            #             {
            #                 'Reference': '',
            #                 'Type': '',
            #                 'Number of cables': '',
            #                 'CSA': '',
            #                 'No Parallels': '',
            #                 'CPC CSA'
            #             },
            #             {
            #                 'Reference': '',
            #                 'Type': '',
            #                 'Number of cables': '',
            #                 'CSA': '',
            #                 'No Parallels': '',
            #                 'CPC CSA': ''
            #             }
            #         ]
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
                tmp_dict = {k: [v.common_install_var.get(), v.common_cont_var.get(), v.common_spare_var.get(), v.common_spacing_var.get()]}
                tmp_dict[k].append(v.list_cables())
                dict_cables.update(tmp_dict)
        to_save.update(dict_tabs)

        return to_save

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
