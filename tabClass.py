#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
tabClass.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk, messagebox
from myDB import db



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
        #self.cable_cpc_var = tk.StringVar()
        self.result_var = tk.StringVar()
        self.result_with_install_var = tk.StringVar()
        self.result_with_spare_var = tk.StringVar()
        self.result_with_cont_var = tk.StringVar()

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
        self.common_parameters.grid_columnconfigure(1, minsize=150)

        # Common - Custom spacing
        self.common_spacing_label = tk.Label(self.common_parameters, text='Custom spacing (mm):')
        self.common_spacing_label.grid(row=0, column=2, sticky='W')
        self.common_spacing_entry = tk.Entry(self.common_parameters, textvariable=self.common_spacing_var, validate='focusout', validatecommand=self.print_result, state='disabled')
        self.common_spacing_var.set('0')
        #self.common_spacing_var.trace('w', self.print_result())
        self.common_spacing_entry.grid(row=0, column=3, sticky='W')

        # Common - Countainment type
        self.common_cont_label = tk.Label(self.common_parameters, text='Countainment type:')
        self.common_cont_label.grid(row=1, column=0, sticky='W')
        self.common_cont_optionmenu = tk.OptionMenu(self.common_parameters, self.common_cont_var, *self.get_cont_list(), command=self.common_cont_select)
        self.common_cont_var.set(self.get_cont_list()[0])
        self.common_cont_optionmenu.grid(row=1, column=1, sticky='WE')

        # Common - Spare capacity
        self.common_spare_label = tk.Label(self.common_parameters, text='Spare capacity (%):')
        self.common_spare_label.grid(row=2, column=0, sticky='W')
        self.common_spare_entry = tk.Entry(self.common_parameters, textvariable=self.common_spare_var, validate='focusout', validatecommand=self.print_result)
        self.common_spare_entry.grid(row=2, column=1, sticky='WE')

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
        self.cable_type_combobox.current(0)
        self.cable_type_combobox.bind('<<ComboboxSelected>>', self.cable_type_select)
        self.cable_type_combobox.grid(row=1, column=1, sticky='EW')

        # Cable - Select Core Number
        self.cable_cores_label = tk.Label(self.cable_parameters, text='Cores', width='15')
        self.cable_cores_label.grid(row=0, column=2)
        self.cable_cores_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['XLPE/SWA/PVC']), postcommand=self.get_cores_list, state='readonly')
        self.cable_cores_combobox.current(0)
        self.cable_cores_combobox.bind('<<ComboboxSelected>>', self.cable_cores_select)
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
        #self.cable_cpc_entry = tk.Entry(self.cable_parameters, textvariable=self.cable_cpc_var)
        self.cable_cpc_combobox = ttk.Combobox(self.cable_parameters, values=list(db['cables']['LSF Single']['1']), state='readonly')
        self.cable_cpc_combobox.current(0)
        self.cable_cpc_combobox.grid(row=1, column=5, sticky='EW')

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
        self.cable_list_listbox_header = tk.Label(self.cable_list_parameters, font=('TkFixedFont', 12), text='{:_^30s}|{:_^30s}|{:_^15s}|{:_^15s}|{:_^15s}|{:_^15s}|{:_^15s}'.format('Ref', 'Type', 'Num_cab', 'CSA', 'Parallel', 'CPC CSA', 'Diam'))
        self.cable_list_listbox_header.grid(row=0, column=0, sticky='W')
        self.cable_list_listbox = tk.Listbox(self.cable_list_parameters, height=10, width=130, border=0, selectmode=tk.BROWSE, font=('TkFixedFont', 12))
        self.cable_list_listbox.grid(row=1, column=0, padx=0, pady=20, sticky='EW')
        self.cable_list_listbox.bind('<<ListboxSelect>>', self.select_item)

        # Cable_List - Scrollbar
        self.cable_list_scrollbar = ttk.Scrollbar(self.cable_list_parameters)
        self.cable_list_scrollbar.grid(row=1, column=1, sticky='NS', padx=0, pady=20)
        self.cable_list_listbox.configure(yscrollcommand=self.cable_list_scrollbar.set)
        self.cable_list_scrollbar.configure(command=self.cable_list_listbox.yview)

        # Result -
        self.result_label_1 = tk.Label(self.result_parameters, text='Cable diameter raw sum:')
        self.result_label_1.grid(row=0, column=0, sticky='E')
        self.result_entry_1 = tk.Entry(self.result_parameters, textvariable=self.result_var, state='disabled')
        self.result_entry_1.grid(row=0, column=1, sticky='E')
        self.result_label_2 = tk.Label(self.result_parameters, text=f'Total diameter required for all cables:')
        self.result_label_2.grid(row=1, column=0, sticky='E')
        self.result_entry_2 = tk.Entry(self.result_parameters, textvariable=self.result_with_install_var, state='disabled')
        self.result_entry_2.grid(row=1, column=1, sticky='E')
        self.result_label_3 = tk.Label(self.result_parameters, text=f'Total diameter required for all cables, with spare capacity:')
        self.result_label_3.grid(row=2, column=0, sticky='E')
        self.result_entry_3 = tk.Entry(self.result_parameters, textvariable=self.result_with_spare_var, state='disabled')
        self.result_entry_3.grid(row=2, column=1, sticky='E')
        self.result_label_4 = tk.Label(self.result_parameters, text=f'Standard containment size required (Ladder Rack):')
        self.result_label_4.grid(row=3, column=0, sticky='E')
        self.result_entry_4 = tk.Entry(self.result_parameters, textvariable=self.result_with_cont_var, state='disabled')
        self.result_entry_4.grid(row=3, column=1, sticky='E')

        # Delete_tab button
        self.del_tab_btn = tk.Button(self, text='Delete Section', width=12, command=self.delete_this_tab)
        self.del_tab_btn.grid(row=5, column=0)


    def select_item(self, event):

        try:
            print(self.cable_list_listbox.curselection()[0])
            print(self.cable_list[self.cable_list_listbox.curselection()[0]].cable_ref)
            self.selected_item = self.cable_list[self.cable_list_listbox.curselection()[0]]

            self.cable_ref_entry.delete(0, tk.END)
            self.cable_ref_entry.insert(tk.END, self.selected_item.cable_ref)

            self.cable_type_combobox.set(self.selected_item.cable_type)
            self.cable_cores_combobox.set(self.selected_item.number_cables)
            self.cable_csa_combobox.set(self.selected_item.csa)
            self.cable_parallel_combobox.set(self.selected_item.parallel)

            self.cable_cpc_combobox.delete(0, tk.END)
            self.cable_cpc_combobox.insert(tk.END, self.selected_item.cpc_csa)
        except IndexError:
            pass


    def delete_this_tab(self):
        """Method to destroy current tab"""
        self.parent.tabs_list.pop(self.name)
        self.destroy()

        # Select back the General Info tab
        self.parent.select(self.parent.tabs_list['Main Page'])

    def add_cable(self):
        """Method to add a cable to this tab"""
        # cable = MyCable(self.cable_ref_var.get(), self.cable_type_var.get(), self.cable_cores_var.get(), self.cable_csa_combobox.get(), self.cable_parallel_var.get(), self.cable_cpc_var.get())
        if self.check_cable_entries():
            cable = MyCable(self.cable_ref_var.get(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_combobox.get())
            self.cable_list.append(cable)
            # print(cable.diam)
            self.populate_list()
            self.print_result()
            self.clear_cable()
        else:
            print('Erro.')

    def remove_cable(self):
        """Method to remove a cable in this tab"""
        self.cable_list.remove(self.selected_item)
        self.populate_list()
        self.print_result()

    def update_cable(self):
        """Method to update data of a cable in this tab"""
        self.selected_item.update_data(self.cable_ref_var.get(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_combobox.get())
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
        self.cable_list_listbox.delete(0, tk.END)
        for obj in self.cable_list:
            line = '{:_^30s}|{:_^30s}|{:_^15d}|{:_^15s}|{:_^15d}|{:_^15s}|{:_^15.2f}'.format(obj.cable_ref, obj.cable_type, int(obj.number_cables), obj.csa, int(obj.parallel), obj.cpc_csa, obj.diam)
            self.cable_list_listbox.insert(tk.END, line)

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
        result_with_install = 0
        for obj in self.cable_list:
            result += obj.diam
        self.result_var.set(result)

        ## Result with install
        if self.common_install_var.get() == 'Spaced':
            result_with_install = result * 2
        elif self.common_install_var.get() == 'Touching':
            result_with_install = result
        else:
            result_with_install = result + (len(self.cable_list)-1) * float(self.common_spacing_var.get())
            print(f'{result} + {len(self.cable_list)}-1 * {self.common_spacing_var.get()}')
        self.result_with_install_var.set(result_with_install)

        ## Result with spare
        if self.common_spare_var.get() != '':
            self.result_with_spare_var.set(float(self.result_with_install_var.get()) * (1 + int(self.common_spare_var.get())/100 ))
            print(f'With spare {self.result_with_install_var.get()} * (1 + {self.common_spare_var.get()}     {self.result_with_spare_var.get()})')
        else:
            self.result_with_spare_var.set(self.result_with_install_var.get())

        ## Result containment
        if self.common_cont_var.get() == 'Ladder Rack':
            for n in list(db['ladder'])[::-1]:
                if n > float(self.result_with_spare_var.get()):
                    self.result_with_cont_var.set(n)
                    break
        elif self.common_cont_var.get() == 'Cable Tray':
            for n in list(db['tray'])[::-1]:
                if n > float(self.result_with_spare_var.get()):
                    self.result_with_cont_var.set(n)
                    break

        return True


    def check_cable_entries(self):
        result = True
        for cable in self.cable_list:
            if self.cable_ref_var.get()==cable.cable_ref:
                print('Cable ref')
                messagebox.showwarning(title='Error', message='That cable name already exist.')
                result = False
        # self.cable_type_combobox.get()
        # self.cable_cores_combobox.get()
        # self.cable_csa_combobox.get()
        # self.cable_parallel_combobox.get()
        # if not self.cable_cpc_var.get().isdigit():
        #     print('CPC')
        #     result = False
        return result

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
        # print(self.common_install_var.get())
        if self.common_install_var.get() in ['Touching', 'Spaced'] :
            self.common_spacing_entry.config(state='disabled')
            # self.common_spacing_label.grid_forget()
        if self.common_install_var.get() == 'Custom Spacing':
            self.common_spacing_entry.config(state='normal')
            #self.common_spacing_label.grid(row=0, column=2, sticky='W')
            #self.common_spacing_entry.grid(row=0, column=3, sticky='W')
        self.print_result()

    def menu_select(self):
        """ Don't do anything"""
        pass



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
        # print(db['cables'][self.cable_type][self.number_cables][self.csa])
        overall = db['cables'][self.cable_type][self.number_cables][self.csa]
        single = db['cables']['LSF Single']['1'][self.cpc_csa]
        result = float(overall) * int(self.parallel) + float(single)
        return result

    def update_data(self, ref, typ, num, csa, par, cpc):
        self.cable_ref = ref
        self.cable_type = typ
        self.number_cables = num
        self.csa = csa
        self.parallel = par
        self.cpc_csa = cpc
        self.diam = self.cable_calc()
