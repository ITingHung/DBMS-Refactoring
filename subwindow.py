import tkinter as tk
from tkinter import ttk

class SubWindow(object):

    def __init__(self, connection, cursor, font_style, table_name, window_title):
        self.connection = connection
        self.cursor = cursor
        self.font_style = font_style
        self.table_name = table_name
        
        self.window = tk.Toplevel()
        self.window.wm_title(window_title)
        self.window.geometry('800x400')
        self.window.configure(background='white')
        
        self.table_label = tk.Label(self.window, text=f'Table: {table_name}', anchor='w', font=self.font_style)
        self.table_label.place(x=20, y=20, height=30, width=200)
        self.table_label.config(background='white')
        
        # Result field
        self.result = tk.Label(self.window, text='Result', font=self.font_style)
        self.result.place(x=20, y=140, width=760)
        self.result.config(background='gray80')
        self.listBox = ttk.Treeview(self.window, show='headings')
        self.listBox.place(x=20, y=170, height=200, width=760)
        
        # clean input
        self.clean_button = tk.Button(self.window, text="Clean", font=self.font_style, command=self.clean_value)
        self.clean_button.place(x=720, y=20, height=30, width=60) 
        
        ## Rolling bar
        ### y-axis
        self.yscroll = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.listBox.yview)
        self.listBox.configure(yscrollcommand = self.yscroll.set)
        self.yscroll.place(x=780, y=170, height=180)
        ### x-axis
        self.xscroll = ttk.Scrollbar(self.window, orient=tk.HORIZONTAL, command=self.listBox.xview)
        self.listBox.configure(xscrollcommand = self.xscroll.set)
        self.xscroll.place(x=20, y=370, width=760)
    
    def display_result(self, query):
        self.listBox.delete(*self.listBox.get_children())
        self.cursor.execute(query)
        table_result = self.cursor.fetchall()
        print(table_result)
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
    
    def send_query(self):
        pass
    
    def clean_value(self):
        pass
    
        