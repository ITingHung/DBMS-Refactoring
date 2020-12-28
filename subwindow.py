import tkinter as tk
from tkinter import ttk

from window import Window

class SubWindow(Window):

    def __init__(self, connection, cursor, font_style, table_name, window_title):
        super().__init__(connection, cursor, font_style)
        self.table_name = table_name
        
        self.window.wm_title(window_title)
        self.window.geometry('800x400')
        
        self.table_label = tk.Label(self.window, text=f'Table: {table_name}', anchor='w', font=self.font_style)
        self.table_label.place(x=20, y=20, height=30, width=200)
        self.table_label.config(background='white')
        
        # clean input
        self.clean_button = tk.Button(self.window, text="Clean", font=self.font_style, command=self.clean_value)
        self.clean_button.place(x=720, y=20, height=30, width=60) 
        
        # Result field
        self.result = tk.Label(self.window, text='Result', font=self.font_style)
        self.result.place(x=20, y=140, width=760)
        self.result.config(background='gray80')
        self.listBox = ttk.Treeview(self.window, show='headings')
        self.listBox.place(x=20, y=170, height=200, width=760)
        
        ## Rolling bar
        ### y-axis
        self.yscroll = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.listBox.yview)
        self.listBox.configure(yscrollcommand = self.yscroll.set)
        self.yscroll.place(x=780, y=170, height=180)
        ### x-axis
        self.xscroll = ttk.Scrollbar(self.window, orient=tk.HORIZONTAL, command=self.listBox.xview)
        self.listBox.configure(xscrollcommand = self.xscroll.set)
        self.xscroll.place(x=20, y=370, width=760)
        
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_name}')
        self.table_columns = self.cursor.fetchall()
        self.display_result(f'SELECT * FROM {self.table_name}')

    def display_result(self, query):
        super().display_result(self.listBox, self.cursor, query)

    def send_query(self):
        pass
    
    def clean_value(self):
        pass
    
        