import tkinter as tk
from tkinter import ttk

class SubWindow(object):

    def __init__(self, connection, cursor, font_style):
        self.connection = connection
        self.cursor = cursor
        self.font_style = font_style
        
        # Create window
        self.window= tk.Toplevel()
        self.window.configure(background='white')

        # Table combobox
        self.combo_label = tk.Label(self.window, text="Table", font=self.font_style)
        self.combo_label.place(x=20, y=20, height=30, width=100)
        self.combo_label.config(background='gray80')
        self.cursor.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
        table_name = self.cursor.fetchall()
        self.table_combo = ttk.Combobox(self.window, font=self.font_style,
                                        values=[table_name[i][2] for i in range(len(table_name))])
        self.table_combo.place(x=120, y=20, height=30, width=200)
        self.table_combo.bind("<<ComboboxSelected>>", self.table_selected) 

        # Result field
        self.result = tk.Label(self.window, text='Result', font=self.font_style)
        self.result.config(background='gray80')
        self.listBox = ttk.Treeview(self.window, show='headings')
        ## Rolling bar
        ### y-axis
        self.yscroll = ttk.Scrollbar(self.window, orient=tk.VERTICAL, command=self.listBox.yview)
        self.listBox.configure(yscrollcommand = self.yscroll.set)
        ### x-axis
        self.xscroll = ttk.Scrollbar(self.window, orient=tk.HORIZONTAL, command=self.listBox.xview)
        self.listBox.configure(xscrollcommand = self.xscroll.set)
        
        # Send query button
        self.query_button = tk.Button(self.window, text='Query', command=self.send_query, font=self.font_style)
        self.query_button.configure(background='light sky blue')

        # Clean input
        self.clean_button = tk.Button(self.window, text="Clean", font=self.font_style, command=self.clean_value)
        self.clean_button.place(x=630, y=20, height=30, width=150)
        self.clean_button.configure(background='white')

    def table_selected(self, event):
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        self.table_columns = self.cursor.fetchall()
        self.display_result(f'SELECT * FROM {self.table_combo.get()}')
        self.initial_gui()

    def initial_gui(self):
        pass

    def display_result(self, query):
        # Display columns
        self.cursor.execute(query)
        table_columns = self.cursor.description
        self.listBox.config(columns=table_columns)
        for i in range(len(table_columns)):
            self.listBox.heading(i, text=table_columns[i][0])
            self.listBox.column(i, stretch='True', anchor='center', width='190')
        # Display result
        self.listBox.delete(*self.listBox.get_children())
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)

    def send_query(self):
        pass
    
    def clean_value(self):
        pass
    
        