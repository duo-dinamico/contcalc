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

    # Falta aqui grande parte da lista

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

    # Falta aqui grande parte da lista



    # for a in db.fetch():
    #     print(a)
    print(db.get_cable_list())

if __name__ == "__main__":
    main()
