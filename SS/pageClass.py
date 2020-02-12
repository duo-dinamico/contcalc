from tkinter import ttk
import tkinter as tk
class calcPage:
    def __init__(self, parent, db):

        self.page = ttk.Frame(parent.nb)
        parent.nb.add(self.page, text='NNNNNNNNNNNNNNNNNNNNNNNN')

        self.variable = tk.StringVar()
        self.variable.set("Touching")
        self.titleLabel = tk.Label(self.page, text='Sub-mains cable containment calculation')
        self.titleLabel.grid(row=0, column=0)

        self.installationLabel = tk.Label(self.page, text='Installation type')
        self.installationLabel.grid(row=1, column=0)
        self.variableDrop1 = tk.StringVar()
        self.variableDrop1.set("Touching")
        self.variableDrop1.trace("w", self.select_drop1)
        self.installationDrop = tk.OptionMenu(self.page, self.variableDrop1, "Touching", "Spaced", "Custom Spacing")
        self.installationDrop.grid(row=1, column=1)

        # self.button_set_drop1 = tk.Button(self.page2, text="Set", command=self.set_drop1).grid(row=1, column=2)

        self.customLabel = tk.Label(self.page, text='Custom spacing')
        self.customLabel.grid(row=1, column=3)
        self.text_customEntry = tk.StringVar()
        self.customEntry = tk.Entry(self.page, textvariable=self.text_customEntry, bg='white')
        #self.customEntry.grid(row=1, column=4)


        self.containmentLabel = tk.Label(self.page, text='Containment type')
        self.containmentLabel.grid(row=2, column=0)
        self.variableDrop2 = tk.StringVar()
        self.variableDrop2.set("Cable Tray")
        self.containmentDrop = tk.OptionMenu(self.page, self.variableDrop2, *db.get_cable_list())
        self.containmentDrop.grid(row=2, column=1)

        self.spareLabel = tk.Label(self.page, text='Spare Capacity')
        self.spareLabel.grid(row=3, column=0)
        self.spareEntry = tk.Entry(self.page, text='25%', bg='white')
        self.spareEntry.grid(row=3, column=1)

        self.trayRefLabel = tk.Label(self.page, text='Cable Tray Reference')
        self.trayRefLabel.grid(row=3, column=3)
        self.trayRefEntry = tk.Entry(self.page, text='C1', bg='white')
        self.trayRefEntry.grid(row=3, column=4)

        self.listHeader = ['Cable\nRef.', 'Cable\nType', 'No. of\nIntegral', 'Cable CSA\n(mm)', 'No. of cables\nin parallel', 'CPC CSA\n(mm)', 'Total\nDiameter']
        for i in range(0, 7):
        	tk.Label(self.page, text=self.listHeader[i], bg='white').grid(row=4, column=i)

        self.create_lines(db)

    def select_drop1(self, *args):
        self.customEntry.delete(0, tk.END)
        if self.variableDrop1.get() in ['Touching', 'Spaced'] :
            self.customEntry.grid_forget()
        else:
            self.customEntry.grid(row=1, column=4)
            self.customEntry.insert(tk.END, self.variableDrop1.get())

    def create_lines(self, db):
        self.vDrop3 = tk.StringVar()
        self.vDrop3.set(db.get_cable_list()[0])
        self.v = tk.StringVar()
        self.reference = tk.Entry(self.page, textvariable=self.v, bg='white')
        self.reference.grid(row=5, column=0)
        self.cable_type = tk.OptionMenu(self.page, self.vDrop3, *db.get_cable_list())
        self.cable_type.grid(row=5, column=1)
        self.vDrop4 = tk.StringVar()
        self.vDrop4.set(db.get_core_list()[0])
        self.integral_number = tk.OptionMenu(self.page, self.vDrop4, *db.get_core_list())
        self.integral_number.grid(row=5, column=2)
        self.vDrop5 = tk.StringVar()
        self.vDrop5.set(db.get_csa_list()[0])
        self.integral_number = tk.OptionMenu(self.page, self.vDrop5, *db.get_csa_list())
        self.integral_number.grid(row=5, column=3)
        self.parallel = tk.Entry(self.page, bg='white')
        self.parallel.grid(row=5, column=4)
        self.cpc_csa = tk.Entry(self.page, bg='white')
        self.cpc_csa.grid(row=5, column=5)

        self.list_of_cables = tk.Listbox(self.page, width=100)
        self.list_of_cables.grid(row=6, column=0, columnspan=6)

        self.add_cable = tk.Button(self.page, text='Add cable', command=self.add_cable)
        self.add_cable.grid(row=7, column=0)
        self.remove_cable = tk.Button(self.page, text='Remove cable')
        self.remove_cable.grid(row=7, column=1)
        self.update_cable = tk.Button(self.page, text='Update cable')
        self.update_cable.grid(row=7, column=2)
    def add_cable(self):
        self.list_of_cables.insert('end', self.v.get())
