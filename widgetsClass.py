#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
notebookClass.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import tkinter as tk


class CreateLabel(tk.Label):
    def __init__(self, name, text, image, background, height, width, row, column, colspan, sticky):
        tk.Label.__init__(self)
        label = tk.Label(name, text=text, image=image, bg=background, height=height, width=width)
        label.grid(row=row, column=column, columnspan=colspan, sticky=sticky)


class CreateEntry(tk.Entry):
    def __init__(self, name, text, background, row, column, colspan, sticky):
        tk.Label.__init__(self)
        entry = tk.Entry(master=name, textvariable=text, bg=background)
        entry.grid(row=row, column=column, columnspan=colspan, sticky=sticky)


class CreateButton(tk.Button):
    def __init__(self, name, text, height, width, command, row, column, colspan, sticky):
        tk.Label.__init__(self)
        button = tk.Button(master=name, text=text, height=height, width=width, command=command)
        button.grid(row=row, column=column, columnspan=colspan, sticky=sticky)