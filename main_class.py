#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
main_class.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

# Import tkinter and tkinter modules
from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import PhotoImage

# Import our own modules
import pageCalculation
import pageLookup
from pageLookup import ccsDatabase
from sectionClass import sectionClass
from sectionClass import cableClass

# Assign variables to our modules
pageC = pageCalculation
pageL = pageLookup

# Global variables to be added here
db = ccsDatabase('database.db')


class MainApplication:
    def __init__(self, parent):
        parent.title('Containment Calculation Sheet')
        self.nb = ttk.Notebook(parent)
        self.nb.grid(row=0, column=0)

        # Page 1 || General Information
        self.page1 = ttk.Frame(self.nb)
        self.nb.add(self.page1, text='General Information')

        self.gifLogo = tk.PhotoImage(file='ArupLogo.gif')
        self.logoLabel = tk.Label(self.page1, image=self.gifLogo, bg='white')
        self.logoLabel.grid(row=0, column=0, columnspan=5, sticky='NSWE')

        self.headers_col0 = ['Job Title :', 'Job Number :', 'Date :', 'Revision :']
        for i in range(0, len(self.headers_col0)):
            tk.Label(self.page1, text=self.headers_col0[i]).grid(row=i+1, column=0, sticky='W')

        self.entry_col1 = ['Project Churchill', '200000', '2020/02/02', 'P01']
        for i in range(0, len(self.entry_col1)):
            tk.Entry(self.page1, textvariable=self.entry_col1[i], bg='white').grid(row=i+1, column=1, sticky='E')

        self.headers_col2 = ['Containment Reference :', 'Designer :']
        for i in range(0, len(self.headers_col2)):
            tk.Label(self.page1, text=self.headers_col2[i]).grid(row=i+2, column=2, sticky='W')

        self.entry_col3 = ['C01', 'JJ']
        for i in range(0, len(self.entry_col3)):
            self.entry_col3[i] = tk.StringVar()
            tk.Entry(self.page1, textvariable=self.entry_col3[i], bg='white').grid(row=i+2, column=3, sticky='E')

        self.titleLabel = tk.Label(self.page1, text='ESN Calc Sheet\nContainment sizing spreadsheet\nRevision 0.1 Feb20', justify='center', bg='white')
        self.titleLabel.grid(row=5, column=0, columnspan=5, sticky='NSWE')


        # Para apagar
        self.add_btn = tk.Button(self.page1, text='Criar Secção', width=12, command=self.add_sec)
        self.add_btn.grid()

        # Page 2 for Calculation information
        self.page2 = ttk.Frame(self.nb)
        self.nb.add(self.page2, text='Calculation')

        self.variable = tk.StringVar(parent)
        self.variable.set("Touching")
        self.titleLabel = tk.Label(self.page2, text='Sub-mains cable containment calculation')
        self.titleLabel.grid(row=0, column=0)

        self.installationLabel = tk.Label(self.page2, text='Installation type')
        self.installationLabel.grid(row=1, column=0)
        self.variableDrop1 = tk.StringVar(parent)
        self.variableDrop1.set("Touching")
        self.variableDrop1.trace("w", self.select_drop1)
        self.installationDrop = tk.OptionMenu(self.page2, self.variableDrop1, "Touching", "Spaced", "Custom Spacing")
        self.installationDrop.grid(row=1, column=1)

        # self.button_set_drop1 = tk.Button(self.page2, text="Set", command=self.set_drop1).grid(row=1, column=2)

        self.customLabel = tk.Label(self.page2, text='Custom spacing')
        self.customLabel.grid(row=1, column=3)
        self.text_customEntry = tk.StringVar(parent)
        self.customEntry = tk.Entry(self.page2, textvariable=self.text_customEntry, bg='white')
        #self.customEntry.grid(row=1, column=4)


        self.containmentLabel = tk.Label(self.page2, text='Containment type')
        self.containmentLabel.grid(row=2, column=0)
        self.variableDrop2 = tk.StringVar(parent)
        self.variableDrop2.set("Cable Tray")
        self.containmentDrop = tk.OptionMenu(self.page2, self.variableDrop2, *db.get_cable_list())
        self.containmentDrop.grid(row=2, column=1)

        self.spareLabel = tk.Label(self.page2, text='Spare Capacity')
        self.spareLabel.grid(row=3, column=0)
        self.spareEntry = tk.Entry(self.page2, text='25%', bg='white')
        self.spareEntry.grid(row=3, column=1)

        self.trayRefLabel = tk.Label(self.page2, text='Cable Tray Reference')
        self.trayRefLabel.grid(row=3, column=3)
        self.trayRefEntry = tk.Entry(self.page2, text='C1', bg='white')
        self.trayRefEntry.grid(row=3, column=4)



        # Page 3 for look up tables
        self.page3 = ttk.Frame(self.nb)
        self.nb.add(self.page3, text='LookUp Tables')
        self.L_Cabe = tk.Label(self.page3, text=pageL.pageL_Cables(), bg='white')
        self.L_Cabe.grid(row=0, column=1)
        self.L_Tray = tk.Label(self.page3, text=pageL.pageL_Tray(), bg='white')
        self.L_Tray.grid(row=0, column=5)
        self.L_Ladder = tk.Label(self.page3, text=pageL.pageL_Ladder(), bg='white')
        self.L_Ladder.grid(row=0, column=6)


    def get_list_header(self):
        self.listHeader = ['Cable\nRef.', 'Cable\nType', 'No. of\nIntegral', 'Cable CSA\n(mm)', 'No. of cables\nin parallel', 'CPC CSA\n(mm)', 'Total\nDiameter']
        for i in range(0, 7):
        	tk.Label(self.page2, text=self.listHeader[i], bg='white').grid(row=4, column=i)


    def create_lines(self):
        self.vDrop3 = tk.StringVar()
        self.vDrop3.set(db.get_cable_list()[0])
        self.v = tk.StringVar()
        self.reference = tk.Entry(self.page2, textvariable=self.v, bg='white')
        self.reference.grid(row=5, column=0)
        self.cable_type = tk.OptionMenu(self.page2, self.vDrop3, *db.get_cable_list())
        self.cable_type.grid(row=5, column=1)
        self.vDrop4 = tk.StringVar()
        self.vDrop4.set(db.get_core_list()[0])
        self.integral_number = tk.OptionMenu(self.page2, self.vDrop4, *db.get_core_list())
        self.integral_number.grid(row=5, column=2)
        self.vDrop5 = tk.StringVar()
        self.vDrop5.set(db.get_csa_list()[0])
        self.integral_number = tk.OptionMenu(self.page2, self.vDrop5, *db.get_csa_list())
        self.integral_number.grid(row=5, column=3)
        self.parallel = tk.Entry(self.page2, bg='white')
        self.parallel.grid(row=5, column=4)
        self.cpc_csa = tk.Entry(self.page2, bg='white')
        self.cpc_csa.grid(row=5, column=5)

        self.list_of_cables = tk.Listbox(self.page2, width=100)
        self.list_of_cables.grid(row=6, column=0, columnspan=6)

        self.add_cable = tk.Button(self.page2, text='Add cable', command=self.add_cable)
        self.add_cable.grid(row=7, column=0)
        self.remove_cable = tk.Button(self.page2, text='Remove cable')
        self.remove_cable.grid(row=7, column=1)
        self.update_cable = tk.Button(self.page2, text='Update cable')
        self.update_cable.grid(row=7, column=2)

    def add_cable(self):
        self.list_of_cables.insert('end', self.v.get())

    # Configure rows and columns dinamically
    def config_window(self):
        for i in range(int(self.page1.grid_size()[1])):
        	self.page1.rowconfigure(i, minsize=10, weight=1)
        for i in range(int(self.page1.grid_size()[0])):
        	self.page1.columnconfigure(i, minsize=10, weight=1)

        for i in range(int(self.page2.grid_size()[1])):
        	self.page2.rowconfigure(i, minsize=10, weight=1)
        for i in range(int(self.page2.grid_size()[0])):
        	self.page2.columnconfigure(i, minsize=10, weight=1)

    def select_drop1(self, *args):
        self.customEntry.delete(0, tk.END)
        if self.variableDrop1.get() in ['Touching', 'Spaced'] :
            self.customEntry.grid_forget()
        else:
            self.customEntry.grid(row=1, column=4)
            self.customEntry.insert(tk.END, self.variableDrop1.get())

    def add_tab(self, sec, title, text):
        frame = ttk.Frame(self.nb)
        self.nb.add(frame,text=title)
        label = ttk.Label(frame,text=text)
        label.grid()
        label1 = ttk.Label(frame,text=sec.list_cables())
        label1.grid()
        self.nb.grid()

    def add_sec(self):
        sec = sectionClass(self.entry_col3[0].get())
        C1 = cableClass('ref', 'typ', '1', '2', '3', '4')
        C2 = cableClass('C2', 'XLE', '5', '2', '2', '4')
        sec.add_cable(C1)
        sec.add_cable(C2)
        self.add_tab(sec, sec.name, 'Aqui vai ser a secção '+sec.name)


def main():
    root = tk.Tk()
    app = MainApplication(root)
    app.config_window()
    app.get_list_header()
    app.create_lines()

    if False:
        sec = sectionClass('S1')
        C1 = cableClass('ref', 'typ', '1', '2', '3', '4')
        C2 = cableClass('C2', 'XLE', '5', '2', '2', '4')
        sec.add_cable(C1)
        sec.add_cable(C2)
        app.add_tab(sec, sec.name, 'Aqui vai ser a secção '+sec.name)

    root.mainloop()


if __name__ == "__main__":
    main()
