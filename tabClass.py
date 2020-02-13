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

        self.name = name
        self.cable_list = []

        parent.add(self, text=self.name)
        self.tab_draw()

    def tab_draw(self):
        """Method that draw all widgets in the tab"""

        # Delete_tab button
        self.del_tab_btn = tk.Button(self, text='Delete Section', width=12, command=self.delete_this_tab)
        self.del_tab_btn.grid()

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
