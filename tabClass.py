#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
tabClass.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk



class MyTab(ttk.Frame):
    """Class for the Section calculation tabs"""

    def __init__(self, parent, name):
        ttk.Frame.__init__(self, parent)
        self.parent = parent

        # Labelframe Groups
        self.common_parameters = ttk.Labelframe(self, text='Common')
        self.common_parameters.grid(row=0, column=0, sticky='WE', padx=20, pady=20)
        self.cable_parameters = ttk.Labelframe(self, text='Cables')
        self.cable_parameters.grid(row=1, column=0, sticky='WE', padx=20, pady=20)
        self.cable_list_parameters = ttk.Labelframe(self, text='Cables List')
        self.cable_list_parameters.grid(row=2, column=0, sticky='WE', padx=20, pady=20)
        self.result_parameters = ttk.Labelframe(self, text='Results')
        self.result_parameters.grid(row=3, column=0, sticky='WE', padx=20, pady=20)

        # Object variables
        self.name = name
        self.common_install_var = tk.StringVar()
        self.common_spacing_var = tk.StringVar()
        self.common_cont_var = tk.StringVar()
        self.common_spare_var = tk.StringVar()
        self.common_trayref_var = tk.StringVar()
        self.cable_list = []
        self.cable_ref_var = tk.StringVar()
        self.cable_cpc_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Start object
        parent.add(self, text=self.name)
        self.tab_draw()

    def tab_draw(self):
        """Method that draw all widgets in the tab"""

        # Common - Installation type
        self.common_install_label = tk.Label(self.common_parameters, text='Installation type:')
        self.common_install_label.grid(row=0, column=0, sticky='W')
        self.common_install_optionmenu = tk.OptionMenu(self.common_parameters, self.common_install_var, *self.get_install_list(), command=self.common_install_select)
        self.common_install_var.set(self.get_install_list()[0])
        self.common_install_optionmenu.grid(row=0, column=1, sticky='WE')

        # Common - Custom spacing
        self.common_spacing_label = tk.Label(self.common_parameters, text='Custom spacing (mm):')
        # self.common_spacing_label.grid(row=0, column=2, sticky='W')
        self.common_spacing_entry = tk.Entry(self.common_parameters, textvariable=self.common_spacing_var)
        # self.common_spacing_entry.grid(row=0, column=3, sticky='W')

        # Common - Countainment type
        self.common_cont_label = tk.Label(self.common_parameters, text='Countainment type:')
        self.common_cont_label.grid(row=1, column=0, sticky='W')
        self.common_cont_optionmenu = tk.OptionMenu(self.common_parameters, self.common_cont_var, *self.get_cont_list(), command=self.common_cont_select)
        self.common_cont_var.set(self.get_cont_list()[0])
        self.common_cont_optionmenu.grid(row=1, column=1, sticky='WE')

        # Common - Spare capacity
        self.common_spare_label = tk.Label(self.common_parameters, text='Spare capacity (%):')
        self.common_spare_label.grid(row=2, column=0, sticky='W')
        self.common_spare_entry = tk.Entry(self.common_parameters, textvariable=self.common_spare_var)
        self.common_spare_entry.grid(row=2, column=1, sticky='W')

        # Common - Cable Tray Ref
        self.common_trayref_label = tk.Label(self.common_parameters, text='Cable Tray Ref:')
        self.common_trayref_label.grid(row=2, column=2, sticky='W')
        self.common_trayref_var.set(self.name)
        self.common_trayref_entry = tk.Entry(self.common_parameters, textvariable=self.common_trayref_var, state='disabled')
        self.common_trayref_entry.grid(row=2, column=3, sticky='W')


        # Cable - Entry for Cable ref
        self.cable_ref_label = tk.Label(self.cable_parameters, text='Ref', width='15')
        self.cable_ref_label.grid(row=0, column=0)
        self.cable_ref_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_ref_var)
        self.cable_ref_entry.grid(row=1, column=0, sticky='EW')

        # Cable - Select cable type
        self.cable_type_label = tk.Label(self.cable_parameters, text='Type', width='15')
        self.cable_type_label.grid(row=0, column=1)
        self.cable_type_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']), postcommand=self.get_type_list, state='readonly')
        self.cable_type_combobox.current(2)
        self.cable_type_combobox.bind('<<ComboboxSelected>>', self.cable_type_select)
        self.cable_type_combobox.grid(row=1, column=1, sticky='EW')

        # Cable - Select Core Number
        self.cable_cores_label = tk.Label(self.cable_parameters, text='Cores', width='15')
        self.cable_cores_label.grid(row=0, column=2)
        self.cable_cores_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['XLPE/SWA/PVC']), postcommand=self.get_cores_list, state='readonly')
        self.cable_cores_combobox.current(0)
        self.cable_cores_combobox.grid(row=1, column=2, sticky='EW')

        # Cable - Select CSA (combobox)
        self.cable_csa_label = tk.Label(self.cable_parameters, text='CSA', width='15')
        self.cable_csa_label.grid(row=0, column=3)
        self.cable_csa_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['XLPE/SWA/PVC']['1']), postcommand=self.get_csa_list, state='readonly')
        self.cable_csa_combobox.current(0)
        self.cable_csa_combobox.grid(row=1, column=3, sticky='EW')


        # Cable - Select Cables in parallel (combobox)
        self.cable_parallel_label = tk.Label(self.cable_parameters, text='Parallel', width='15')
        self.cable_parallel_label.grid(row=0, column=4)
        self.cable_parallel_combobox = ttk.Combobox(self.cable_parameters, values=[1, 2, 3, 4, 5, 6, 7, 8], postcommand=self.get_parallel_list, state='readonly')
        self.cable_parallel_combobox.current(0)
        self.cable_parallel_combobox.grid(row=1, column=4, sticky='EW')


        # Cable - Select CPC CSA
        self.cable_cpc_label = tk.Label(self.cable_parameters, text='CPC CSA', width='15')
        self.cable_cpc_label.grid(row=0, column=5)
        self.cable_cpc_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_cpc_var)
        self.cable_cpc_entry.grid(row=1, column=5, sticky='EW')

        # Cable - Buttons
        self.cable_add_btn = tk.Button(self.cable_parameters, text='Add', width=12, command=self.add_cable)
        self.cable_add_btn.grid(row=3, column=0, sticky='WE', padx=5, pady=5)

        self.cable_remove_btn = tk.Button(self.cable_parameters, text='Remove', width=12, command=self.remove_cable)
        self.cable_remove_btn.grid(row=3, column=1, sticky='WE', padx=5, pady=5)

        self.cable_update_btn = tk.Button(self.cable_parameters, text='Update', width=12, command=self.update_cable)
        self.cable_update_btn.grid(row=3, column=2, sticky='WE', padx=5, pady=5)

        self.cable_clear_btn = tk.Button(self.cable_parameters, text='Clear', width=12, command=self.clear_cable)
        self.cable_clear_btn.grid(row=3, column=3, sticky='WE', padx=5, pady=5)


        # Cable_List - List of cables
        self.cable_list_listbox = tk.Listbox(self.cable_list_parameters, height=16, width=100, border=0)
        self.cable_list_listbox.grid(row=1, column=0, rowspan=6, columnspan=4, padx=20, pady=20)
        self.cable_list_listbox.bind('<<ListboxSelect>>', self.select_item)

        # Result -
        self.result_label = tk.Label(self.result_parameters, text='Result:')
        self.result_label.grid(row=0, column=0)
        self.result_entry = tk.Entry(self.result_parameters, textvariable=self.result_var, state='disabled')
        self.result_entry.grid(row=0, column=1, sticky='E')

        # Delete_tab button
        self.del_tab_btn = tk.Button(self, text='Delete Section', width=12, command=self.delete_this_tab)
        self.del_tab_btn.grid(row=5, column=0)


    def select_item(self, event):
        print(self.cable_list_listbox.curselection()[0])
        print(self.cable_list[self.cable_list_listbox.curselection()[0]].cable_ref)
        self.selected_item = self.cable_list[self.cable_list_listbox.curselection()[0]]

        self.cable_ref_entry.delete(0, tk.END)
        self.cable_ref_entry.insert(tk.END, self.selected_item.cable_ref)

        self.cable_type_combobox.set(self.selected_item.cable_type)
        self.cable_cores_combobox.set(self.selected_item.number_cables)
        self.cable_csa_combobox.set(self.selected_item.csa)
        #self.cable_parallel_var.set(self.selected_item.parallel)
        self.cable_parallel_combobox.set(self.selected_item.parallel)

        self.cable_cpc_entry.delete(0, tk.END)
        self.cable_cpc_entry.insert(tk.END, self.selected_item.cpc_csa)


    def delete_this_tab(self):
        """Method to destroy current tab"""
        self.parent.tabs_list.pop(self.name)
        self.destroy()

        # Select back the General Info tab
        self.parent.select(self.parent.tabs_list['Main Page'])

    def add_cable(self):
        """Method to add a cable to this tab"""
        # cable = MyCable(self.cable_ref_var.get(), self.cable_type_var.get(), self.cable_cores_var.get(), self.cable_csa_combobox.get(), self.cable_parallel_var.get(), self.cable_cpc_var.get())
        cable = MyCable(self.cable_ref_var.get(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_var.get())
        self.cable_list.append(cable)
        print(cable.diam)
        self.populate_list()
        self.print_result()

    def remove_cable(self):
        """Method to remove a cable in this tab"""
        self.cable_list.remove(self.selected_item)
        self.populate_list()
        self.print_result()

    def update_cable(self):
        """Method to update data of a cable in this tab"""
        # self.selected_item.update_data(self.cable_ref_var.get(), self.cable_type_var.get(), self.cable_cores_var.get(), self.cable_csa_var.get(), self.cable_parallel_var.get(), self.cable_cpc_var.get())
        self.selected_item.update_data(self.cable_ref_var.get(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_var.get())
        self.populate_list()
        self.print_result()

    def clear_cable(self):
        """Method to clear data entries of a cable in this tab"""
        self.cable_ref_entry.delete(0, tk.END)
        self.cable_type_combobox.set(self.get_type_list()[0])
        self.cable_cores_combobox.set(self.get_cores_list()[0])
        self.cable_csa_combobox.set(self.get_csa_list()[0])
        #self.cable_parallel_var.set(self.get_parallel_list()[0])
        self.cable_parallel_combobox.set(self.get_parallel_list()[0])
        self.cable_cpc_entry.delete(0, tk.END)

    def populate_list(self):
        self.cable_list_listbox.delete(0, tk.END)
        for obj in self.list_cables():
            self.cable_list_listbox.insert(tk.END, obj)

    def list_cables(self):
        """Method to list all cables in this tab"""
        result_list = []
        for cable in self.cable_list:
            result_list.append([cable.cable_ref, cable.cable_type, cable.number_cables, cable.csa, cable.parallel, cable.cpc_csa, cable.diam])
        return result_list

    def print_result(self):
        result = 0
        for obj in self.cable_list:
            result += obj.diam
        self.result_var.set(result)
        print(result)

    def get_type_list(self):
        """Method that returns the list of all cables available"""
        self.cable_type_combobox['values'] = list(db['cables'])

    def get_cores_list(self):
        """Method that returns the list of all cores abvailable"""
        self.cable_cores_combobox['values'] = list(db['cables'][self.cable_type_combobox.get()])

    def get_csa_list(self):
        """Method that returns the list of all cores abvailable"""
        self.cable_csa_combobox['values'] = list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()])

    def get_parallel_list(self):
        """Method that returns the list of all cores abvailable"""
        #self.cable_parallel_combobox['values'] = list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()][self.cable_csa_combobox.get()])
        pass

    def get_cont_list(self):
        """Method that returns the list of containment types abvailable"""

        # Um dia vai ser aqui criada uma lista de cores de cabos,
        # mas esse dia não é hoje
        return ['Ladder Rack', 'Cable Tray']
    def get_install_list(self):
        """Method that returns the list of containment types abvailable"""

        # Um dia vai ser aqui criada uma lista de cores de cabos,
        # mas esse dia não é hoje
        return ['Spaced', 'Touching', 'Custom Spacing']

    def cable_type_select(self, event):

        # print(list(db['cables'][self.cable_type_combobox.get()]))

        #print(list(db['cables'][self.cable_type_var.get()]))

        # prepare number of cores menu
        # menu = self.cable_cores_optionmenu['menu']
        # menu.delete(0, tk.END)
        # for x in list(db['cables'][self.cable_type_var.get()]):
        #     menu.add_command(label=x, command=lambda value=x: self.cable_cores_var.set(value))
        # self.cable_cores_var.set('Select...')
        # self.cable_cores_optionmenu.children['menu'] = ['teste', 'teste2']
        pass


    def cable_cores_select(self, event):
        print('Prepare CSA menu.')
        print(list(db['cables'][self.cable_type_combobox.get()][self.cable_cores_combobox.get()]))


    def cable_csa_select(self, event):
        #print(self.cable_csa_var.get())
        pass

    def cable_parallel_select(self, event):
        #print(self.cable_parallel_var.get())
        pass
    def common_cont_select(self, event):
        #print(self.cable_parallel_var.get())
        pass

    def common_install_select(self, event):
        # print(self.common_install_var.get())
        if self.common_install_var.get() in ['Touching', 'Spaced'] :
            self.common_spacing_entry.grid_forget()
            self.common_spacing_label.grid_forget()
        if self.common_install_var.get() == 'Custom Spacing':
            self.common_spacing_label.grid(row=0, column=2, sticky='W')
            self.common_spacing_entry.grid(row=0, column=3, sticky='W')

    def menu_select(self):
        """ Don't do anything"""
        pass



class MyCable:
    """Class for the Cables in the tabs"""
    def __init__(self, ref, typ, num, csa, par, cpc):
        self.cable_ref = ref
        self.cable_type = typ
        self.number_cables = float(num)
        self.csa = float(csa)
        self.parallel = par
        self.cpc_csa = float(cpc)
        self.diam = self.cable_calc()

    def cable_calc(self):
        result = self.number_cables * self.csa * self.cpc_csa
        return result

    def update_data(self, ref, typ, num, csa, par, cpc):
        self.cable_ref = ref
        self.cable_type = typ
        self.number_cables = float(num)
        self.csa = float(csa)
        self.parallel = par
        self.cpc_csa = float(cpc)
        self.diam = self.cable_calc()


db = {'cables': {
    'XLPE/SWA/PVC': {
        '1': {
            '50': 17.5,
            '70': 20.2
        },
        '2': {
            '1.5': 12.3,
            '2.5': 13.6
        },
        '3': {
            '1.5': 12.6,
            '2.5': 14.1
        }
    },
    'XLPE/SWA/LSF': {
        '1': {
            '50': 17.5,
            '70': 20.2,
            '95': 22.3,
            '120': 24.2,
            '150': 27.4,
            '185': 30.0,
            '240': 32.8,
            '300': 35.6,
            '400': 40.4,
            '500': 44.2,
            '630': 48.8,
            '800': 55.4,
            '1000': 60.6
        },
        '2': {},
        '3': {},
        '4': {},
        '5': {}
    },
    'FP400': {

    },
    'FP600S': {

    },
    'MICC (Light Duty)': {

    },
    'MICC (Heavy Duty)': {

    },
    'LSF Single': {

    }

}
}
