#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
mywindowClass.py v0.1
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

        # Test Labelframe
        self.common_parameters = ttk.Labelframe(self, text='Common')
        self.common_parameters.grid()
        self.cable_parameters = ttk.Labelframe(self, text='Cables')
        self.cable_parameters.grid()

        self.name = name
        self.install_type_var = tk.StringVar()
        self.custom_spacing_var = tk.StringVar()
        self.cable_list = []
        self.cable_ref_var = tk.StringVar()
        self.cable_type_var = tk.StringVar()
        self.cable_cores_var = tk.StringVar()


        parent.add(self, text=self.name)
        self.tab_draw()

    def tab_draw(self):
        """Method that draw all widgets in the tab"""

        # Common - Installation type
        self.install_type_label = tk.Label(self.common_parameters, text='Installation type:')
        self.install_type_label.grid(row=0, column=0)
        self.install_type_entry = tk.Entry(self.common_parameters, textvariable=self.install_type_var)
        self.install_type_entry.grid(row=0, column=1)

        # Common - Custom spacing
        self.custom_spacing_label = tk.Label(self.common_parameters, text='Custom spacing:')
        self.custom_spacing_label.grid(row=0, column=2)
        self.custom_spacing_entry = tk.Entry(self.common_parameters, textvariable=self.custom_spacing_var)
        self.custom_spacing_entry.grid(row=0, column=3)

        # Entry for Cable ref
        self.cable_ref_label = tk.Label(self.cable_parameters, text='Ref')
        self.cable_ref_label.grid(row=0, column=0)
        self.cable_ref_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_ref_var)
        self.cable_ref_entry.grid(row=0, column=1)

        # Select cable type
        self.cable_type_label = tk.Label(self.cable_parameters, text='Type')
        self.cable_type_label.grid(row=1, column=0)
        self.cable_type_optionmenu = tk.OptionMenu(self.cable_parameters, self.cable_type_var, *self.get_type_list(), command=self.cable_type_select)
        self.cable_type_optionmenu.grid(row=1, column=1)

        # Select core Number
        self.cable_cores_label = tk.Label(self.cable_parameters, text='Cores')
        self.cable_cores_label.grid(row=2, column=0)
        self.cable_cores_optionmenu = tk.OptionMenu(self.cable_parameters, self.cable_cores_var, *self.get_cores_list(), command=self.cable_cores_select)
        self.cable_cores_optionmenu.grid(row=2, column=1)

        # Delete_tab button
        self.del_tab_btn = tk.Button(self, text='Delete Section', width=12, command=self.delete_this_tab)
        self.del_tab_btn.grid(row=5, column=0)

    def delete_this_tab(self):
        """Method to destroy current tab"""
        print(self.parent.tabs_list)
        self.parent.tabs_list.remove(self)
        print(self.parent.tabs_list)
        self.destroy()

    def add_cable(self, cable):
        """Method to add a cable to this tab"""
        self.cable_list.append(cable)

    def remove_cable(self, cable):
        """Method to remove a cable in this tab"""
        self.cable_list.remove(cable)

    def list_cables(self):
        """Method to list all cables in this tab"""
        result_list = []
        for cable in self.cable_list:
            result_list.append(cable.cable_ref)
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
        return ['1 core', '2 core', '3 core']

    def cable_type_select(self, event):
        print(self.cable_type_var.get())
    def cable_cores_select(self, event):
        print(self.cable_cores_var.get())



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
