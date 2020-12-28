import tkinter as tk
from tkinter import ttk

from window import Window

class ExistWindow(Window):
    def __init__(self, connection, cursor, font_style):
        super().__init__(connection, cursor, font_style)
        self.window.wm_title('Exist')
        self.window.geometry('800x400')

        # Condition field
        self.exist_combo = ttk.Combobox(self.window, font=self.font_style, values=['EXISTS', 'NOT EXISTS'])        
        self.exist_combo.place(x=20, y=60, height=30, width=105)
        self.select_columns_combo = ttk.Combobox(self.window, font=self.font_style)          
        self.select_columns_combo.place(x=295, y=60, height=30, width=180)
        self.equal_label = tk.Label(self.window, text='=', font=self.font_style, background='pale green')
        self.equal_label.place(x=485, y=60, height=30, width=35)
        
        # Decide the position
        ## Result field
        self.result.place(x=20, y=140, width=760)
        self.listBox.place(x=20, y=170, height=200, width=760)
        self.xscroll.place(x=20, y=370, width=760)
        self.yscroll.place(x=780, y=170, height=180)
        ## Query button
        self.query_button.place(x=720, y=60, height=30, width=60)

        # Provide columns of the selected table to select_table_combo
        self.cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
        table_category = self.cursor.fetchall()
        self.select_table_combo = ttk.Combobox(self.window, font=self.font_style, 
                                                values=[table_category[i][2] for i in range(len(table_category))])          
        self.select_table_combo.place(x=135, y=60, height=30, width=150)
        self.select_table_combo.bind("<<ComboboxSelected>>", self.create_column_combo)
    
    def initial_gui(self):
        self.current_columns_combo = ttk.Combobox(self.window, font=self.font_style, 
                                                  values=[self.table_columns[i][0] 
                                                          for i in range(len(self.table_columns))])          
        self.current_columns_combo.place(x=530, y=60, height=30, width=180)       

    def create_column_combo(self, event):
        self.cursor.execute(f'SHOW COLUMNS FROM {self.select_table_combo.get()}')
        select_table_columns = self.cursor.fetchall()
        self.select_columns_combo['values'] = [select_table_columns[i][0] for i in range(len(select_table_columns))]
    
    def send_query(self):
        query = f'SELECT * FROM {self.table_combo.get()} \
                  WHERE {self.exist_combo.get()} \
                  (SELECT * FROM {self.select_table_combo.get()} \
                  WHERE {self.table_combo.get()}.{self.current_columns_combo.get()}={self.select_table_combo.get()}.{self.select_columns_combo.get()})'
        self.display_result(query)
  
    def clean_value(self):    
        self.exist_combo.set('')
        self.select_table_combo.set('')
        self.select_columns_combo.set('')
        self.current_columns_combo.set('')
