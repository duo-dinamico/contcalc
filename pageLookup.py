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

    # title = str(d1.keys())
    # content = str(d1.values())

    for k, v in d1.items():
        #return ''.join('{}{}'.format(v,'\n'))
        return k + '\n' + '\n'.join(v)

def pageL_Ladder():
    d1 = {
    'Ladder Sizes': ['900','750','600','450','300','225','150','150','150','150']
    }

    # title = str(d1.keys())
    # content = str(d1.values())

    for k, v in d1.items():
        #return ''.join('{}{}'.format(v,'\n'))
        return k + '\n' + '\n'.join(v)
