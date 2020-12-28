# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:37:21 2020

@author: kevin
"""

class ModifiyFunc(object):
    def __init__(self, window):
        query = self.get_query(window)
        
        window.cursor.execute(query)  
        window.connection.commit()
        window.display_result(f'SELECT * FROM {window.table_combo.get()}')

    def get_query(self, window):
        pass
    
    