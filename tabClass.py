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
from decimal import Decimal, getcontext


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
        self.result_var = tk.StringVar()
        self.result_with_install_var = tk.StringVar()
        self.result_with_spare_var = tk.StringVar()
        self.result_with_cont_var = tk.StringVar()
        self.result_with_cont_var.set('0')

        ## Configure Decimal
        print(getcontext())
        getcontext().prec = 4

        # Start object
        parent.add(self, text=self.name)
        self.tab_draw()

    def tab_draw(self):
        """Method that draw all widgets in the tab"""

        # Common - Installation type
        self.common_install_label = tk.Label(self.common_parameters, text='Installation type:')
        self.common_install_label.grid(row=0, column=0, sticky='W')
        self.common_install_optionmenu = tk.OptionMenu(self.common_parameters, self.common_install_var, *['Spaced', 'Touching', 'Custom Spacing'], command=self.common_install_select)
        self.common_install_var.set('Spaced')
        self.common_install_optionmenu.grid(row=0, column=1, sticky='WE')
        self.common_parameters.grid_columnconfigure(1, minsize=150)

        # Common - Custom spacing
        self.common_spacing_label = tk.Label(self.common_parameters, text='Custom spacing (mm):')
        self.common_spacing_label.grid(row=0, column=2, sticky='W')
        self.common_spacing_entry = tk.Entry(self.common_parameters, textvariable=self.common_spacing_var, validate='focusout', validatecommand=self.common_spacing_validate, state='disabled')
        self.common_spacing_var.set('0')
        #self.common_spacing_var.trace('w', self.print_result())
        self.common_spacing_entry.grid(row=0, column=3, sticky='W')

        # Common - Countainment type
        self.common_cont_label = tk.Label(self.common_parameters, text='Containment type:')
        self.common_cont_label.grid(row=1, column=0, sticky='W')
        self.common_cont_optionmenu = tk.OptionMenu(self.common_parameters, self.common_cont_var, *['Ladder Rack', 'Cable Tray'], command=self.common_cont_select)
        self.common_cont_var.set('Ladder Rack')
        # print(f'Draw: {self.get_cont_list()}')
        self.common_cont_optionmenu.grid(row=1, column=1, sticky='WE')

        # Common - Spare capacity
        self.common_spare_label = tk.Label(self.common_parameters, text='Spare capacity (%):')
        self.common_spare_label.grid(row=2, column=0, sticky='W')
        self.common_spare_entry = tk.Entry(self.common_parameters, textvariable=self.common_spare_var, validate='focusout', validatecommand=self.common_spare_validate)
        self.common_spare_var.set('25')
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
        self.cable_parallel_combobox = ttk.Combobox(self.cable_parameters, values=[1, 2, 3, 4, 5, 6, 7, 8], state='readonly')
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

        self.print_result()


    def select_item(self, event):
        try:
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
        msgbox = tk.messagebox.askyesno('Delete Tab', 'Are you sure you want to delete ' + self.name + '?')
        if msgbox:
            self.parent.tabs_list.pop(self.name)
            self.destroy()

            # Select back the General Info tab
            self.parent.select(self.parent.tabs_list['Main Page'])
        else:
            return

    def add_cable(self):
        """Method to add a cable to this tab"""
        if self.check_cable_entries():
            cable = MyCable(self.cable_ref_var.get(), self.cable_type_combobox.get(), self.cable_cores_combobox.get(), self.cable_csa_combobox.get(), self.cable_parallel_combobox.get(), self.cable_cpc_combobox.get())
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
        """ Method that update the data in the listbox."""
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
        for obj in self.cable_list:
            result += obj.diam
        self.result_var.set(result)

        ## Result with install
        result_with_install = 0
        if self.common_install_var.get() == 'Spaced':
            result_with_install = result * 2
        elif self.common_install_var.get() == 'Touching':
            result_with_install = result
        else:
            result_with_install = result + (len(self.cable_list)-1) * Decimal(self.common_spacing_var.get())
            print(f'result_with_install = {result} + {len(self.cable_list)}-1 * {self.common_spacing_var.get()}')
        self.result_with_install_var.set(result_with_install)

        ## Result with spare
        if self.common_spare_var.get() != '':
            self.result_with_spare_var.set(Decimal(self.result_with_install_var.get()) * Decimal(1 + int(self.common_spare_var.get())/100 ))
            print(f'With spare {Decimal(self.result_with_install_var.get())} * (1 + {int(self.common_spare_var.get())}   ->  {self.result_with_spare_var.get()})')
        else:
            self.result_with_spare_var.set(self.result_with_install_var.get())

        ## Result containment
        if self.common_cont_var.get() == 'Ladder Rack':
            for n in list(db['ladder'])[::-1]:
                if n > Decimal(self.result_with_spare_var.get()):
                    self.result_with_cont_var.set(n)
                    break
        elif self.common_cont_var.get() == 'Cable Tray':
            for n in list(db['tray'])[::-1]:
                if n > Decimal(self.result_with_spare_var.get()):
                    self.result_with_cont_var.set(n)
                    break

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
        result = True
        for cable in self.cable_list:
            if self.cable_ref_var.get()==cable.cable_ref:
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
        if self.common_install_var.get() in ['Touching', 'Spaced'] :
            self.common_spacing_entry.config(state='disabled')
        if self.common_install_var.get() == 'Custom Spacing':
            self.common_spacing_entry.config(state='normal')
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
            'Installation type': self.common_install_var.get(),
            'Custom Spacing': self.common_spacing_var.get(),
            'Containment Type': self.common_cont_var.get(),
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
            pass

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
        print(f'{Decimal(overall)} * {int(self.parallel)} + {Decimal(single)}')
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
            result_dict.update({'Diameter': self.diam})

        return result_dict
