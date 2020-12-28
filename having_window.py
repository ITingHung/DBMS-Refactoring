import tkinter as tk
from tkinter import ttk

from window import Window


class HavingWindow(Window):
    def __init__(self, connection, cursor, font_style):
        super().__init__(connection, cursor, font_style)
        self.window.wm_title('Group by, having')
        self.window.geometry('800x400')

        # Condition field
        self.groupby_label = tk.Label(
            self.window, text='Grouped by', font=self.font_style, background='light salmon')
        self.groupby_label.place(x=20, y=60, height=30, width=150)
        self.having_label = tk.Label(
            self.window, text='Having', font=self.font_style, background='light salmon')
        self.having_label.place(x=20, y=100, height=30, width=150)
        self.ope_combo = ttk.Combobox(
            self.window, values=['>', '<', '=', '>=', '<='], font=self.font_style)
        self.ope_combo.place(x=510, y=100, height=30, width=50)
        self.condition_entry = tk.Entry(self.window, font=self.font_style)
        self.condition_entry.place(x=590, y=100, height=30, width=120)
        self.agg_combo = ttk.Combobox(self.window, font=self.font_style)
        self.agg_combo.place(x=380, y=100, height=30, width=100)

        # Decide the position
        # Result field
        self.result.place(x=20, y=140, width=760)
        self.listBox.place(x=20, y=170, height=200, width=760)
        self.xscroll.place(x=20, y=370, width=760)
        self.yscroll.place(x=780, y=170, height=180)
        # Query button
        self.query_button.place(x=720, y=60, height=30, width=60)

    def initial_gui(self):
        self.groupby_combo = ttk.Combobox(self.window, font=self.font_style,
                                          values=[self.table_columns[i][0] for i in range(len(self.table_columns))])
        self.groupby_combo.place(x=200, y=60, height=30, width=200)
        self.havcol_combo = ttk.Combobox(self.window, font=self.font_style,
                                         values=[self.table_columns[i][0] for i in range(len(self.table_columns))])
        self.havcol_combo.place(x=200, y=100, height=30, width=150)
        self.havcol_combo.bind("<<ComboboxSelected>>", self.create_agg_combo)

    def create_agg_combo(self, event):
        # Display select table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        self.table_columns = self.cursor.fetchall()

        # Find int column
        int_column = []
        for i in range(len(self.table_columns)):
            if self.table_columns[i][1] == 'int':
                int_column.append(self.table_columns[i][0])

        if self.havcol_combo.get() in int_column:
            self.agg_combo['values'] = ['Sum', 'Max', 'Min', 'Avg', 'Count']
        else:
            self.agg_combo['values'] = ['Count']

    def send_query(self):
        query = f'SELECT {self.groupby_combo.get()}, {self.agg_combo.get()}({self.havcol_combo.get()})\
                  FROM {self.table_combo.get()} \
                  GROUP BY {self.groupby_combo.get()} \
                  HAVING {self.agg_combo.get()}({self.havcol_combo.get()}) {self.ope_combo.get()} {self.condition_entry.get()}'
        self.display_result(query)

        # Reset listbox's column
        list_column = [self.groupby_combo.get(
        ), f'{self.agg_combo.get()}({self.havcol_combo.get()})']
        self.listBox.config(columns=list_column)
        for i in range(len(list_column)):
            self.listBox.heading(i, text=list_column[i])
            self.listBox.column(i, stretch='True',
                                anchor='center', width='380')

    def clean_value(self):
        self.agg_combo.set('')
        self.ope_combo.set('')
        self.condition_entry.delete(0, 'end')
        self.groupby_combo.set('')
        self.havcol_combo.set('')
