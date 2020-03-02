#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
appMain.py v1.0
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk
from tkinter import ttk
from menuClass import Menu
from notebookClass import Notebook

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Containment Calculation Sheet')
        self.iconbitmap('images/calc.ico')
        menu = Menu(self)
        self.config(menu=menu)
        Notebook(self)

if __name__ == '__main__':
    app=App()
    app.mainloop()
