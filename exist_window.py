import tkinter as tk
from tkinter import ttk
from subwindow import SubWindow

class ExistWindow(SubWindow):
    
    def __init__(self, connection, cursor, font_style, table_name, window_title):
        self.table_name = table_name
        self.cursor = cursor
        self.cursor.execute(f'SHOW COLUMNS FROM {table_name}')
        table_columns = self.cursor.fetchall()
        super().__init__(connection, cursor, font_style, table_name, window_title)
        
        # Condition field
        self.exist_combo = ttk.Combobox(self.window, font=self.font_style, values=['EXISTS', 'NOT EXISTS'])        
        self.exist_combo.place(x=25, y=60, height=30, width=125)
        self.select_columns_combo = ttk.Combobox(self.window, font=self.font_style)          
        self.select_columns_combo.place(x=295, y=60, height=30, width=180)
        self.equal_label = tk.Label(self.window, text='=', font=self.font_style, background='pale green')
        self.equal_label.place(x=485, y=60, height=30, width=35)
        self.current_columns_combo = ttk.Combobox(self.window, font=self.font_style, 
                                                    values=[table_columns[i][0] for i in range(len(table_columns))])          
        self.current_columns_combo.place(x=530, y=60, height=30, width=180)            
        # Display columns of the current table in listbox
        self.listBox.config(columns=table_columns)
        for i in range(len(table_columns)):
            self.listBox.heading(i, text=table_columns[i][0])
            self.listBox.column(i, stretch='True', anchor='center', width='190')
        
        # Provide columns of the selected table to select_table_combo
        self.cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
        table_category = self.cursor.fetchall()
        self.select_table_combo = ttk.Combobox(self.window, font=self.font_style, 
                                                values=[table_category[i][2] for i in range(len(table_category))])          
        self.select_table_combo.place(x=160, y=60, height=30, width=125)
        self.select_table_combo.bind("<<ComboboxSelected>>", self.create_column_combo)
    
        # Send query button
        self.send_button = tk.Button(self.window, text='Send', command=self.send_query, font=self.font_style)
        self.send_button.place(x=720, y=60, height=30, width=55)
        self.send_button.config(background='medium spring green')
    
    def send_query(self):
        query = f'SELECT * FROM {self.table_name} \
                  WHERE {self.exist_combo.get()} \
                  (SELECT * FROM {self.select_table_combo.get()} \
                  WHERE {self.table_name}.{self.current_columns_combo.get()}={self.select_table_combo.get()}.{self.select_columns_combo.get()})'
        self.display_result(query)
    
    def create_column_combo(self, event):
        self.cursor.execute(f'SHOW COLUMNS FROM {self.select_table_combo.get()}')
        select_table_columns = self.cursor.fetchall()
        self.select_columns_combo['values'] = [select_table_columns[i][0] for i in range(len(select_table_columns))]
      
    def clean_value(self):    
        self.exist_combo.set('')
        self.select_table_combo.set('')
        self.select_columns_combo.set('')
        self.current_columns_combo.set('')
        