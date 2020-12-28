# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:29:14 2020

@author: kevin
"""

import tkinter as tk

class Window(object):
    def __init__(self, connection, cursor, font_style):
        self.connection = connection
        self.cursor = cursor
        self.font_style = font_style
        
        self.window= tk.Toplevel()
        self.window.configure(background='white')

    def display_result(self, result_field, cursor, query):
        cursor.execute(query)
        table_columns = cursor.description
        result_field.config(columns=table_columns)
        for i in range(len(table_columns)):
            result_field.heading(i, text=table_columns[i][0])
            result_field.column(i, stretch='True', anchor='center', width='190')
        
        result_field.delete(*result_field.get_children())
        table_result = cursor.fetchall()
        if table_result:
            for row in table_result:
                result_field.insert('', 'end', values=row)
        
        