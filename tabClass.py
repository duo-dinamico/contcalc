#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
tabClass.py v1.0
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk, messagebox
from myDB import db
from decimal import Decimal, getcontext


class MyTab(ttk.Frame):
    """Class for the Section calculation tabs"""

    def __init__(self, parent, name):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        # Labelframe Groups
        self.common_parameters = ttk.Labelframe(self, text='Common')
        self.common_parameters.grid(row=0, column=0, sticky='WE', padx=10, pady=10)
        self.cable_parameters = ttk.Labelframe(self, text='Cables')
        self.cable_parameters.grid(row=1, column=0, columnspan=2, sticky='WE', padx=10, pady=10)
        self.cable_list_parameters = ttk.Labelframe(self, text='Cables List')
        self.cable_list_parameters.grid(row=2, column=0, columnspan=2, sticky='WE', padx=10, pady=10)
        self.result_parameters = ttk.Labelframe(self, text='Results')
        self.result_parameters.grid(row=3, column=0, columnspan=2, sticky='WE', padx=10, pady=10)
        self.commands_parameters = ttk.Labelframe(self, text='Section Actions')
        self.commands_parameters.grid(row=0, column=1, sticky='NSWE', padx=10, pady=10)

        # Object variables
        self.name = name
        self.common_spacing_var = tk.StringVar()
        self.common_spare_var = tk.StringVar()
        self.common_trayref_var = tk.StringVar()
        self.cable_list = []
        self.cable_ref_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.result_with_install_var = tk.StringVar()
        self.result_with_spare_var = tk.StringVar()
        self.result_with_cont_var = tk.StringVar()
        self.result_with_cont_var.set('0')
        self.duplicate_var = tk.StringVar()

        ## Configure Decimal
        getcontext().prec = 4
        print(f'Precisão no cable: {getcontext()}')

        # Start object
        parent.add(self, text=self.name)
        self.tab_draw()

    def tab_draw(self):
        """Method that draw all widgets in the tab"""

        # Common - Installation type
        self.common_install_label = tk.Label(self.common_parameters, text='Installation type:')
        self.common_install_label.grid(row=0, column=0, sticky='W', pady=5)
        self.common_install_combobox = ttk.Combobox(self.common_parameters, values=['Spaced', 'Touching', 'Custom Spacing'], state='readonly')
        self.common_install_combobox.current(0)
        self.common_install_combobox.bind('<<ComboboxSelected>>', self.common_install_select)
        self.common_install_combobox.grid(row=0, column=1, sticky='WE', padx=5, pady=5)
        # self.common_parameters.grid_columnconfigure(1, minsize=150)

        # Common - Custom spacing
        self.common_spacing_label = tk.Label(self.common_parameters, text='Custom spacing (mm):')
        self.common_spacing_label.grid(row=1, column=0, sticky='W', pady=5)
        self.common_spacing_entry = tk.Entry(self.common_parameters, textvariable=self.common_spacing_var, validate='focusout', validatecommand=self.common_spacing_validate, state='disabled')
        self.common_spacing_var.set('0')
        self.common_spacing_entry.grid(row=1, column=1, sticky='WE', padx=5, pady=5)

        # Common - Countainment type
        self.common_cont_label = tk.Label(self.common_parameters, text='Containment type:')
        self.common_cont_label.grid(row=2, column=0, sticky='W', pady=5)
        self.common_cont_combobox = ttk.Combobox(self.common_parameters, values=['Ladder Rack', 'Cable Tray'], state='readonly')
        self.common_cont_combobox.current(0)
        self.common_cont_combobox.bind('<<ComboboxSelected>>', self.common_cont_select)
        self.common_cont_combobox.grid(row=2, column=1, sticky='WE', padx=5, pady=5)

        # Common - Spare capacity
        self.common_spare_label = tk.Label(self.common_parameters, text='Spare capacity (%):')
        self.common_spare_label.grid(row=3, column=0, sticky='W', pady=5)
        self.common_spare_entry = tk.Entry(self.common_parameters, textvariable=self.common_spare_var, validate='focusout', validatecommand=self.common_spare_validate)
        self.common_spare_var.set('25')
        self.common_spare_entry.grid(row=3, column=1, sticky='WE', padx=5, pady=5)

        # Cable - Entry for Cable ref
        self.cable_ref_label = tk.Label(self.cable_parameters, text='Cable Reference', width='13')
        self.cable_ref_label.grid(row=0, column=0)
        self.cable_ref_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_ref_var)
        self.cable_ref_entry.grid(row=1, column=0, sticky='EW', padx=5)

        # Cable - Select cable type
        self.cable_type_label = tk.Label(self.cable_parameters, text='Cable Type', width='13')
        self.cable_type_label.grid(row=0, column=1)
        self.cable_type_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']), postcommand=self.get_type_list, state='readonly')
        self.cable_type_combobox.current(0)
        self.cable_type_combobox.bind('<<ComboboxSelected>>', self.cable_type_select)
        self.cable_type_combobox.grid(row=1, column=1, sticky='EW', padx=5)

        # Cable - Select Core Number
        self.cable_cores_label = tk.Label(self.cable_parameters, text='No Integral Cores', width='13')
        self.cable_cores_label.grid(row=0, column=2)
        self.cable_cores_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['XLPE/SWA/PVC']), postcommand=self.get_cores_list, state='readonly')
        self.cable_cores_combobox.current(0)
        self.cable_cores_combobox.bind('<<ComboboxSelected>>', self.cable_cores_select)
        self.cable_cores_combobox.grid(row=1, column=2, sticky='EW', padx=5)

        # Cable - Select CSA (combobox)
        self.cable_csa_label = tk.Label(self.cable_parameters, text='Cable CSA (mm)', width='13')
        self.cable_csa_label.grid(row=0, column=3)
        self.cable_csa_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['XLPE/SWA/PVC']['1']), postcommand=self.get_csa_list, state='readonly')
        self.cable_csa_combobox.current(0)
        self.cable_csa_combobox.grid(row=1, column=3, sticky='EW', padx=5)

        # Cable - Select Cables in parallel (combobox)
        self.cable_parallel_label = tk.Label(self.cable_parameters, text='Cables in Parallel', width='13')
        self.cable_parallel_label.grid(row=0, column=4)
        self.cable_parallel_combobox = ttk.Combobox(self.cable_parameters, values=[1, 2, 3, 4, 5, 6, 7, 8], state='readonly')
        self.cable_parallel_combobox.current(0)
        self.cable_parallel_combobox.grid(row=1, column=4, sticky='EW', padx=5)

        # Cable - Select CPC CSA
        self.cable_cpc_label = tk.Label(self.cable_parameters, text='CPC CSA (mm)', width='13')
        self.cable_cpc_label.grid(row=0, column=5)
        #self.cable_cpc_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_cpc_var)
        self.cable_cpc_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['LSF Single']['1']), state='readonly')
        self.cable_cpc_combobox.current(0)
        self.cable_cpc_combobox.grid(row=1, column=5, sticky='EW', padx=5)

        # Cable - Buttons
        self.cable_add_btn = tk.Button(self.cable_parameters, text='Add Cable', width=13, command=self.add_cable)
        self.cable_add_btn.grid(row=3, column=0, sticky='WE', padx=5, pady=5)

        self.cable_remove_btn = tk.Button(self.cable_parameters, text='Remove Cable', width=13, command=self.remove_cable)
        self.cable_remove_btn.grid(row=3, column=1, sticky='WE', padx=5, pady=5)

        self.cable_update_btn = tk.Button(self.cable_parameters, text='Update Cable', width=13, command=self.update_cable)
        self.cable_update_btn.grid(row=3, column=2, sticky='WE', padx=5, pady=5)

        self.cable_clear_btn = tk.Button(self.cable_parameters, text='Clear Entries', width=13, command=self.clear_cable)
        self.cable_clear_btn.grid(row=3, column=3, sticky='WE', padx=5, pady=5)

        # Cable_List - List of cables
        self.cable_list_treeview = ttk.Treeview(self.cable_list_parameters, show='headings')
        self.cable_list_treeview.grid(row=1, column=0, padx=0, pady=20, sticky='EW')
        self.list_headers = ['Cable Ref.', 'Cable Type', 'No of Integral Cores', 'Cable CSA (mm)', 'No parallel cables', 'CPC CSA (mm)', 'Total diameter (mm)']
        self.cable_list_treeview['columns'] = (self.list_headers)
        c = 0
        for h in self.list_headers:
            self.cable_list_treeview.column(h, width=125, anchor='center')
            self.cable_list_treeview.heading(h, text=h)
            c += 1
        self.cable_list_treeview.bind('<<TreeviewSelect>>', self.select_item)

        # Cable_List - Scrollbar
        self.cable_list_scrollbar = ttk.Scrollbar(self.cable_list_parameters)
        self.cable_list_scrollbar.grid(row=1, column=1, sticky='NS', padx=0, pady=20)
        self.cable_list_treeview.configure(yscrollcommand=self.cable_list_scrollbar.set)
        self.cable_list_scrollbar.configure(command=self.cable_list_treeview.yview)

        # Result
        self.result_label_2 = tk.Label(self.result_parameters, text=f'Total diameter required for all cables:')
        self.result_label_2.grid(row=1, column=0, sticky='E')
        self.result_entry_2 = tk.Entry(self.result_parameters, textvariable=self.result_with_install_var, state='disabled')
        self.result_entry_2.grid(row=1, column=1, sticky='E', padx=5, pady=5)
        self.result_label_3 = tk.Label(self.result_parameters, text=f'Total diameter required for all cables, with spare capacity:')
        self.result_label_3.grid(row=2, column=0, sticky='E')
        self.result_entry_3 = tk.Entry(self.result_parameters, textvariable=self.result_with_spare_var, state='disabled')
        self.result_entry_3.grid(row=2, column=1, sticky='E', padx=5, pady=5)
        self.result_label_4 = tk.Label(self.result_parameters, text=f'Standard containment size required (Ladder Rack):')
        self.result_label_4.grid(row=3, column=0, sticky='E')
        self.result_entry_4 = tk.Entry(self.result_parameters, textvariable=self.result_with_cont_var, state='disabled')
        self.result_entry_4.grid(row=3, column=1, sticky='E', padx=5, pady=5)

        # Section Actions - Cable Tray Ref
        self.common_trayref_label = tk.Label(self.commands_parameters, text='Section/Tray Ref:')
        self.common_trayref_label.grid(row=0, column=0, sticky='W', pady=5)
        self.common_trayref_var.set(self.name)
        self.common_trayref_entry = tk.Entry(self.commands_parameters, textvariable=self.common_trayref_var, state='disabled')
        self.common_trayref_entry.grid(row=0, column=1, sticky='W', padx=5, pady=5)
        self.trayref_change_btn = tk.Button(self.commands_parameters, text='Update Section Ref', width=16, command=self.trayref_change)
        self.trayref_change_btn.grid(row=0, column=2, sticky='WE', padx=5, pady=5)
        self.trayref_confirm_btn = tk.Button(self.commands_parameters, text='Confirm', width=16, command=self.trayref_confirm)

        # Section Actions - Duplicate
        self.duplicate_label = tk.Label(self.commands_parameters, text='Duplicate Ref.:')
        self.duplicate_label.grid(row=1, column=0, sticky='W', pady=5)
        self.duplicate_entry = tk.Entry(self.commands_parameters, textvariable=self.duplicate_var)
        self.duplicate_entry.grid(row=1, column=1, padx=5, pady=5)
        self.duplicate_button = tk.Button(self.commands_parameters, text='Duplicate Section', width=16, command=self.duplicate_tab)
        self.duplicate_button.grid(row=1, column=2, pady=5)

        # Section Actions - Delete Section
        self.del_tab_btn = tk.Button(self.commands_parameters, text='Delete Section', width=16, command=lambda: self.delete_this_tab(True))
        self.del_tab_btn.grid(row=2, column=2, pady=5)

        self.print_result()

    def duplicate_tab(self):
        for k in self.parent.tabs_list:
            if k == self.duplicate_entry.get():
                messagebox.showwarning(title='Error', message='That section name already exist.')
                return
        if self.duplicate_entry.get() != '':
            new_tab = self.parent.tab_create(self.duplicate_entry.get())
            self.duplicate_var.set('')
            if self.common_install_combobox.get() == 'Custom Spacing':
                new_tab.common_spacing_entry.config(state='normal')
            else:
                pass
            new_tab.common_install_combobox.set(self.common_install_combobox.get())
            new_tab.common_spacing_var.set(self.common_spacing_var.get())
            new_tab.common_cont_combobox.set(self.common_cont_combobox.get())
            new_tab.common_spare_var.set(self.common_spare_var.get())
            for c in self.cable_list:
                cable = MyCable(c.cable_ref, c.cable_type, c.number_cables, c.csa, c.parallel, c.cpc_csa)
                new_tab.cable_list.append(cable)
                new_tab.populate_list()
                new_tab.print_result()
                new_tab.clear_cable()
        else:
            messagebox.showwarning(title='Error', message='You must insert a section name to duplicate.')

    def trayref_change(self):
        self.trayref_change_btn.grid_remove()
        self.trayref_confirm_btn.grid(row=0, column=2, sticky='WE', padx=5, pady=5)
        self.common_trayref_entry.configure(state='normal')

    def trayref_confirm(self):
        if self.common_trayref_var.get() in self.parent.tabs_list and self.common_trayref_var.get() != self.name:
            messagebox.showwarning(title='Error', message='That section name already exist.')
            return
        if self.common_trayref_var.get() != '':
            ini_list = [] # doing this list to avoid the dictionary change in order
            for k in self.parent.tabs_list.keys():
                if k == self.name:
                    ini_list.append(self.common_trayref_var.get())
                else:
                    ini_list.append(k)

            self.parent.tabs_list = dict(zip(ini_list, list(self.parent.tabs_list.values())))
            self.parent.tab('current', text=self.common_trayref_var.get())
            self.name = self.common_trayref_var.get()
            self.common_trayref_entry.configure(state='disabled')
            self.trayref_confirm_btn.grid_remove()
            self.trayref_change_btn.grid(row=2, column=4, sticky='WE', padx=5, pady=5)
        else:
            messagebox.showwarning(title='Error', message='You must insert a section name.')

    def select_item(self, event):
        try:
            self.curItem = self.cable_list_treeview.focus()
            self.selected_item = self.cable_list[self.cable_list_treeview.item(self.curItem)['text']]

            self.cable_ref_entry.delete(0, tk.END)
            self.cable_ref_entry.insert(tk.END, self.selected_item.cable_ref)

            self.cable_type_combobox.set(self.selected_item.cable_type)
            self.cable_cores_combobox.set(self.selected_item.number_cables)
            self.cable_csa_combobox.set(self.selected_item.csa)
            self.cable_parallel_combobox.set(self.selected_item.parallel)
            self.cable_cpc_combobox.set(self.selected_item.cpc_csa)

        except IndexError:
            pass

    def delete_this_tab(self, box):
        """Method to destroy current tab"""
        if box == True:
            msg_box = tk.messagebox.askyesno('Delete Tab', 'Are you sure you want to delete ' + self.name + '?')
        if box == True and msg_box or box == False:
            self.parent.tabs_list.pop(self.name)
            self.destroy()

            # Select back the General Info tab
            self.parent.select(self.parent.tabs_list['Main Page'])
        else:
            return

    def add_cable(self):
        """Method to add a cable to this tab"""
        if self.check_cable_entries():
            cable = MyCable(self.cable_ref_var.get().strip(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_combobox.get())
            self.cable_list.append(cable)
            self.populate_list()
            self.print_result()
            self.clear_cable()
        else:
            print('Erro.')

    def remove_cable(self):
        """Method to remove a cable in this tab"""
        self.cable_list.remove(self.selected_item)
        self.populate_list()
        self.clear_cable()
        self.print_result()

    def update_cable(self):
        """Method to update data of a cable in this tab"""
        self.selected_item.update_data(self.cable_ref_var.get().strip(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_combobox.get())
        self.populate_list()
        self.print_result()
        self.clear_cable()

    def clear_cable(self):
        """Method to clear data entries of a cable in this tab"""
        self.cable_ref_entry.delete(0, tk.END)
        self.cable_type_combobox.current(newindex=0)
        self.cable_cores_combobox.current(newindex=0)
        self.cable_csa_combobox.current(newindex=0)
        self.cable_parallel_combobox.current(newindex=0)
        self.cable_cpc_combobox.current(newindex=0)

    def populate_list(self):
        """ Method that update the data in the listbox."""
        self.cable_list_treeview.delete(*self.cable_list_treeview.get_children())
        c = 0
        for obj in self.cable_list:
            line = [obj.cable_ref, obj.cable_type, int(obj.number_cables), obj.csa, int(obj.parallel), obj.cpc_csa, obj.diam]
            self.cable_list_treeview.insert('', 'end', text=c, values=(line))
            c += 1

    def list_cables(self):
        """Method to list all cables in this tab"""
        result_list = []
        for cable in self.cable_list:
            result_list.append([cable.cable_ref, cable.cable_type, cable.number_cables, cable.csa, cable.parallel, cable.cpc_csa, cable.diam])
        return result_list

    def print_result(self):
        """ Method to get the multiple results to print."""
        ## Raw Result
        result = 0
        for obj in self.cable_list:
            result += obj.diam
        self.result_var.set(result)

        ## Result with install
        result_with_install = 0
        if self.common_install_combobox.get() == 'Spaced':
            result_with_install = result * 2
        elif self.common_install_combobox.get() == 'Touching':
            result_with_install = result
        elif len(self.cable_list) != 0:
            result_with_install = result + (len(self.cable_list)-1) * Decimal(self.common_spacing_var.get())
            print(f'result_with_install = {result} + {len(self.cable_list)}-1 * {self.common_spacing_var.get()}')
        self.result_with_install_var.set(str(result_with_install))

        ## Result with spare
        if self.common_spare_var.get() != '':
            self.result_with_spare_var.set( str(Decimal(self.result_with_install_var.get()) * Decimal(1 + int(self.common_spare_var.get())/100 ) ) )
            print(f'With spare {Decimal(self.result_with_install_var.get())} * (1 + {int(self.common_spare_var.get())}   ->  {self.result_with_spare_var.get()})')
        else:
            self.result_with_spare_var.set(self.result_with_install_var.get())

        ## Result containment
        ## Need to check exception because may not exist when this is called
        try:
            if self.common_cont_combobox.get() == 'Ladder Rack':
                for n in list(db['ladder'])[::-1]:
                    if n > Decimal(self.result_with_spare_var.get()):
                        self.result_with_cont_var.set(n)
                        break
                if Decimal(self.result_with_spare_var.get()) > max(db['ladder']):
                    self.result_with_cont_var.set(max(db['ladder']))
            elif self.common_cont_combobox.get() == 'Cable Tray':
                for n in list(db['tray'])[::-1]:
                    if n > Decimal(self.result_with_spare_var.get()):
                        self.result_with_cont_var.set(n)
                        break
                if Decimal(self.result_with_spare_var.get()) > max(db['tray']):
                    self.result_with_cont_var.set(max(db['tray']))
        except:
            pass
        ## Warning if total diam is higher than maximum size of Tray/Ladder
        ## Need to pass if result_entry_4 does not already exist
        try:
            if float(self.result_with_spare_var.get()) > float(self.result_with_cont_var.get()):
                self.result_entry_4.configure(disabledbackground='red')
            else:
                self.result_entry_4.configure(disabledbackground='SystemButtonFace')
        except:
            pass
        return True

    def check_cable_entries(self):
        """ Method that check if data inserted are valid."""
        if self.cable_ref_var.get().strip() == '':
            messagebox.showwarning(title='Error', message='Cable must have a reference.')
            return False
        for cable in self.cable_list:
            if self.cable_ref_var.get().strip() == cable.cable_ref:
                messagebox.showwarning(title='Error', message='That cable reference already exist.')
                return False
        return True

    def get_type_list(self):
        """Method that returns the list of all cables available"""
        self.cable_type_combobox['values'] = list(db['cables'])
        self.cable_type_combobox.current(newindex=0)

    def get_cores_list(self):
        """Method that returns the list of all cores abvailable"""
        self.cable_cores_combobox['values'] = list(db['cables'][self.cable_type_combobox.get()])
        self.cable_cores_combobox.current(newindex=0)

    def get_csa_list(self):
        """Method that returns the list of all cores abvailable"""
        self.cable_csa_combobox['values'] = list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()])
        self.cable_csa_combobox.current(newindex=0)

    def get_parallel_list(self):
        """Method that returns the list of all cores abvailable"""
        #self.cable_parallel_combobox['values'] = list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()][self.cable_csa_combobox.get()])
        pass

    def cable_type_select(self, event):
        """Method that changes current values in combobox to default"""
        self.cable_cores_combobox.set(list(db['cables'][self.cable_type_combobox.get()])[0])
        self.cable_csa_combobox.set(list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()])[0])

    def cable_cores_select(self, event):
        """Method that changes current values in combobox to default"""
        self.cable_csa_combobox.set(list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()])[0])

    def cable_csa_select(self, event):
        #print(self.cable_csa_var.get())
        pass

    def cable_parallel_select(self, event):
        #print(self.cable_parallel_var.get())
        pass

    def common_cont_select(self, event):
        self.print_result()

    def common_install_select(self, event):
        """ Called when Instalation is selectd. """
        if self.common_install_combobox.get() in ['Touching', 'Spaced'] :

            ## Enable spacing entry
            self.common_spacing_entry.config(state='disabled')

            ## Put back spacing to zero
            self.common_spacing_var.set('0')

        if self.common_install_combobox.get() == 'Custom Spacing':

            ## Disable spacing entry
            self.common_spacing_entry.config(state='normal')

        ## Refresh result table
        self.print_result()

    def common_spacing_validate(self):
        """ Method that validate if spacing is a number. """
        if self.common_spacing_var.get().isdigit():
            self.print_result()
            return True
        else:
            messagebox.showwarning(title='Error', message='Spacing must be a number.')
            self.common_spacing_entry.focus_set()
            return False

    def common_spare_validate(self):
        """ Method that validate if spare is a number. """
        ## Check if is number
        if self.common_spare_var.get().isdigit():
            self.print_result()
            return True
        else:
            messagebox.showwarning(title='Error', message='Spare must be a number.')
            self.common_spare_entry.focus_set()
            return False

    def menu_select(self):
        """ Don't do anything"""
        pass

    def get_tab_dict(self, with_results):
        """ Method that return a dictionary with data of the tab. """

        ## First values
        result_dict = {
            'Tab_name': self.name,
            'Installation type': self.common_install_combobox.get(),
            'Custom Spacing': self.common_spacing_var.get(),
            'Containment Type': self.common_cont_combobox.get(),
            'Spare Capacity': self.common_spare_var.get()
        }

        ## Create cable list
        my_list = []
        for cable in self.cable_list:
            my_list.append(cable.get_cable_dict(with_results))

        ## Add list of cables to dictionary
        result_dict.update({'Cables': my_list})

        ## Add results if with_results is True
        if with_results:
            result_dict.update({'Results': {
                                    'Total diameter': self.result_with_install_var.get(),
                                    'Total with spare': self.result_with_spare_var.get(),
                                    'Containment size': self.result_with_cont_var.get()
            }})

        return result_dict


class MyCable:
    """Class for the Cables in the tabs"""
    def __init__(self, ref, typ, num, csa, par, cpc):
        self.cable_ref = ref
        self.cable_type = typ
        self.number_cables = num
        self.csa = csa
        self.parallel = par
        self.cpc_csa = cpc
        self.diam = self.cable_calc()

    def cable_calc(self):
        overall = db['cables'][self.cable_type][self.number_cables][self.csa]
        single = db['cables']['LSF Single']['1'][self.cpc_csa]
        result = Decimal(overall) * int(self.parallel) + Decimal(single)

        ## Try setting the precision
        # getcontext().prec = 4
        print(f'Precisão no cable: {getcontext()}')
        print(f'Calculationin cable: {Decimal(overall)} * {int(self.parallel)} + {Decimal(single)}')
        return result

    def update_data(self, ref, typ, num, csa, par, cpc):
        self.cable_ref = ref
        self.cable_type = typ
        self.number_cables = num
        self.csa = csa
        self.parallel = par
        self.cpc_csa = cpc
        self.diam = self.cable_calc()

    def get_cable_dict(self, with_results):
        """ Method that return a dictionary with data of cable. """
        result_dict = {
            'Reference': self.cable_ref,
            'Type': self.cable_type,
            'Number of cables': self.number_cables,
            'CSA': self.csa,
            'No Parallels': self.parallel,
            'CPC CSA': self.cpc_csa
        }

        ## Add diameter, if with_results is True
        if with_results:
            result_dict.update({'Diameter': str(self.diam)})

        return result_dict
