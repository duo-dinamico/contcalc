#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
menuClass.py v1.0
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tabClass import MyTab, MyCable
from widgetsClass import CreateLabel, CreateEntry, CreateButton
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
        self.filemenu.add_command(label='Exit', command=parent.quit)
        self.editmenu.add_command(label='Add...', command=self.popupWindow)
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
            return
        if '.txt' not in self.filepath and self.dialog == asksaveasfilename:
            self.filepath = self.filepath + '.txt'
        else:
            pass
        with open(self.filepath, self.mode, encoding='utf-8') as json_file: # access the json file as Write or Read mode
            if self.dialog == askopenfilename: # if open file, access the file and save it on a variable
                data = json.load(json_file)
                self.filemenu.entryconfigure(1, state='normal') # set menu save to normal
            else:
                json.dump(self.to_save(), json_file, ensure_ascii=False, indent=4, separators=(',', ': ')) # otherwise just do a dump into the file
                data = '' # set data to empty just for error handling
                self.filemenu.entryconfigure(1, state='disabled') # disable the save menu
        return data # return the data to be used when opening a file

    def open_file(self):
        """Method for opening files.
        INPUT: JSON file with entries and tabs
        OUTPUT: no output
        """
        data = self.json_access('r', askopenfilename) # convert the data into a variable inside the open
        try:
            for v in self.parent.nb.tabs_list.values(): # cycle through open tabs and destroy them
                v.destroy()
            self.parent.nb.create_general_tab('Main Page') # generate a clear main page
            for i, myline in zip(self.parent.nb.lst_entries, data['Project Info'].values()): # cycle through the list of tk entries to fill them with the values from data
                i.set(myline)
            for d in data['Project Tabs']:
                new_tab = MyTab(self.parent.nb, d['Tab_name'])
                if d['Installation type'] == 'Custom Spacing':
                    new_tab.common_spacing_entry.config(state='normal')
                else:
                    pass
                new_tab.common_install_var.set(d['Installation type'])
                new_tab.common_spacing_var.set(d['Custom Spacing'])
                new_tab.common_cont_var.set(d['Containment Type'])
                new_tab.common_spare_var.set(d['Spare Capacity'])
                for z in d['Cables']:
                    cable = MyCable(z['Reference'], z['Type'], z['Number of cables'], z['CSA'], z['No Parallels'], z['CPC CSA'])
                    new_tab.cable_list.append(cable)
                    new_tab.populate_list()
                    new_tab.print_result()
                    new_tab.clear_cable()
                self.dict = {d['Tab_name']: new_tab}
                self.parent.nb.tabs_list.update(self.dict)

            self.filename_state('normal') # function to set title and save menu to enabled
        except TypeError:
            return

    def filename_state(self, state):
        self.filename = self.filepath.lower().split('/')[-1].replace('.txt', '') # clean filepath to get filename only
        self.filename = self.filename.title()
        self.parent.title(f'Containment Calculation Sheet - {self.filename}') # set the title of the window to the filename
        self.filemenu.entryconfigure(1, state=state) # set save menu to enabled

    def save_file(self):
        """Method for saving files.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        try:
            if self.filename: # if the software has a name, should be able to save it to the filepath. if not, silently pass
                self.json_access('w', '')
                self.filename_state('disabled') # function to set title and save menu to enabled
        except AttributeError:
            pass

    def saveas_file(self):
        """Method for saving files as.
        INPUT: self
        OUTPUT: JSON file with entries and tabs
        """
        self.json_access('w', asksaveasfilename)
        self.filename_state('normal') # function to set title and save menu to enabled

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

            ## Loop all calculation tabs
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

        ## Lets test

        print(self.parent.nb.get_notebook_dict(False))
        print(json.dumps(self.parent.nb.get_notebook_dict(False), indent=4, sort_keys=True, separators=(',', ': ')))

    def to_save(self):
        to_save = self.parent.nb.get_notebook_dict(False)
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

    def popupWindow(self):
        self.top = tk.Toplevel(self.parent)
        self.top.title('Section Name')
        self.top.wm_geometry('300x150')
        self.pu_frame = ttk.Frame(self.top)
        self.pu_frame.pack()
        self.pu_label = CreateLabel(self.pu_frame, text='Please enter name of section', image='', background=None, height=2, width=25, row=0, column=0, colspan=1, sticky='EW')
        self.pu_entry = CreateEntry(self.pu_frame, background='white', row=1, column=0, colspan=1, sticky='')
        CreateLabel(self.pu_frame, text='', image='', background=None, height=1, width=25, row=2, column=0, colspan=1, sticky='EW')
        self.pu_button = CreateButton(self.pu_frame, text='Confirm', height=2, width=10, command=self.cleanup, row=3, column=0, colspan=1, sticky='')

    def cleanup(self):
        self.popup_value = self.pu_entry.get()
 
        for k in self.parent.nb.tabs_list:
            if k == self.popup_value:
                messagebox.showwarning(title='Error', message='That section name already exist.')
                return
        if self.popup_value != '':
            self.parent.nb.tab_create(self.popup_value)
        else:
            return
        self.top.destroy()
