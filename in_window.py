import tkinter as tk
from tkinter import ttk
from subwindow import SubWindow

class InWindow(SubWindow):
    
    def __init__(self, connection, cursor, font_style, table_name, window_title):
        self.table_name = table_name
        self.cursor = cursor
        self.cursor.execute(f'SHOW COLUMNS FROM {table_name}')
        table_columns = self.cursor.fetchall()
        super().__init__(connection, cursor, font_style, table_name, window_title)
        
        # Condition field
        self.nested_in_label = tk.Label(self.window, text='Nested: IN', font=self.font_style, background='pale green')
        self.nested_in_label.place(x=20, y=60, height=30, width=150)
        self.in_combo = ttk.Combobox(self.window, font=self.font_style, values=['IN', 'NOT IN'])        
        self.in_combo.place(x=380, y=60, height=30, width=90)
        self.in_entry = tk.Entry(self.window, font=self.font_style)
        self.in_entry.place(x=500, y=60, height=30, width=210)
        self.column_combo = ttk.Combobox(self.window, font=self.font_style,
                                         values=[table_columns[i][0] for i in range(len(table_columns))])        
        self.column_combo.place(x=200, y=60, height=30, width=150)
        
        # Display selected table in listbox
        self.listBox.config(columns=table_columns)
        for i in range(len(table_columns)):
            self.listBox.heading(i, text=table_columns[i][0])
            self.listBox.column(i, stretch='True', anchor='center', width='190')
        self.cursor.execute(f'SELECT * FROM {table_name}')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
  
        # Send query button
        self.send_button = tk.Button(self.window, text='Send', command=self.send_query, font=self.font_style)
        self.send_button.place(x=720, y=60, height=30, width=60)
        self.send_button.config(background='medium spring green')
    
    def send_query(self):
        query = f'SELECT * FROM {self.table_name} \
                  WHERE {self.column_combo.get()} {self.in_combo.get()} ({self.in_entry.get()})'
        self.display_result(query)
        
    def clean_value(self):    
        self.column_combo.set('')
        self.in_combo.set('')
        self.in_entry.delete(0, 'end')
    
    