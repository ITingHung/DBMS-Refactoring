import tkinter as tk
import pymysql

from interface import DatabaseInterface

# Create the GUI and pass it to our App class
class ConnectWorkbench(object):
    def __init__(self, ip, user, password, database):
        window = tk.Tk()
        try:
            connection = pymysql.connect(ip, user, password, database)
            cursor = connection.cursor()
            DatabaseInterface(window, connection, cursor)
            window.mainloop()
        finally:
            cursor.close()

if __name__ == "__main__":
    ConnectWorkbench(ip='localhost', user='root', password='red91310', database = 'delivery_db')