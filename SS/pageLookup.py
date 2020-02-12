#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Containment Calculation Sheet
pageLookup.py v0.1
#odetojoy
Copyright 2020, The JJ duo
"""

import sqlite3

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




class ccsDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS cables (id INTEGER PRIMARY KEY, cable_type text, number_cores text, csa text, overall_diam text)')
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM cables')
        rows = self.cur.fetchall()
        return rows

    def insert(self, cable_type, number_cores, csa, overall_diam):
        self.cur.execute('INSERT INTO cables VALUES (NULL, ?, ?, ?, ?)', (cable_type, number_cores, csa, overall_diam))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute('DELETE FROM cables WHERE id=?', (id,))
        self.conn.commit()

    def update(self, id, cable_type, number_cores, csa, overall_diam):
        self.cur.execute('UPDATE cables SET cable_type=?, number_cores=?, csa=?, overall_diam=? WHERE id=?', (cable_type, number_cores, csa, overall_diam, id))
        self.conn.commit()

    def drop_tables(self):
        self.cur.execute('DROP TABLE cables')
        self.cur.execute('CREATE TABLE IF NOT EXISTS cables (id INTEGER PRIMARY KEY, cable_type text, number_cores text, csa text, overall_diam text)')
        self.conn.commit()

    def get_cable_list(self):
        self.cur.execute('SELECT DISTINCT cable_type FROM cables')
        rows = self.cur.fetchall()
        return_list = []
        for li in rows:
            return_list.append(li[0])
        return return_list

    def get_core_list(self):
        self.cur.execute('SELECT DISTINCT number_cores FROM cables')
        rows = self.cur.fetchall()
        return_list = []
        for li in rows:
            return_list.append(li[0])
        return return_list

    def get_csa_list(self):
        self.cur.execute('SELECT DISTINCT csa FROM cables')
        rows = self.cur.fetchall()
        return_list = []
        for li in rows:
            return_list.append(li[0])
        return return_list

    def __del__(self):
        self.conn.close()

def main():
    db = ccsDatabase('database.db')
    db.drop_tables()
    db.insert('XLPE/SWA/PVC', '1', '50', '17.5')
    db.insert('XLPE/SWA/PVC', '1', '70', '20.2')
    db.insert('XLPE/SWA/PVC', '1', '95', '22.3')
    db.insert('XLPE/SWA/PVC', '1', '120', '24.2')
    db.insert('XLPE/SWA/PVC', '1', '150', '27.4')
    db.insert('XLPE/SWA/PVC', '1', '185', '30.0')
    db.insert('XLPE/SWA/PVC', '1', '240', '32.8')
    db.insert('XLPE/SWA/PVC', '1', '300', '35.6')
    db.insert('XLPE/SWA/PVC', '1', '400', '40.4')
    db.insert('XLPE/SWA/PVC', '1', '500', '44.2')
    db.insert('XLPE/SWA/PVC', '1', '630', '48.8')
    db.insert('XLPE/SWA/PVC', '1', '800', '55.4')
    db.insert('XLPE/SWA/PVC', '1', '1000', '60.6')

    db.insert('XLPE/SWA/PVC', '2', '1.5', '12.3')
    db.insert('XLPE/SWA/PVC', '2', '2.5', '13.6')
    db.insert('XLPE/SWA/PVC', '2', '4', '14.7')
    db.insert('XLPE/SWA/PVC', '2', '6', '15.9')
    db.insert('XLPE/SWA/PVC', '2', '10', '18.0')
    db.insert('XLPE/SWA/PVC', '2', '16', '20.4')
    db.insert('XLPE/SWA/PVC', '2', '25', '20.4')
    db.insert('XLPE/SWA/PVC', '2', '35', '23.3')
    db.insert('XLPE/SWA/PVC', '2', '50', '25.8')
    db.insert('XLPE/SWA/PVC', '2', '70', '29.0')
    db.insert('XLPE/SWA/PVC', '2', '95', '33.1')
    db.insert('XLPE/SWA/PVC', '2', '120', '36.1')
    db.insert('XLPE/SWA/PVC', '2', '150', '39.3')
    db.insert('XLPE/SWA/PVC', '2', '185', '44.7')
    db.insert('XLPE/SWA/PVC', '2', '240', '49.0')
    db.insert('XLPE/SWA/PVC', '2', '300', '53.5')
    db.insert('XLPE/SWA/PVC', '2', '400', '59.0')

    db.insert('XLPE/SWA/PVC', '3', '1.5', '12.6')
    db.insert('XLPE/SWA/PVC', '3', '2.5', '14.1')
    db.insert('XLPE/SWA/PVC', '3', '4', '15.3')
    db.insert('XLPE/SWA/PVC', '3', '6', '16.6')
    db.insert('XLPE/SWA/PVC', '3', '10', '19.5')
    db.insert('XLPE/SWA/PVC', '3', '16', '21.6')
    db.insert('XLPE/SWA/PVC', '3', '25', '25.5')
    db.insert('XLPE/SWA/PVC', '3', '35', '28.0')
    db.insert('XLPE/SWA/PVC', '3', '50', '28.5')
    db.insert('XLPE/SWA/PVC', '3', '70', '32.2')
    db.insert('XLPE/SWA/PVC', '3', '95', '37.0')
    db.insert('XLPE/SWA/PVC', '3', '120', '40.4')
    db.insert('XLPE/SWA/PVC', '3', '150', '45.5')
    db.insert('XLPE/SWA/PVC', '3', '185', '49.8')
    db.insert('XLPE/SWA/PVC', '3', '240', '55.1')
    db.insert('XLPE/SWA/PVC', '3', '300', '60.2')
    db.insert('XLPE/SWA/PVC', '3', '400', '66.6')

    db.insert('XLPE/SWA/PVC', '4', '1.5', '13.5')
    db.insert('XLPE/SWA/PVC', '4', '2.5', '15.0')
    db.insert('XLPE/SWA/PVC', '4', '4', '16.4')
    db.insert('XLPE/SWA/PVC', '4', '6', '18.7')
    db.insert('XLPE/SWA/PVC', '4', '10', '21.1')
    db.insert('XLPE/SWA/PVC', '4', '16', '22.9')
    db.insert('XLPE/SWA/PVC', '4', '25', '27.6')
    db.insert('XLPE/SWA/PVC', '4', '35', '30.4')
    db.insert('XLPE/SWA/PVC', '4', '50', '32.0')
    db.insert('XLPE/SWA/PVC', '4', '70', '37.7')
    db.insert('XLPE/SWA/PVC', '4', '95', '41.7')
    db.insert('XLPE/SWA/PVC', '4', '120', '47.1')
    db.insert('XLPE/SWA/PVC', '4', '150', '51.4')
    db.insert('XLPE/SWA/PVC', '4', '185', '56.6')
    db.insert('XLPE/SWA/PVC', '4', '240', '63.0')
    db.insert('XLPE/SWA/PVC', '4', '300', '68.8')
    db.insert('XLPE/SWA/PVC', '4', '400', '78.1')
    
    db.insert('XLPE/SWA/PVC', '5', '1.5', '14.3')
    db.insert('XLPE/SWA/PVC', '5', '2.5', '16.3')
    db.insert('XLPE/SWA/PVC', '5', '4', '17.8')
    db.insert('XLPE/SWA/PVC', '5', '6', '20.0')
    db.insert('XLPE/SWA/PVC', '5', '10', '22.9')
    db.insert('XLPE/SWA/PVC', '5', '16', '26.6')
    db.insert('XLPE/SWA/PVC', '5', '25', '31.5')
    db.insert('XLPE/SWA/PVC', '5', '35', '34.8')
    db.insert('XLPE/SWA/PVC', '5', '50', '40.4')
    db.insert('XLPE/SWA/PVC', '5', '70', '46.3')
    
    db.insert('XLPE/SWA/LSF', '1', '50', '17.5')
    db.insert('XLPE/SWA/LSF', '1', '70', '20.2')
    db.insert('XLPE/SWA/LSF', '1', '95', '22.3')
    db.insert('XLPE/SWA/LSF', '1', '120', '24.2')
    db.insert('XLPE/SWA/LSF', '1', '150', '27.4')
    db.insert('XLPE/SWA/LSF', '1', '185', '30.0')
    db.insert('XLPE/SWA/LSF', '1', '240', '32.8')
    db.insert('XLPE/SWA/LSF', '1', '300', '35.6')
    db.insert('XLPE/SWA/LSF', '1', '400', '40.4')
    db.insert('XLPE/SWA/LSF', '1', '500', '44.2')
    db.insert('XLPE/SWA/LSF', '1', '630', '48.8')
    db.insert('XLPE/SWA/LSF', '1', '800', '55.4')
    db.insert('XLPE/SWA/LSF', '1', '1000', '60.6')
    
    db.insert('XLPE/SWA/LSF', '2', '1.5', '12.3')
    db.insert('XLPE/SWA/LSF', '2', '2.5', '13.6')
    db.insert('XLPE/SWA/LSF', '2', '4', '14.7')
    db.insert('XLPE/SWA/LSF', '2', '6', '15.9')
    db.insert('XLPE/SWA/LSF', '2', '10', '18.0')
    db.insert('XLPE/SWA/LSF', '2', '16', '20.4')
    db.insert('XLPE/SWA/LSF', '2', '25', '20.4')
    db.insert('XLPE/SWA/LSF', '2', '35', '23.3')
    db.insert('XLPE/SWA/LSF', '2', '50', '25.8')
    db.insert('XLPE/SWA/LSF', '2', '70', '29.0')
    db.insert('XLPE/SWA/LSF', '2', '95', '33.1')
    db.insert('XLPE/SWA/LSF', '2', '120', '36.1')
    db.insert('XLPE/SWA/LSF', '2', '150', '39.3')
    db.insert('XLPE/SWA/LSF', '2', '185', '44.7')
    db.insert('XLPE/SWA/LSF', '2', '240', '49.0')
    db.insert('XLPE/SWA/LSF', '2', '300', '53.5')
    db.insert('XLPE/SWA/LSF', '2', '400', '59.0')
    
    db.insert('XLPE/SWA/LSF', '3', '1.5', '12.6')
    db.insert('XLPE/SWA/LSF', '3', '2.5', '14.1')
    db.insert('XLPE/SWA/LSF', '3', '4', '15.3')
    db.insert('XLPE/SWA/LSF', '3', '6', '16.6')
    db.insert('XLPE/SWA/LSF', '3', '10', '19.5')
    db.insert('XLPE/SWA/LSF', '3', '16', '21.6')
    db.insert('XLPE/SWA/LSF', '3', '25', '25.5')
    db.insert('XLPE/SWA/LSF', '3', '35', '28.0')
    db.insert('XLPE/SWA/LSF', '3', '50', '28.5')
    db.insert('XLPE/SWA/LSF', '3', '70', '32.2')
    db.insert('XLPE/SWA/LSF', '3', '95', '37.0')
    db.insert('XLPE/SWA/LSF', '3', '120', '40.4')
    db.insert('XLPE/SWA/LSF', '3', '150', '45.5')
    db.insert('XLPE/SWA/LSF', '3', '185', '49.8')
    db.insert('XLPE/SWA/LSF', '3', '240', '55.1')
    db.insert('XLPE/SWA/LSF', '3', '300', '60.2')
    db.insert('XLPE/SWA/LSF', '3', '400', '66.6')

    db.insert('XLPE/SWA/LSF', '4', '1.5', '13.5')
    db.insert('XLPE/SWA/LSF', '4', '2.5', '15.0')
    db.insert('XLPE/SWA/LSF', '4', '4', '16.4')
    db.insert('XLPE/SWA/LSF', '4', '6', '18.7')
    db.insert('XLPE/SWA/LSF', '4', '10', '21.1')
    db.insert('XLPE/SWA/LSF', '4', '16', '22.9')
    db.insert('XLPE/SWA/LSF', '4', '25', '27.6')
    db.insert('XLPE/SWA/LSF', '4', '35', '30.4')
    db.insert('XLPE/SWA/LSF', '4', '50', '32.0')
    db.insert('XLPE/SWA/LSF', '4', '70', '37.7')
    db.insert('XLPE/SWA/LSF', '4', '95', '41.7')
    db.insert('XLPE/SWA/LSF', '4', '120', '47.1')
    db.insert('XLPE/SWA/LSF', '4', '150', '51.4')
    db.insert('XLPE/SWA/LSF', '4', '185', '56.6')
    db.insert('XLPE/SWA/LSF', '4', '240', '63.0')
    db.insert('XLPE/SWA/LSF', '4', '300', '68.8')
    db.insert('XLPE/SWA/LSF', '4', '400', '78.1')
    
    db.insert('XLPE/SWA/LSF', '5', '1.5', '14.3')
    db.insert('XLPE/SWA/LSF', '5', '2.5', '16.3')
    db.insert('XLPE/SWA/LSF', '5', '4', '17.8')
    db.insert('XLPE/SWA/LSF', '5', '6', '20.0')
    db.insert('XLPE/SWA/LSF', '5', '10', '22.9')
    db.insert('XLPE/SWA/LSF', '5', '16', '26.6')
    db.insert('XLPE/SWA/LSF', '5', '25', '31.5')
    db.insert('XLPE/SWA/LSF', '5', '35', '34.8')
    db.insert('XLPE/SWA/LSF', '5', '50', '40.4')
    db.insert('XLPE/SWA/LSF', '5', '70', '46.3')
    
    db.insert('FP400', '2', '1.5', '12.9')
    db.insert('FP400', '2', '2.5', '14.1')
    db.insert('FP400', '2', '4', '15.2')
    db.insert('FP400', '2', '6', '16.4')
    db.insert('FP400', '2', '10', '18.6')
    db.insert('FP400', '2', '16', '21.4')
    db.insert('FP400', '2', '25', '23.7')
    db.insert('FP400', '2', '35', '27.2')
    db.insert('FP400', '2', '50', '28.0')
    db.insert('FP400', '2', '70', '30.7')
    db.insert('FP400', '2', '95', '35.3')
    db.insert('FP400', '2', '120', '36.6')
    db.insert('FP400', '2', '150', '39.3')
    db.insert('FP400', '2', '185', '44.2')
    db.insert('FP400', '2', '240', '48.0')
    db.insert('FP400', '2', '300', '51.8')
    db.insert('FP400', '2', '400', '55.9')
    
    db.insert('FP400', '3', '1.5', '13.4')
    db.insert('FP400', '3', '2.5', '14.8')
    db.insert('FP400', '3', '4', '16.1')
    db.insert('FP400', '3', '6', '17.4')
    db.insert('FP400', '3', '10', '20.3')
    db.insert('FP400', '3', '16', '22.8')
    db.insert('FP400', '3', '25', '27.4')
    db.insert('FP400', '3', '35', '29.2')
    db.insert('FP400', '3', '50', '33.0')
    db.insert('FP400', '3', '70', '37.0')
    db.insert('FP400', '3', '95', '40.6')
    db.insert('FP400', '3', '120', '43.8')
    db.insert('FP400', '3', '150', '48.0')
    db.insert('FP400', '3', '185', '52.0')
    db.insert('FP400', '3', '240', '57.1')
    db.insert('FP400', '3', '300', '63.0')
    db.insert('FP400', '3', '400', '69.5')

    db.insert('FP400', '4', '1.5', '14.3')
    db.insert('FP400', '4', '2.5', '16.0')
    db.insert('FP400', '4', '4', '17.3')
    db.insert('FP400', '4', '6', '19.6')
    db.insert('FP400', '4', '10', '21.8')
    db.insert('FP400', '4', '16', '24.6')
    db.insert('FP400', '4', '25', '29.1')
    db.insert('FP400', '4', '35', '32.2')
    db.insert('FP400', '4', '50', '35.0')
    db.insert('FP400', '4', '70', '40.2')
    db.insert('FP400', '4', '95', '44.0')
    db.insert('FP400', '4', '120', '48.4')
    db.insert('FP400', '4', '150', '52.5')
    db.insert('FP400', '4', '185', '57.1')
    db.insert('FP400', '4', '240', '62.7')
    db.insert('FP400', '4', '300', '69.6')
    db.insert('FP400', '4', '400', '78.0')

    db.insert('FP400', '7', '1.5', '16.4')
    db.insert('FP400', '7', '2.5', '18.3')
    db.insert('FP400', '7', '4', '20.8')

    db.insert('FP400', '12', '1.5', '21.2')
    db.insert('FP400', '12', '2.5', '24.0')
    db.insert('FP400', '12', '4', '27.3')

    db.insert('FP400', '19', '1.5', '24.2')
    db.insert('FP400', '19', '2.5', '28.6')

    db.insert('FP400', '27', '1.5', '29.4')
    db.insert('FP400', '27', '2.5', '33.4')

    db.insert('FP400', '37', '1.5', '32.2')
    db.insert('FP400', '37', '2.5', '36.7')

    db.insert('FP600S', '2', '4', '21.0')
    db.insert('FP600S', '2', '6', '21.0')
    db.insert('FP600S', '2', '10', '22.0')
    db.insert('FP600S', '2', '16', '23.0')
    db.insert('FP600S', '2', '25', '26.0')
    db.insert('FP600S', '2', '35', '30.0')
    db.insert('FP600S', '2', '50', '31.0')
    db.insert('FP600S', '2', '70', '33.0')
    db.insert('FP600S', '2', '95', '35.0')
    db.insert('FP600S', '2', '120', '39.0')
    db.insert('FP600S', '2', '150', '42.0')
    db.insert('FP600S', '2', '185', '46.0')
    db.insert('FP600S', '2', '240', '51.0')
    db.insert('FP600S', '2', '300', '56.0')
    db.insert('FP600S', '2', '400', '61.0')

    db.insert('FP600S', '3', '4', '21.0')
    db.insert('FP600S', '3', '6', '21.0')
    db.insert('FP600S', '3', '10', '23.0')
    db.insert('FP600S', '3', '16', '24.0')
    db.insert('FP600S', '3', '25', '29.0')
    db.insert('FP600S', '3', '35', '31.0')
    db.insert('FP600S', '3', '50', '32.0')
    db.insert('FP600S', '3', '70', '36.0')
    db.insert('FP600S', '3', '95', '40.0')
    db.insert('FP600S', '3', '120', '43.0')
    db.insert('FP600S', '3', '150', '48.0')
    db.insert('FP600S', '3', '185', '52.0')
    db.insert('FP600S', '3', '240', '57.0')
    db.insert('FP600S', '3', '300', '62.0')
    db.insert('FP600S', '3', '400', '69.0')

    db.insert('FP600S', '4', '4', '21.0')
    db.insert('FP600S', '4', '6', '23.0')
    db.insert('FP600S', '4', '10', '24.0')
    db.insert('FP600S', '4', '16', '27.0')
    db.insert('FP600S', '4', '25', '32.0')
    db.insert('FP600S', '4', '35', '35.0')
    db.insert('FP600S', '4', '50', '36.0')
    db.insert('FP600S', '4', '70', '41.0')
    db.insert('FP600S', '4', '95', '44.0')
    db.insert('FP600S', '4', '120', '49.0')
    db.insert('FP600S', '4', '150', '55.0')
    db.insert('FP600S', '4', '185', '59.0')
    db.insert('FP600S', '4', '240', '64.0')
    db.insert('FP600S', '4', '300', '70.0')
    db.insert('FP600S', '4', '400', '79.0')

    db.insert('MICC (Light Duty)', '2', '1', '6.6')
    db.insert('MICC (Light Duty)', '2', '1.5', '7.2')
    db.insert('MICC (Light Duty)', '2', '2.5', '8.1')
    db.insert('MICC (Light Duty)', '2', '4', '9.4')

    db.insert('MICC (Light Duty)', '3', '1', '7.3')
    db.insert('MICC (Light Duty)', '3', '1.5', '7.9')
    db.insert('MICC (Light Duty)', '3', '2.5', '9.0')

    db.insert('MICC (Light Duty)', '4', '1', '7.8')
    db.insert('MICC (Light Duty)', '4', '1.5', '8.5')
    db.insert('MICC (Light Duty)', '4', '2.5', '9.8')

    db.insert('MICC (Light Duty)', '7', '1', '9.3')
    db.insert('MICC (Light Duty)', '7', '1.5', '10.1')
    db.insert('MICC (Light Duty)', '7', '2.5', '11.4')

    db.insert('MICC (Heavy Duty)', '1', '10', '9.0')
    db.insert('MICC (Heavy Duty)', '1', '16', '10.0')
    db.insert('MICC (Heavy Duty)', '1', '25', '11.3')
    db.insert('MICC (Heavy Duty)', '1', '35', '12.4')
    db.insert('MICC (Heavy Duty)', '1', '50', '13.8')
    db.insert('MICC (Heavy Duty)', '1', '70', '15.4')
    db.insert('MICC (Heavy Duty)', '1', '95', '17.7')
    db.insert('MICC (Heavy Duty)', '1', '120', '19.1')
    db.insert('MICC (Heavy Duty)', '1', '150', '20.7')
    db.insert('MICC (Heavy Duty)', '1', '185', '23.2')
    db.insert('MICC (Heavy Duty)', '1', '240', '26.1')

    db.insert('MICC (Heavy Duty)', '2', '1.5', '9.6')
    db.insert('MICC (Heavy Duty)', '2', '2.5', '10.4')
    db.insert('MICC (Heavy Duty)', '2', '4', '11.5')
    db.insert('MICC (Heavy Duty)', '2', '6', '12.6')
    db.insert('MICC (Heavy Duty)', '2', '10', '14.4')
    db.insert('MICC (Heavy Duty)', '2', '16', '16.4')
    db.insert('MICC (Heavy Duty)', '2', '25', '19.4')
    
    db.insert('MICC (Heavy Duty)', '3', '1.5', '10.0')
    db.insert('MICC (Heavy Duty)', '3', '2.5', '11.0')
    db.insert('MICC (Heavy Duty)', '3', '4', '12.1')
    db.insert('MICC (Heavy Duty)', '3', '6', '13.2')
    db.insert('MICC (Heavy Duty)', '3', '10', '15.3')
    db.insert('MICC (Heavy Duty)', '3', '16', '17.9')
    db.insert('MICC (Heavy Duty)', '3', '25', '20.5')
    
    db.insert('MICC (Heavy Duty)', '4', '1.5', '10.8')
    db.insert('MICC (Heavy Duty)', '4', '2.5', '11.8')
    db.insert('MICC (Heavy Duty)', '4', '4', '13.1')
    db.insert('MICC (Heavy Duty)', '4', '6', '14.4')
    db.insert('MICC (Heavy Duty)', '4', '10', '16.5')
    db.insert('MICC (Heavy Duty)', '4', '16', '19.6')
    db.insert('MICC (Heavy Duty)', '4', '25', '22.9')
    
    db.insert('MICC (Heavy Duty)', '7', '1.5', '12.5')
    db.insert('MICC (Heavy Duty)', '7', '2.5', '13.8')

    db.insert('MICC (Heavy Duty)', '12', '1.5', '15.8')
    db.insert('MICC (Heavy Duty)', '12', '2.5', '17.9')

    db.insert('MICC (Heavy Duty)', '19', '1.5', '18.9')

    db.insert('LSF Single', '1', '1.5', '3.4')
    db.insert('LSF Single', '1', '2.5', '4.2')
    db.insert('LSF Single', '1', '4', '4.8')
    db.insert('LSF Single', '1', '6', '5.4')
    db.insert('LSF Single', '1', '10', '6.8')
    db.insert('LSF Single', '1', '16', '8.0')
    db.insert('LSF Single', '1', '25', '9.8')
    db.insert('LSF Single', '1', '35', '11.0')
    db.insert('LSF Single', '1', '50', '13.0')
    db.insert('LSF Single', '1', '70', '15.0')
    db.insert('LSF Single', '1', '95', '17.0')
    db.insert('LSF Single', '1', '120', '19.0')
    db.insert('LSF Single', '1', '150', '21.0')
    db.insert('LSF Single', '1', '185', '23.5')
    db.insert('LSF Single', '1', '240', '26.5')
    db.insert('LSF Single', '1', '300', '29.5')
    db.insert('LSF Single', '1', '400', '33.5')
    db.insert('LSF Single', '1', '500', '37.0')
    db.insert('LSF Single', '1', '630', '41')
    
    # for a in db.fetch():
    #     print(a)
    print(db.get_cable_list())

if __name__ == "__main__":
    main()
