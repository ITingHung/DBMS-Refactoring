# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:25:22 2020

@author: user
"""

import tkinter as tk
import pymysql

from interface import DatabaseInterface

# https://www.w3schools.com/python/python_mysql_create_database.asp

# Create the GUI and pass it to our App class
def main(ip, user, password, database):
    window = tk.Tk()
    try:
        connection = pymysql.connect(ip, user, password, database)
        cursor = connection.cursor()
        DatabaseInterface(window, connection, cursor)
        window.mainloop()
    finally:
        cursor.close()

if __name__ == "__main__":
    main(ip='localhost', user='root', password='red91310', database = 'delivery_db')