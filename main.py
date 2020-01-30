#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 19:33:30 2020
# odetojoy
@author: sj
"""

from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def main():
    root = tk.Tk()
    root.title("Containment Size Calculation")

    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb)

    # second page
    page2 = ttk.Frame(nb)
    text = ScrolledText(page2)
    text.pack(expand=1, fill="both")

    # third page
    page3 = ttk.Frame(nb)
    
    
    nb.add(page1, text='General Data')
    nb.add(page2, text='Calculation')
    nb.add(page3, text='Lookup')

    nb.pack(expand=1, fill="both")

    root.mainloop()

if __name__ == "__main__":
    main()

