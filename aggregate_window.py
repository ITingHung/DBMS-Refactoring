import tkinter as tk
from tkinter import ttk

from window import Window

class AggregateWindow(Window):
    def __init__(self, connection, cursor, font_style):
        super().__init__(connection, cursor, font_style)
        self.window.wm_title('Aggregate')
        self.window.geometry('800x700')
        
        # Decide the position
        ## Result field
        self.result.place(x=20, y=440, width=760)
        self.listBox.place(x=20, y=470, height=200, width=760)
        self.yscroll.place(x=780, y=470, height=180)
        self.xscroll.place(x=20, y=670, width=760)
        ## Query button
        self.query_button.place(x=720, y=190, height=50, width=60)

    def initial_gui(self):
        # Get column infomation of the selected table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        self.table_columns = self.cursor.fetchall()
        self.display_condition() # Display condition field
        self.total_record(self.table_combo.get()) # Show total record of the selected table
        self.display_result(f'SELECT * FROM {self.table_combo.get()}') # Display record
    
    # Condition field
    def display_condition(self):
        # Label
        self.condition_label = tk.Label(self.window, text='Condition', font=self.font_style)
        self.condition_label.place(x=20, y=100, height=30, width=760)
        self.condition_label.config(background='gray80')
        # Combobox
        combo_label, self.column_combo = [], []
        for i in range(len(self.table_columns)):
            combo_label.append(tk.Label(self.window, text=self.table_columns[i][0], font=self.font_style))
            combo_label[i].place(x=20+190*(i), y=130, height=30, width=190)
            self.cursor.execute(f'SELECT DISTINCT {self.table_columns[i][0]} FROM {self.table_combo.get()}')
            self.column_combo.append(ttk.Combobox(self.window, values=self.cursor.fetchall(), font=self.font_style))
            self.column_combo[i].place(x=20+190*(i), y=160, height=30, width=190)   

    # Show the number of total record in selected table
    def total_record(self, table_name):
        self.record_label = tk.Label(self.window, text='', anchor='w', font=self.font_style)
        self.record_label.place(x=20, y=50, height=30, width=200)
        self.record_label.config(background='white')
        self.cursor.execute(f'SELECT COUNT(*) FROM {self.table_combo.get()}')
        count_total = self.cursor.fetchone()[0]
        self.record_label.config(text=f'Total Record: {count_total}') 

    def send_query(self):
        # Count the number of record that satisfiy the condition
        for i in range(len(self.column_combo)):
            if self.column_combo[i].get():
                self.condition = f'{self.table_columns[i][0]}="{self.column_combo[i].get()}"'
                self.cursor.execute(f'SELECT COUNT({self.table_columns[i][0]}) FROM {self.table_combo.get()} WHERE {self.condition}')
        count_condition = self.cursor.fetchone()[0]
        self.count_result = tk.Label(self.window, text=f'Record: {count_condition}', background='gray80', font=self.font_style)
        self.count_result.place(x=630, y=360, height=30, width=150)
        # Find int atribute for sum, max, min, avg.
        aggregate_list = ['Sum', 'Max', 'Min', 'Avg']
        for i in range(len(self.table_columns)):
            self.agg_result = []
            if self.table_columns[i][1]=='int':
                for agg in range(len(aggregate_list)):
                    self.cursor.execute(f'SELECT {aggregate_list[agg]}({self.table_columns[i][0]}) FROM {self.table_combo.get()}')
                    agg_total = self.cursor.fetchone()[0]
                    self.cursor.execute(f'SELECT {aggregate_list[agg]}({self.table_columns[i][0]}) FROM {self.table_combo.get()} WHERE {self.condition}')
                    agg_condition = self.cursor.fetchone()[0]
                    self.agg_result.append(tk.Label(self.window, 
                                                    text=f'{aggregate_list[agg]}: {round(agg_condition, 0)}/{round(agg_total, 0)}', 
                                                    background='gray80', 
                                                    font=self.font_style))
                    self.agg_result[agg].place(x=20+190*i, y=240+30*agg, height=30, width=190)
        # Display record         
        self.display_result(f'SELECT * FROM {self.table_combo.get()} WHERE {self.condition}') 
    
    def clean_value(self):
        for i in range(len(self.column_combo)):
            self.column_combo[i].set('')
