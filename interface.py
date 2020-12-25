# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:02:15 2020

@author: kevin
"""

import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.scrolledtext import ScrolledText

class AggregateInterface(object):
    def __init__(self, connection, cursor, font_style, table_name):
        self.connection = connection
        self.cursor = cursor
        self.font_style = font_style
        self.table_name = table_name
        
        self.window = tk.Toplevel()
        self.window.wm_title("Aggregate")
        self.window.geometry('800x400')
        self.window.configure(background='white')
        
        self.table_label = tk.Label(self.window, text=f'Table: {table_name}', anchor='w', font=self.font_style)
        self.table_label.place(x=20, y=20, height=30, width=200)
        self.table_label.config(background='white')
        
        self.record_label = tk.Label(self.window, text='', anchor='w', font=self.font_style)
        self.record_label.place(x=20, y=50, height=30, width=200)
        self.record_label.config(background='white')
        
        self.condition_label = tk.Label(self.window, text='Condition', font=self.font_style)
        self.condition_label.place(x=20, y=100, height=30, width=760)
        self.condition_label.config(background='gray80')
        
        # Count button
        self.count_button = tk.Button(self.window, text=f'Count', font=self.font_style, command=self.count_function)
        self.count_button.place(x=20, y=200, height=30, width=760)
        self.count_button.config(background='gold')
        
        # Clean combobox
        self.clean_button = tk.Button(self.window, text=f'Clean', font=self.font_style, command=self.clean_value)
        self.clean_button.place(x=630, y=20, height=30, width=150)
        self.clean_button.configure(background='white')
        
        # Get column infomation of the selected table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_name}')
        self.table_columns = self.cursor.fetchall()
        self.display_condition()
        self.total_record(table_name)
    
    def display_condition(self):
        # Combo
        combo_label, self.column_combo = [], []
        for i in range(len(self.table_columns)):
            combo_label.append(tk.Label(self.window, text=self.table_columns[i][0], font=self.font_style))
            combo_label[i].place(x=20+190*(i), y=130, height=30, width=190)
            self.cursor.execute(f'SELECT DISTINCT {self.table_columns[i][0]} FROM {self.table_name}')
            self.column_combo.append(ttk.Combobox(self.window, values=self.cursor.fetchall(), font=self.font_style))
            self.column_combo[i].place(x=20+190*(i), y=160, height=30, width=190)   

    def total_record(self, table_name):
        # Show total number of record
        self.cursor.execute(f'SELECT COUNT(*) FROM {self.table_name}')
        count_total = self.cursor.fetchone()[0]
        self.record_label.config(text=f'Total Record: {count_total}')           
        
    def count_function(self):
        # count
        for i in range(len(self.column_combo)):
            if self.column_combo[i].get():
                self.condition = f'{self.table_columns[i][0]}="{self.column_combo[i].get()}"'
                self.cursor.execute(f'SELECT COUNT({self.table_columns[i][0]}) FROM {self.table_name} WHERE {self.condition}')
        count_condition = self.cursor.fetchone()[0]
        self.count_result = tk.Label(self.window, text=f'Record: {count_condition}', background='gray80', font=self.font_style)
        self.count_result.place(x=630, y=360, height=30, width=150)
        
        # find int atribute for sum, max, min, avg.
        aggregate_list = ['Sum', 'Max', 'Min', 'Avg']
        for i in range(len(self.table_columns)):
            self.agg_result = []
            if self.table_columns[i][1]=='int':
                for agg in range(len(aggregate_list)):
                    self.cursor.execute(f'SELECT {aggregate_list[agg]}({self.table_columns[i][0]}) FROM {self.table_name}')
                    agg_total = self.cursor.fetchone()[0]
                    self.cursor.execute(f'SELECT {aggregate_list[agg]}({self.table_columns[i][0]}) FROM {self.table_name} WHERE {self.condition}')
                    agg_condition = self.cursor.fetchone()[0]
                    self.agg_result.append(tk.Label(self.window, 
                                                    text=f'{aggregate_list[agg]}: {round(agg_condition, 0)}/{round(agg_total, 0)}', 
                                                    background='gray80', 
                                                    font=self.font_style))
                    self.agg_result[agg].place(x=20+190*i, y=240+30*agg, height=30, width=190)         

    def clean_value(self):
        for i in range(len(self.column_combo)):
            self.column_combo[i].set('')
        
class ButtonInterface(object):
    def __init__(self, connection, cursor, font_style):
        self.connection = connection
        self.cursor = cursor
        self.font_style = font_style

        self.window = tk.Toplevel()
        self.window.wm_title("Button Interface")
        self.window.geometry('800x700')
        self.window.configure(background='white')
        
        # Combo
        self.combo_label = tk.Label(self.window, text="Table", font=self.font_style)
        self.combo_label.place(x=20, y=20, width=100)
        self.combo_label.config(background='gray80')
        
        # Search field
        # Search button
        self.search_button = tk.Button(self.window, text="Search", font=self.font_style, command=self.send_search)
        self.search_button.place(x=350, y=15, width=100)
        # Search status
        self.status_label = tk.Label(self.window, text='', font=self.font_style)
        self.status_label.configure(background = 'white')
        self.status_label.place(x=20, y=60, width=760)
        
        # Condition field
        self.condition_label = tk.Label(self.window, text='Condition', font=self.font_style)
        self.condition_label.place(x=20, y=90, height=30, width=760)
        self.condition_label.config(background='gray80')
        self.label = []
        for i in range(4):
            self.label.append(tk.Label(self.window, text='', font=self.font_style))
            self.label[i].place(x=20+190*(i), y=120, height=30, width=190)
        
        # Result field
        self.result = tk.Label(self.window, text='Result', font=self.font_style)
        self.result.place(x=20, y=440, width=760)
        self.result.config(background='gray80')
        self.listBox = ttk.Treeview(self.window, show='headings')
        self.listBox.place(x=20, y=470, height=200, width=760)
        self.listBox.bind("<<TreeviewSelect>>", self.on_listbox_select)
        ## Rolling bar
        ### y-axis
        self.yscroll = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.listBox.yview)
        self.listBox.configure(yscrollcommand = self.yscroll.set)
        self.yscroll.place(x=780, y=470, height=180)
        ### x-axis
        self.xscroll = ttk.Scrollbar(self.window, orient=tk.HORIZONTAL, command=self.listBox.xview)
        self.listBox.configure(xscrollcommand = self.xscroll.set)
        self.xscroll.place(x=20, y=670, width=760)
        
        self.display_table_combo()
        
    def display_table_combo(self):
        self.cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
        table_name = self.cursor.fetchall()
        self.table_combo = ttk.Combobox(self.window, font=self.font_style,
                                        values=[table_name[i][2] for i in range(len(table_name))])
        self.table_combo.place(x=120, y=20, height=30, width=200)
            
    def send_search(self):
        self.select_button = tk.Button(self.window, text='Condition Search', font=self.font_style, command=self.condi_search_fun)          
        self.select_button.place(x=620, y=50, width=160)
        self.select_button.config(background='light sky blue')
        
        for i in range(len(self.label)):
            self.label[i].config(text='')
        self.listBox.delete(*self.listBox.get_children())
        # Display select table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        table_columns = self.cursor.fetchall()
        self.listBox.config(columns=table_columns)
        for i in range(len(table_columns)):
            self.listBox.heading(i, text=table_columns[i][0])
            self.listBox.column(i, stretch='True', anchor='center', width='190')
        
        # Entry
        text, self.entry = [], []
        for i in range(len(table_columns)):
            self.label[i].config(text=table_columns[i][0])
            text.append(tk.StringVar())
            self.entry.append(tk.Entry(self.window, textvariable=text[i], font=self.font_style))
            self.entry[i].place(x=20+190*(i), y=150, height=40, width=190)
                
        # Buttons
        function_label = tk.Label(self.window, text="Function", font=self.font_style, background='goldenrod1')
        function_label.place(x=20, y=200, height=30, width=150) 
        
        insert_button = tk.Button(self.window, text="Insert", font=self.font_style, command=self.insert)
        insert_button.place(x=200, y=200, height=30, width=100) 
        insert_button.config(background='Gold')
        
        delete_button = tk.Button(self.window, text="Delete", font=self.font_style, command=self.delete)
        delete_button.place(x=330, y=200, height=30, width=100) 
        delete_button.config(background='Gold')
        
        update_button = tk.Button(self.window, text="Update", font=self.font_style, command=self.update)
        update_button.place(x=460, y=200, height=30, width=100) 
        update_button.config(background='Gold')
        
        aggregate_button = tk.Button(self.window, text="Aggregate", font=self.font_style, command=self.aggregate)
        aggregate_button.place(x=590, y=200, height=30, width=100) 
        aggregate_button.config(background='Gold')
        
        clean_button = tk.Button(self.window, text="Clean", font=self.font_style, command=self.clean)
        clean_button.place(x=720, y=200, height=50, width=60) 
        
        self.select_columns_combo = ttk.Combobox(self.window, font=self.font_style)          
        self.select_columns_combo.place(x=420, y=400, height=30, width=120)
        
        self.agg_combo = ttk.Combobox(self.window, font=self.font_style)        
        self.agg_combo.place(x=380, y=300, height=30, width=100)
        
        self.cursor.execute(f'SELECT * FROM {self.table_combo.get()}')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
        self.status_label.configure(text = '')
        self.status_label.configure(background = 'white')
        
        # Having field
        self.having_display()
        self.groupby_combo.config(state='disable')
        self.ope_combo.config(state='disable')
        self.condition_entry.config(state='disable')
        self.having_button.config(state='disable')
        self.havcol_combo.config(state='disable')
        self.agg_combo.config(state='disable')
        for i in range(len(table_columns)):
            if table_columns[i][1]=='int':
                self.groupby_combo.config(state='normal')
                self.ope_combo.config(state='normal')
                self.condition_entry.config(state='normal')
                self.having_button.config(state='normal')
                self.havcol_combo.config(state='normal')
                self.agg_combo.config(state='normal')
                break
        
        # Nested field
        self.in_display()
        self.exist_display()           
        # except:
        #     self.status_label.configure(text = 'Please select a table', fg='white')
        #     self.status_label.configure(background = 'orange red')

    def condi_search_fun(self):
        self.listBox.delete(*self.listBox.get_children())
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        select_value = {}
        condition = ''
        table_columns = self.cursor.fetchall()
        for i in range(len(table_columns)):
            select_value[table_columns[i][0]] = self.entry[i].get()
            if select_value[table_columns[i][0]] != '' and condition=='':
                condition = condition + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
            elif select_value[table_columns[i][0]] != '':
                condition = condition + ' AND ' + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
        self.cursor.execute(f'SELECT * FROM {self.table_combo.get()} WHERE {condition}')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
    
    def clean(self):    
        for i in range(len(self.entry)):
            self.entry[i].delete(0, 'end')
        self.exist_combo.set('')
        self.select_table_combo.set('')
        self.select_columns_combo.set('')
        self.current_columns_combo.set('')
        self.column_combo.set('')
        self.in_combo.set('')
        self.in_entry.delete(0, 'end')
        self.agg_combo.set('')
        self.ope_combo.set('')
        self.condition_entry.delete(0, 'end')
        self.groupby_combo.set('')
        self.havcol_combo.set('')
    
    def exist_display(self):
        self.exist_label = tk.Label(self.window, text='EXIST', font=self.font_style, background='pale green')
        self.exist_label.place(x=100, y=400, height=30, width=75)
        self.exist_combo = ttk.Combobox(self.window, font=self.font_style, values=['EXISTS', 'NOT EXISTS'])        
        self.exist_combo.place(x=200, y=400, height=30, width=100)
        self.exist_button = tk.Button(self.window, text='Send', command=self.exist_func, font=self.font_style)
        self.exist_button.place(x=720, y=400, height=30, width=60)
        self.exist_button.config(background='medium spring green')
        self.equal_label = tk.Label(self.window, text='=', font=self.font_style, background='pale green')
        self.equal_label.place(x=550, y=400, height=30, width=30)

        # Display select table
        self.cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
        table_name = self.cursor.fetchall()
        self.select_table_combo = ttk.Combobox(self.window, font=self.font_style, 
                                                values=[table_name[i][2] for i in range(len(table_name))])          
        self.select_table_combo.place(x=310, y=400, height=30, width=100)
        self.select_table_combo.bind("<<ComboboxSelected>>", self.create_column_combo)
        
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        current_table_columns = self.cursor.fetchall()
        self.current_columns_combo = ttk.Combobox(self.window, font=self.font_style, 
                                                    values=[current_table_columns[i][0] for i in range(len(current_table_columns))])          
        self.current_columns_combo.place(x=590, y=400, height=30, width=120)            
            
    def exist_func(self):
        self.listBox.delete(*self.listBox.get_children())
        self.cursor.execute(f'SELECT * FROM {self.table_combo.get()} \
                    WHERE {self.exist_combo.get()} \
                    (SELECT * FROM {self.select_table_combo.get()} \
                        WHERE {self.table_combo.get()}.{self.current_columns_combo.get()}={self.select_table_combo.get()}.{self.select_columns_combo.get()})')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
        self.status_label.configure(text = '')
        self.status_label.configure(background = 'white')            
            
    def create_column_combo(self, event):
        self.cursor.execute(f'SHOW COLUMNS FROM {self.select_table_combo.get()}')
        select_table_columns = self.cursor.fetchall()
        self.select_columns_combo['values'] = [select_table_columns[i][0] for i in range(len(select_table_columns))]

    def in_display(self):
        self.nested_label = tk.Label(self.window, text='Nested', font=self.font_style, background='pale green')
        self.nested_label.place(x=20, y=360, height=70, width=75)
        self.in_label = tk.Label(self.window, text='IN', font=self.font_style, background='pale green')
        self.in_label.place(x=100, y=360, height=30, width=75)
        self.in_combo = ttk.Combobox(self.window, font=self.font_style, values=['IN', 'NOT IN'])        
        self.in_combo.place(x=380, y=360, height=30, width=90)
        self.in_entry = tk.Entry(self.window, font=self.font_style)
        self.in_entry.place(x=500, y=360, height=30, width=210)
        self.in_button = tk.Button(self.window, text='Send', command=self.in_func, font=self.font_style)
        self.in_button.place(x=720, y=360, height=30, width=60)
        self.in_button.config(background='medium spring green')
        # Display select table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        table_columns = self.cursor.fetchall()
        self.column_combo = ttk.Combobox(self.window, font=self.font_style,
                                            values=[table_columns[i][0] for i in range(len(table_columns))])        
        self.column_combo.place(x=200, y=360, height=30, width=150)                       

    def in_func(self):
        self.listBox.delete(*self.listBox.get_children())
        self.cursor.execute(f'SELECT * FROM {self.table_combo.get()} \
                    WHERE {self.column_combo.get()} {self.in_combo.get()} ({self.in_entry.get()})')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
        self.status_label.configure(text = '')
        self.status_label.configure(background = 'white')            
        
    def having_display(self):   
        self.groupby_label = tk.Label(self.window, text='Grouped by', font=self.font_style, background='light salmon')
        self.groupby_label.place(x=20, y=260, height=30, width=150)
        self.having_label = tk.Label(self.window, text='Having', font=self.font_style, background='light salmon')
        self.having_label.place(x=20, y=300, height=30, width=150)
        self.ope_combo = ttk.Combobox(self.window, values=['>', '<', '=', '>=', '<='], font=self.font_style)        
        self.ope_combo.place(x=510, y=300, height=30, width=50)
        self.condition_entry = tk.Entry(self.window, font=self.font_style)
        self.condition_entry.place(x=590, y=300, height=30, width=120)
        self.having_button = tk.Button(self.window, text='Send', command=self.having_func, font=self.font_style)
        self.having_button.place(x=720, y=260, height=70, width=60)
        self.having_button.config(background='salmon')
        # Display select table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        table_columns = self.cursor.fetchall()
        self.groupby_combo = ttk.Combobox(self.window, font=self.font_style,
                                            values=[table_columns[i][0] for i in range(len(table_columns))])        
        self.groupby_combo.place(x=200, y=260, height=30, width=200)
        
        self.havcol_combo = ttk.Combobox(self.window, font=self.font_style,
                                            values=[table_columns[i][0] for i in range(len(table_columns))])        
        self.havcol_combo.place(x=200, y=300, height=30, width=150)  
        self.havcol_combo.bind("<<ComboboxSelected>>", self.create_agg_combo)
        
    def having_func(self):
        self.listBox.delete(*self.listBox.get_children())
        
        self.cursor.execute(f'SELECT {self.groupby_combo.get()}, {self.agg_combo.get()}({self.havcol_combo.get()})\
                    FROM {self.table_combo.get()} \
                    GROUP BY {self.groupby_combo.get()} \
                    HAVING {self.agg_combo.get()}({self.havcol_combo.get()}) {self.ope_combo.get()} {self.condition_entry.get()}')
        table_result = self.cursor.fetchall()
        # Reset listbox
        list_column = [self.groupby_combo.get(), f'{self.agg_combo.get()}({self.havcol_combo.get()})']
        self.listBox.config(columns=list_column)
        for i in range(len(list_column)):
            self.listBox.heading(i, text=list_column[i])
            self.listBox.column(i, stretch='True', anchor='center', width='380')
        # Display having result
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
        self.status_label.configure(text = '')
        self.status_label.configure(background = 'white')
            
    def create_agg_combo(self, event):
        # Display select table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        table_columns = self.cursor.fetchall()
        
        # Find int column
        int_column = []
        for i in range(len(table_columns)):
            if table_columns[i][1]=='int':
                int_column.append(table_columns[i][0])  
                
        if self.havcol_combo.get() in int_column: 
            self.agg_combo['values'] = ['Sum', 'Max', 'Min', 'Avg', 'Count']
        else:
            self.agg_combo['values'] = ['Count']
            
    def aggregate(self):
        AggregateInterface(self.connection, self.cursor, self.font_style, self.table_combo.get())

    def insert(self):
        insert_value = []
        for i in range(len(self.entry)):
            insert_value.append(self.entry[i].get())
        self.cursor.execute(f'INSERT INTO {self.table_combo.get()} VALUES{tuple(insert_value)}')  
        self.connection.commit()
        self.listBox.insert('', tk.END, text=str(self.cursor.lastrowid), values=tuple(insert_value))
        self.update_listbox()
        
    def delete(self):
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        delete_value = {}
        condition = ''
        table_columns = self.cursor.fetchall()
        for i in range(len(table_columns)):
            delete_value[table_columns[i][0]] = self.entry[i].get()
            if delete_value[table_columns[i][0]] != '' and condition=='':
                condition = condition + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
            elif delete_value[table_columns[i][0]] != '':
                condition = condition + ' AND ' + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
        self.cursor.execute(f'DELETE FROM {self.table_combo.get()} WHERE {condition}')  
        self.connection.commit()
        # except:
        #     warning_window = tk.Toplevel()
        #     warning_window.wm_title("Warning")
        #     warning_window.geometry('500x100')
        #     warning_window.configure(background='white')
        #     warning_label = tk.Label(warning_window, 
        #                              text='Please enter condition for deletion!', font=self.font_style)
        #     warning_label.configure(background = 'white')
        #     warning_label.place(x=20, y=20, width=460)
        self.update_listbox()
    
    def update(self):
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        update_value = {}
        condition = ''
        table_columns = self.cursor.fetchall()
        for i in range(1, len(table_columns)):
            update_value[table_columns[i][0]] = self.entry[i].get()
            if condition=='':
                condition = condition + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
            elif update_value[table_columns[i][0]] != '':
                condition = condition + ', ' + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
        self.cursor.execute(f'UPDATE {self.table_combo.get()} SET {condition} WHERE {table_columns[0][0]}="{self.entry[0].get()}"')
        self.connection.commit()
        self.update_listbox()
    
    def on_listbox_select(self, event):
        try:
            select_value = self.listBox.item(self.listBox.selection(), 'values')
            for i in range(len(self.entry)):
                self.entry[i].delete(0, 'end')
                self.entry[i].insert(0, select_value[i])
        except:
            warning_window = tk.Toplevel()
            warning_window.wm_title("Warning")
            warning_window.geometry('500x100')
            warning_window.configure(background='white')
            warning_label = tk.Label(warning_window, 
                                     text='[Not allowed] More than one tuples are choosen!', font=self.font_style)
            warning_label.configure(background = 'white')
            warning_label.place(x=20, y=20, width=460)
            
    def update_listbox(self):
        self.listBox.delete(*self.listBox.get_children())
        # Display select table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        table_columns = self.cursor.fetchall()
        self.listBox.config(columns=table_columns)
        for i in range(len(table_columns)):
            self.listBox.heading(i, text=table_columns[i][0])
            self.listBox.column(i, stretch='True', anchor='center', width='190')
        self.cursor.execute(f'SELECT * FROM {self.table_combo.get()}')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)
      
class QueryInterface(object):
    def __init__(self, connection, cursor, font_style):
        self.connection = connection
        self.cursor = cursor
        self.font_style = font_style
        
        window= tk.Toplevel()
        window.wm_title("Query Interface")
        window.geometry('800x600')
        window.configure(background='white')
        self.font_style = font.Font(family='Calibri', size=15)
        
        # Query field
        self.query_label = tk.Label(window, text="Query", font=self.font_style)
        self.query_label.place(x=20, y=70, height=100, width=100)
        self.query_label.config(background='gray80')
        self.query_entry = ScrolledText(window)
        self.query_entry.place(x=120, y=70, height=100, width=660)
        
        # Query button
        self.query_button = tk.Button(window, text="Send Query", font=self.font_style, command=self.send_query)
        self.query_button.place(x=20, y=170, width=760)
        
        # Query status
        self.status_label = tk.Label(window, text='', font=self.font_style)
        self.status_label.configure(background = 'white')
        self.status_label.place(x=20, y=220, width=760)
        
        # Result field
        self.result = tk.Label(window, text='Result', font=self.font_style)
        self.result.place(x=20, y=270, width=760)
        self.result.config(background='gray80')
        self.listBox = ttk.Treeview(window, show='headings')
        self.listBox.place(x=20, y=300, height=200, width=760)
        ## Rolling bar
        ### y-axis
        self.yscroll = ttk.Scrollbar(window, orient=tk.VERTICAL, command=self.listBox.yview)
        self.listBox.configure(yscrollcommand = self.yscroll.set)
        self.yscroll.place(x=780, y=300, height=180)
        ### x-axis
        self.xscroll = ttk.Scrollbar(window, orient=tk.HORIZONTAL, command=self.listBox.xview)
        self.listBox.configure(xscrollcommand = self.xscroll.set)
        self.xscroll.place(x=20, y=500, width=760)
        
    def send_query(self):
        self.listBox.delete(*self.listBox.get_children())
        # Setting the query
        self.query = self.query_entry.get('1.0', tk.END)
        # Send select statement
        self.cursor.execute(self.query)
        self.connection.commit()
        # # Display select table
        # table_columns = self.cursor.description
        # self.listBox.config(columns=table_columns)
        # for i in range(len(table_columns)):
        #     self.listBox.heading(i, text=table_columns[i][0])
        #     self.listBox.column(i, stretch='True', anchor='center', width='190')
        
        # table_result = self.cursor.fetchall()
        # if table_result:
        #     for row in table_result:
        #         self.listBox.insert('', 'end', values=row)
        
        # self.status_label.configure(text = 'Query Success')
        # self.status_label.configure(background = 'chartreuse3', fg='white')
        # except:
        #     self.status_label.configure(text = 'Query Failed')
        #     self.status_label.configure(background = 'orange red', fg='white')
        
class DatabaseInterface(object):
    def __init__(self, window, connection, cursor):
        self.connection = connection
        self.cursor = cursor

        # Set the window title 
        window.wm_title("Database Interface")
        window.geometry('800x200')
        window.configure(background='white')
        self.font_style = font.Font(family='Calibri', size=15)
        
        # Select button
        self.query_button = tk.Button(window, text="Query", font=self.font_style, command=self.query)
        self.query_button.place(x=275, y=100)
        self.button_button = tk.Button(window, text="Button", font=self.font_style, command=self.button)
        self.button_button.place(x=425, y=100)
        
        self.choose_label = tk.Label(window, text="Please choose a way for SQL:", font=self.font_style)
        self.choose_label.place(x=190, y=40, width=400)
        self.choose_label.configure(background='white')
    
    def query(self):
        QueryInterface(self.connection, self.cursor, self.font_style)
        
    def button(self):
        ButtonInterface(self.connection, self.cursor, self.font_style)

            
<<<<<<< HEAD:interface.py
=======
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
    main(ip ='localhost', user ='root', password ='red91310', database = 'delivery_db')
>>>>>>> 8eadc98 (Rename a function name):DBMS.py
