# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:03:33 2020

@author: kevin
"""

from modify_func import ModifiyFunc

class UpdateFunc(ModifiyFunc):
    def get_query(self, window):
        update_value = {}
        condition = ''
        for i in range(1, len(window.table_columns)):
            update_value[window.table_columns[i][0]] = window.entry[i].get()
            if condition=='':
                condition = condition + str(f'{window.table_columns[i][0]}="{window.entry[i].get()}"')
            elif update_value[window.table_columns[i][0]] != '':
                condition = condition + ', ' + str(f'{window.table_columns[i][0]}="{window.entry[i].get()}"')
        
        return f'UPDATE {window.table_combo.get()} SET {condition} WHERE {window.table_columns[0][0]}="{window.entry[0].get()}"'
