# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:45:30 2020

@author: kevin
"""

import tkinter as tk
import pymysql

from interface import DatabaseWindow

# Create the GUI and pass it to our App class
class ConnectWorkbench(object):
    def __init__(self, ip, user, password, database):
        main_window = tk.Tk()
        try:
            connection = pymysql.connect(ip, user, password, database)
            cursor = connection.cursor()
            DatabaseWindow(main_window, connection, cursor)
            main_window.mainloop()
        finally:
            cursor.close()
