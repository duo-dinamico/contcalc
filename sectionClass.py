#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
sectionClass.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""


class sectionClass:
    def __init__(self):
        self.cable_list = []

    def add_cable(self, cable):
        self.cable_list.append(cable)

    def remove_cable(self, cable):
        self.cable_list.remove(cable)

    def list_cables(self):
        for cable in self.cable_list:
            print(cable.cable_ref)


class cableClass:
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
