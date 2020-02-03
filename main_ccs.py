#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
main_ccs.py v0.2
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

# Assign variables to our modules
pageG = pageGeneral
pageC = pageCalculation
pageL = pageLookup

# Initiate the main window for tkinter
mainWindow = tk.Tk()
mainWindow.title('Containment Calculation Sheet')
mainWindow.geometry('500x500')

# Initiate the notebook inside the main window
nb = ttk.Notebook(mainWindow, height=500, width=500)
nb.grid()

# Page 1 for General information about the project
# General page might not link to external module
page1 = ttk.Frame(nb, height=500, width=500)
nb.add(page1, text='General Information')
# L1 = tk.Label(page1, text=pageG.pageG()) .grid(row=0, column=0)
gifLogo = tk.PhotoImage(file='ArupLogo.gif')
#logoCanvas = tk.Canvas(page1)
#logoCanvas.grid(row=0, column=0)
#logoCanvas.create_image(50, 20, anchor='center', image=gifLogo)
logoLabel = tk.Label(page1, image=gifLogo).grid(row=0, columnspan=8, pady=20)

jobTitleLabel1 = tk.Label(page1, text='Job Title').grid(row=1, column=0, columnspan=4, sticky='W', pady=10)
jobTitleLabel2 = tk.Label(page1, text='Project Churchill', bg='white').grid(row=1, column=4, columnspan=4, sticky='E')

jobNumberLabel1 = tk.Label(page1, text='Job Number').grid(row=2, column=0, sticky='W', pady=10,)
jobNumberLabel2 = tk.Label(page1, text='200000', bg='white').grid(row=2, column=1, sticky='E')
refLabel1 = tk.Label(page1, text='Reference').grid(row=2, column=6, sticky='W', pady=10)
refLabel2 = tk.Label(page1, text='A', bg='white').grid(row=2, column=7, sticky='E')

dateLabel1 = tk.Label(page1, text='Date').grid(row=3, column=0, sticky='W', pady=10)
dateLabel2 = tk.Label(page1, text='2020/02/02', bg='white').grid(row=3, column=1, sticky='E')
designerLabel1 = tk.Label(page1, text='Designer').grid(row=4, column=6, sticky='W', pady=10)
designerLabel2 = tk.Label(page1, text='JJ', bg='white').grid(row=4, column=7, sticky='E')

revLabel1 = tk.Label(page1, text='Revision').grid(row=4, column=0, sticky='W', pady=10)
revLabel2 = tk.Label(page1, text='P01', bg='white').grid(row=4, column=1, sticky='E')

titleLabel = tk.Label(page1, text='ESN Calc Sheet\nContainment sizing spreadsheet\nRevision 0.1 Feb20', justify='center').grid(row=5, column=0, columnspan=8, sticky='NSWE')

# Page 2 for Calculation information
page2 = ttk.Frame(nb)
nb.add(page2, text='Calculation', sticky='NESW')
L2 = tk.Label(page2, text=pageC.pageC()) .grid(row=0, column=0)

# Page 3 for look up tables
page3 = ttk.Frame(nb)
nb.add(page3, text='LookUp Tables')
L_Cabe = tk.Label(page3, text=pageL.pageL_Cables(), bg='white').grid(row=0, column=1)
L_Tray = tk.Label(page3, text=pageL.pageL_Tray(), bg='white').grid(row=0, column=5)
L_Ladder = tk.Label(page3, text=pageL.pageL_Ladder(), bg='white').grid(row=0, column=6)

# Loop to run the main window
mainWindow.mainloop()
