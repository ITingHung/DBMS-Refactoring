import tkinter as tk
import pymysql

from ui import DatabaseWindow


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
