#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
pageLookup.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

def pageL_Tray():
    d1 = {
    'Tray Sizes': ['900','750','600','450','300','225','150','100','75','50']
    }

    for k, v in d1.items():
        #return ''.join('{}{}'.format(v,'\n'))
        return k + '\n' + '\n'.join(v)

def pageL_Ladder():
    d1 = {
    'Ladder Sizes': ['900','750','600','450','300','225','150','150','150','150']
    }

    for k, v in d1.items():
        #return ''.join('{}{}'.format(v,'\n'))
        return k + '\n' + '\n'.join(v)

def pageL_Cables():
    d1 = {
    'Cable Type': ['XLPE/SWA/PVC', 'XLPE/SWA/LSF', 'FP400', 'FP600S', 'MICC (Light Duty)', 'MICC (Heavy Duty)', 'LSF Single'],
    'Cores': ['1', '2', '3', '4', '5', '7', '12', '19', '27', '37'],
    'CSA': ['1', '1.5', '2.5', '4', '6', '10', '16', '25', '35', '50', '70', '95', '120', '150', '185', '240', '300', '400', '500', '630', '800', '1000']
    }

    for k, v in d1.items():
        return k + '\n' + '\n'.join(v)
