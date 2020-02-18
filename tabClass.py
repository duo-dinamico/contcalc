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

        self.name = name
        self.common_install_var = tk.StringVar()
        self.common_spacing_var = tk.StringVar()
        self.common_cont_var = tk.StringVar()
        self.common_spare_var = tk.StringVar()
        self.common_trayref_var = tk.StringVar()
        self.cable_list = []
        self.cable_ref_var = tk.StringVar()
        self.cable_type_var = tk.StringVar()
        self.cable_cores_var = tk.StringVar()
        self.cable_csa_var = tk.StringVar()
        self.cable_parallel_var = tk.StringVar()
        self.cable_cpc_var = tk.StringVar()

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
        self.cable_ref_label = tk.Label(self.cable_parameters, text='Ref')
        self.cable_ref_label.grid(row=0, column=0)
        self.cable_ref_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_ref_var)
        self.cable_ref_entry.grid(row=0, column=1)

        # Cable - Select cable type
        self.cable_type_label = tk.Label(self.cable_parameters, text='Type')
        self.cable_type_label.grid(row=1, column=0)
        self.cable_type_optionmenu = tk.OptionMenu(self.cable_parameters, self.cable_type_var, *self.get_type_list(), command=self.cable_type_select)
        self.cable_type_optionmenu.grid(row=1, column=1)

        # Cable - Select core Number
        self.cable_cores_label = tk.Label(self.cable_parameters, text='Cores')
        self.cable_cores_label.grid(row=1, column=2)
        self.cable_cores_optionmenu = tk.OptionMenu(self.cable_parameters, self.cable_cores_var, *self.get_cores_list(), command=self.cable_cores_select)
        self.cable_cores_optionmenu.grid(row=1, column=3)

        # Cable - Select CSA
        self.cable_csa_label = tk.Label(self.cable_parameters, text='CSA')
        self.cable_csa_label.grid(row=1, column=4)
        self.cable_csa_optionmenu = tk.OptionMenu(self.cable_parameters, self.cable_csa_var, *self.get_csa_list(), command=self.cable_csa_select)
        self.cable_csa_optionmenu.grid(row=1, column=5)

        # Cable - Select Cables in parallel
        self.cable_parallel_label = tk.Label(self.cable_parameters, text='Parallel')
        self.cable_parallel_label.grid(row=1, column=6)
        self.cable_parallel_optionmenu = tk.OptionMenu(self.cable_parameters, self.cable_parallel_var, *self.get_parallel_list(), command=self.cable_parallel_select)
        self.cable_parallel_optionmenu.grid(row=1, column=7)

        # Cable - Select CPC CSA
        self.cable_cpc_label = tk.Label(self.cable_parameters, text='CPC CSA')
        self.cable_cpc_label.grid(row=2, column=0)
        self.cable_cpc_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_cpc_var)
        self.cable_cpc_entry.grid(row=2, column=1)

        # Cable - Buttons
        self.cable_add_btn = tk.Button(self.cable_parameters, text='Add', width=12, command=self.add_cable)
        self.cable_add_btn.grid(row=3, column=0, sticky='WE', padx=5, pady=5)

        # Cable_List - List of cables
        self.cable_list_label = tk.Label(self.cable_list_parameters, text='Cable List')
        self.cable_list_label.grid(row=0, column=0)
        self.cable_list_listbox = tk.Listbox(self.cable_list_parameters, height=16, width=100, border=0)
        self.cable_list_listbox.grid(row=1, column=0, rowspan=6, columnspan=4, padx=20)

        # Delete_tab button
        self.del_tab_btn = tk.Button(self, text='Delete Section', width=12, command=self.delete_this_tab)
        self.del_tab_btn.grid(row=5, column=0)

    def delete_this_tab(self):
        """Method to destroy current tab"""
        self.parent.tabs_list.remove(self)
        self.destroy()
        self.parent.select(self.parent.tabs['General Info'])


    def add_cable(self):
        """Method to add a cable to this tab"""
        cable = MyCable(self.cable_ref_var.get(), self.cable_type_var.get(), self.cable_cores_var.get(), self.cable_csa_var.get(), self.cable_parallel_var.get(), self.cable_cpc_var.get())
        self.cable_list.append(cable)
        print(cable.diam)
        self.populate_list()

    def remove_cable(self, cable):
        """Method to remove a cable in this tab"""
        self.cable_list.remove(cable)

    def populate_list(self):
        self.cable_list_listbox.delete(0, tk.END)
        for obj in self.list_cables():
            self.cable_list_listbox.insert(tk.END, obj)

    def list_cables(self):
        """Method to list all cables in this tab"""
        result_list = []
        for cable in self.cable_list:
            result_list.append([cable.cable_ref, cable.cable_type, cable.integral_cables, cable.csa, cable.parallel, cable.cpc_csa, cable.diam])
        result = ''
        for i in result_list:
            result += ' ' + str(i)
        #print('list_cables' + result)
        return result_list

    def get_type_list(self):
        """Method that returns the list of all cables abvailable"""

        # Um dia vai ser aqui criada uma lista de referencias de cabos,
        # mas esse dia não é hoje
        return ['Cabo A', 'Cabo B', 'Cabo C']

    def get_cores_list(self):
        """Method that returns the list of all cores abvailable"""

        # Um dia vai ser aqui criada uma lista de cores de cabos,
        # mas esse dia não é hoje
        return ['1', '2', '3']

    def get_csa_list(self):
        """Method that returns the list of all cores abvailable"""

        # Um dia vai ser aqui criada uma lista de cores de cabos,
        # mas esse dia não é hoje
        return ['240', '120', '35']

    def get_parallel_list(self):
        """Method that returns the list of all cores abvailable"""

        # Um dia vai ser aqui criada uma lista de cores de cabos,
        # mas esse dia não é hoje
        return ['1', '2', '3']

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
        #print(self.cable_type_var.get())
        pass

    def cable_cores_select(self, event):
        #print(self.cable_cores_var.get())
        pass

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
        print(self.common_install_var.get())
        if self.common_install_var.get() in ['Touching', 'Spaced'] :
            self.common_spacing_entry.grid_forget()
            self.common_spacing_label.grid_forget()
        if self.common_install_var.get() == 'Custom Spacing':
            self.common_spacing_label.grid(row=0, column=2, sticky='W')
            self.common_spacing_entry.grid(row=0, column=3, sticky='W')
        #pass



class MyCable:
    """Class for the Cables in the tabs"""
    def __init__(self, ref, typ, num, csa, par, cpc):
        self.cable_ref = ref
        self.cable_type = typ
        self.integral_cables = float(num)
        self.csa = float(csa)
        self.parallel = par
        self.cpc_csa = cpc
        self.diam = self.cable_calc()

    def cable_calc(self):
        result = self.integral_cables * self.csa
        return result

    def get_list(self):
        return ['teste', 'aaaa', 'bbb']
