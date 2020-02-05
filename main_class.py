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
import pageGeneral
import pageCalculation
import pageLookup
from pageLookup import ccsDatabase

# Assign variables to our modules
pageG = pageGeneral
pageC = pageCalculation
pageL = pageLookup


class MainApplication:
    def __init__(self, parent):
        parent.title('Containment Calculation Sheet')
        self.nb = ttk.Notebook(parent)
        self.nb.grid(row=0, column=0)

        #
        self.page1 = ttk.Frame(self.nb)
        self.nb.add(self.page1, text='General Information')
        self.gifLogo = tk.PhotoImage(file='ArupLogo.gif')
        self.logoLabel = tk.Label(self.page1, image=self.gifLogo, bg='white').grid(row=0, column=0, columnspan=5, sticky='NSWE')
        self.jobTitleLabel1 = tk.Label(self.page1, text='Job Title').grid(row=1, column=0, columnspan=2, sticky='W')
        self.jobTitleLabel2 = tk.Label(self.page1, text='Project Churchill', bg='white').grid(row=1, column=2, columnspan=3, sticky='W')
        self.jobNumberLabel1 = tk.Label(self.page1, text='Job Number').grid(row=2, column=0, sticky='W')
        self.jobNumberLabel2 = tk.Label(self.page1, text='200000', bg='white').grid(row=2, column=1, sticky='E')
        self.refLabel1 = tk.Label(self.page1, text='Reference').grid(row=2, column=2, sticky='W')
        self.refLabel2 = tk.Label(self.page1, text='A', bg='white').grid(row=2, column=3, sticky='E')
        self.dateLabel1 = tk.Label(self.page1, text='Date').grid(row=3, column=0, sticky='W')
        self.dateLabel2 = tk.Label(self.page1, text='2020/02/02', bg='white').grid(row=3, column=1, sticky='E')
        self.designerLabel1 = tk.Label(self.page1, text='Designer').grid(row=3, column=2, sticky='W')
        self.designerLabel2 = tk.Label(self.page1, text='JJ', bg='white').grid(row=3, column=3, sticky='E')
        self.revLabel1 = tk.Label(self.page1, text='Revision').grid(row=4, column=0, sticky='W')
        self.revLabel2 = tk.Label(self.page1, text='P01', bg='white').grid(row=4, column=1, sticky='E')
        self.titleLabel = tk.Label(self.page1, text='ESN Calc Sheet\nContainment sizing spreadsheet\nRevision 0.1 Feb20', justify='center').grid(row=5, column=0, columnspan=5, sticky='NSWE')

        # Page 2 for Calculation information
        self.page2 = ttk.Frame(self.nb)
        self.nb.add(self.page2, text='Calculation')
        self.variable = tk.StringVar(parent)
        self.variable.set("Touching")
        self.titleLabel = tk.Label(self.page2, text='Sub-mains cable containment calculation').grid(row=0, column=0)

        self.installationLabel = tk.Label(self.page2, text='Installation type').grid(row=1, column=0)
        self.variableDrop1 = tk.StringVar(parent)
        self.variableDrop1.set("Touching")
        self.variableDrop1.trace("w", self.select_drop1)
        self.installationDrop = tk.OptionMenu(self.page2, self.variableDrop1, "Touching", "Spaced", "Custom Spacing").grid(row=1, column=1)

        # self.button_set_drop1 = tk.Button(self.page2, text="Set", command=self.set_drop1).grid(row=1, column=2)

        self.customLabel = tk.Label(self.page2, text='Custom spacing').grid(row=1, column=3)
        self.text_customEntry = tk.StringVar(parent)
        self.customEntry = tk.Entry(self.page2, textvariable=self.text_customEntry, bg='white')
        #self.customEntry.grid(row=1, column=4)


        self.containmentLabel = tk.Label(self.page2, text='Containment type').grid(row=2, column=0)
        self.variableDrop2 = tk.StringVar(parent)
        self.variableDrop2.set("Cable Tray")
        self.containmentDrop = tk.OptionMenu(self.page2, self.variableDrop2, *db.get_cable_list())
        self.containmentDrop.grid(row=2, column=1)

        self.spareLabel = tk.Label(self.page2, text='Spare Capacity').grid(row=3, column=0)
        self.spareEntry = tk.Entry(self.page2, text='25%', bg='white').grid(row=3, column=1)

        self.trayRefLabel = tk.Label(self.page2, text='Cable Tray Reference').grid(row=3, column=3)
        self.trayRefEntry = tk.Entry(self.page2, text='C1', bg='white').grid(row=3, column=4)



        # Page 3 for look up tables
        self.page3 = ttk.Frame(self.nb)
        self.nb.add(self.page3, text='LookUp Tables')
        self.L_Cabe = tk.Label(self.page3, text=pageL.pageL_Cables(), bg='white').grid(row=0, column=1)
        self.L_Tray = tk.Label(self.page3, text=pageL.pageL_Tray(), bg='white').grid(row=0, column=5)
        self.L_Ladder = tk.Label(self.page3, text=pageL.pageL_Ladder(), bg='white').grid(row=0, column=6)


    def get_list_header(self):
        self.listHeader = ['Cable Ref.', 'Cable Type', 'No. of Integral', 'Cable CSA (mm)', 'No. of cables in parallel', 'CPC CSA (mm)', 'Total Diameter']
        for i in range(0, 7):
        	tk.Label(self.page2, text=self.listHeader[i], bg='white').grid(row=4, column=i, padx=5)


    def create_lines(self):
        self.vDrop3 = tk.StringVar()
        self.vDrop3.set(db.get_cable_list()[0])
        self.reference = tk.Entry(self.page2, bg='white').grid(row=5, column=0)
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
        self.parallel = tk.Entry(self.page2, bg='white').grid(row=5, column=4)
        self.cpc_csa = tk.Entry(self.page2, bg='white').grid(row=5, column=5)

        self.list_of_cables = tk.Listbox(self.page2, width=150)
        self.list_of_cables.grid(row=6, column=0, columnspan=6)

        self.add_cable = tk.Button(self.page2, text='Add cable')
        self.add_cable.grid(row=7, column=0)
        self.remove_cable = tk.Button(self.page2, text='Remove cable')
        self.remove_cable.grid(row=7, column=1)
        self.update_cable = tk.Button(self.page2, text='Update cable')
        self.update_cable.grid(row=7, column=2)

    def config_window(self):
        # Configure rows and columns dinamically
        for i in range(int(self.page1.grid_size()[1])):
        	self.page1.rowconfigure(i, minsize=50, weight=1)
        for i in range(int(self.page1.grid_size()[0])):
        	self.page1.columnconfigure(i, minsize=25, weight=1)

        for i in range(int(self.page2.grid_size()[1])):
        	self.page2.rowconfigure(i, minsize=50, weight=1)
        for i in range(int(self.page2.grid_size()[0])):
        	self.page2.columnconfigure(i, minsize=25, weight=1)

    def select_drop1(self, *args):
        self.customEntry.delete(0, tk.END)
        if self.variableDrop1.get() in ['Touching', 'Spaced'] :
            self.customEntry.grid_forget()
        else:
            self.customEntry.grid(row=1, column=4)
            self.customEntry.insert(tk.END, self.variableDrop1.get())


def main():
    global db
    db = ccsDatabase('database.db')
    root = tk.Tk()
    app = MainApplication(root)
    app.config_window()
    app.get_list_header()
    app.create_lines()
    root.mainloop()


if __name__ == "__main__":
    main()
