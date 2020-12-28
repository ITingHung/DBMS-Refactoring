import tkinter as tk
from tkinter import ttk

from window import Window

class InWindow(Window):
    def __init__(self, connection, cursor, font_style):
        super().__init__(connection, cursor, font_style)
        self.window.wm_title('Nested: IN')
        self.window.geometry('800x400')
        
        # Condition field
        self.nested_in_label = tk.Label(self.window, text='Nested: IN', font=self.font_style, background='pale green')
        self.nested_in_label.place(x=20, y=60, height=30, width=150)
        self.in_combo = ttk.Combobox(self.window, font=self.font_style, values=['IN', 'NOT IN'])        
        self.in_combo.place(x=380, y=60, height=30, width=90)
        self.in_entry = tk.Entry(self.window, font=self.font_style)
        self.in_entry.place(x=500, y=60, height=30, width=210)

        # Decide the position
        ## Result field
        self.result.place(x=20, y=140, width=760)
        self.listBox.place(x=20, y=170, height=200, width=760)
        self.xscroll.place(x=20, y=370, width=760)
        self.yscroll.place(x=780, y=170, height=180)
        ## Query button
        self.query_button.place(x=720, y=60, height=30, width=60)
        
    def initial_gui(self):
        self.column_combo = ttk.Combobox(self.window, font=self.font_style,
                                         values=[self.table_columns[i][0] for i in range(len(self.table_columns))])        
        self.column_combo.place(x=200, y=60, height=30, width=150)

    def send_query(self):
        query = f'SELECT * FROM {self.table_combo.get()} \
                  WHERE {self.column_combo.get()} {self.in_combo.get()} ({self.in_entry.get()})'
        self.display_result(query)
        
    def clean_value(self):    
        self.column_combo.set('')
        self.in_combo.set('')
        self.in_entry.delete(0, 'end')
    
    