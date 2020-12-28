import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.scrolledtext import ScrolledText

from window import Window
from insert_func import InsertFunc
from delete_func import DeleteFunc
from update_func import UpdateFunc
from exist_window import ExistWindow
from in_window import InWindow
from having_window import HavingWindow
from aggregate_window import AggregateWindow


class DatabaseWindow(object):
    def __init__(self, window, connection, cursor):
        self.connection = connection
        self.cursor = cursor

        # Set the window title
        window.wm_title('Database Interface')
        window.geometry('800x200')
        window.configure(background='white')
        self.font_style = font.Font(family='Calibri', size=15)

        # Select button
        self.query_button = tk.Button(
            window, text='Query', font=self.font_style, command=self.query)
        self.query_button.place(x=275, y=100)
        self.button_button = tk.Button(
            window, text='Button', font=self.font_style, command=self.button)
        self.button_button.place(x=425, y=100)

        self.choose_label = tk.Label(
            window, text='Please choose a way for SQL:', font=self.font_style)
        self.choose_label.place(x=190, y=40, width=400)
        self.choose_label.configure(background='white')

    def query(self):
        QueryWindow(self.connection, self.cursor, self.font_style)

    def button(self):
        ButtonWindow(self.connection, self.cursor, self.font_style)


class QueryWindow(Window):
    def __init__(self, connection, cursor, font_style):
        super().__init__(connection, cursor, font_style)
        self.window.wm_title('Query Interface')
        self.window.geometry('800x600')

        # Query field
        self.query_label = tk.Label(
            self.window, text='Query', font=self.font_style)
        self.query_label.place(x=20, y=120, height=100, width=100)
        self.query_label.config(background='gray80')
        self.query_entry = ScrolledText(self.window)
        self.query_entry.place(x=120, y=120, height=100, width=660)

        # Query status
        self.status_label = tk.Label(
            self.window, text='', font=self.font_style)
        self.status_label.configure(background='white')
        self.status_label.place(x=20, y=270, height=30, width=760)

        # Decide the position
        # Result field
        self.result.place(x=20, y=320, width=760)
        self.listBox.place(x=20, y=350, height=200, width=760)
        self.yscroll.place(x=780, y=350, height=180)
        self.xscroll.place(x=20, y=550, width=760)
        # Query button
        self.query_button.place(x=720, y=60, height=30, width=60)

    def send_query(self):
        try:
            # Setting the query
            self.query = self.query_entry.get('1.0', tk.END)
            # Send select statement
            self.display_result(self.query)
            self.connection.commit()
            self.status_label.configure(text='Query Success')
            self.status_label.configure(background='chartreuse3', fg='white')
        except:
            self.status_label.configure(text='Query Failed')
            self.status_label.configure(background='orange red', fg='white')

    def clean_value(self):
        self.query_entry.delete('1.0', tk.END)


class ButtonWindow(Window):
    def __init__(self, connection, cursor, font_style):
        super().__init__(connection, cursor, font_style)
        self.window.wm_title('Button Interface')
        self.window.geometry('800x700')

        # Decide the position
        # Result field
        self.result.place(x=20, y=440, width=760)
        self.listBox.place(x=20, y=470, height=200, width=760)
        self.listBox.bind("<<TreeviewSelect>>", self.on_listbox_select)
        self.yscroll.place(x=780, y=470, height=180)
        self.xscroll.place(x=20, y=670, width=760)
        # Query button
        self.query_button.place(x=720, y=220, height=50, width=60)

        # Function file
        function_label = tk.Label(
            self.window, text="Function", font=self.font_style, background='goldenrod1')
        function_label.place(x=20, y=220, height=50, width=150)

        self.insert_button = tk.Button(
            self.window, text="Insert", font=self.font_style, command=self.insert_func)
        self.insert_button.place(x=200, y=220, height=50, width=100)
        self.insert_button.config(background='Gold')
        self.insert_button.config(state='disable')

        self.delete_button = tk.Button(
            self.window, text="Delete", font=self.font_style, command=self.delete_func)
        self.delete_button.place(x=330, y=220, height=50, width=100)
        self.delete_button.config(background='Gold')
        self.delete_button.config(state='disable')

        self.update_button = tk.Button(
            self.window, text="Update", font=self.font_style, command=self.update_func)
        self.update_button.place(x=460, y=220, height=50, width=100)
        self.update_button.config(background='Gold')
        self.update_button.config(state='disable')

        self.aggregate_button = tk.Button(
            self.window, text="Aggregate", font=self.font_style, command=self.aggregate)
        self.aggregate_button.place(x=590, y=220, height=50, width=100)
        self.aggregate_button.config(background='Gold')
        self.aggregate_button.config(state='disable')

        self.exist_display()
        self.in_display()
        self.having_display()

        # Condition field
        self.condition_label = tk.Label(self.window, font=self.font_style)
        self.condition_label.place(x=20, y=90, height=30, width=760)
        self.condition_label.config(background='white')
        self.column_label = []
        self.entry = []

    def initial_gui(self):
        # Get columns of the selected table
        self.cursor.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
        self.table_columns = self.cursor.fetchall()

        # Enable condition field
        self.condition_label.configure(text='Condition', background='gray80')
        self.clean_value()  # Clean previous value
        for i in range(len(self.table_columns)):
            self.column_label.append(
                tk.Label(self.window, text=self.table_columns[i][0], font=self.font_style))
            self.column_label[i].place(
                x=20+190*(i), y=120, height=30, width=190)
            self.entry.append(
                tk.Entry(self.window, textvariable=tk.StringVar(), font=self.font_style))
            self.entry[i].place(x=20+190*(i), y=150, height=40, width=190)

        # Enable function buttons
        self.insert_button.config(state='normal')
        self.delete_button.config(state='normal')
        self.update_button.config(state='normal')
        self.aggregate_button.config(state='normal')
        # Activate having_button only if there is column in int type
        for i in range(len(self.table_columns)):
            if self.table_columns[i][1] == 'int':
                self.having_button.config(state='normal')

        # Show record in result field
        self.display_result(f'SELECT * FROM {self.table_combo.get()}')

    def clean_value(self):
        for i in range(len(self.column_label)):
            self.column_label[i].destroy()
        self.column_label = []
        for i in range(len(self.entry)):
            self.entry[i].delete(0, 'end')
        self.entry = []

    def send_query(self):
        self.listBox.delete(*self.listBox.get_children())
        select_value = {}
        condition = ''
        for i in range(len(self.table_columns)):
            select_value[self.table_columns[i][0]] = self.entry[i].get()
            if select_value[self.table_columns[i][0]] != '' and condition == '':
                condition = condition + \
                    str(f'{self.table_columns[i][0]}="{self.entry[i].get()}"')
            elif select_value[self.table_columns[i][0]] != '':
                condition = condition + ' AND ' + \
                    str(f'{self.table_columns[i][0]}="{self.entry[i].get()}"')
        self.cursor.execute(
            f'SELECT * FROM {self.table_combo.get()} WHERE {condition}')
        table_result = self.cursor.fetchall()
        if table_result:
            for row in table_result:
                self.listBox.insert('', 'end', values=row)

    def insert_func(self):
        InsertFunc(self)

    def delete_func(self):
        DeleteFunc(self)

    def update_func(self):
        UpdateFunc(self)

    def exist_display(self):
        self.exist_button = tk.Button(
            self.window, text='Exist', command=self.exist_func, font=self.font_style)
        self.exist_button.place(x=150, y=320, height=50, width=100)
        self.exist_button.config(background='medium spring green')

    def exist_func(self):
        ExistWindow(self.connection, self.cursor, self.font_style)

    def in_display(self):
        self.in_button = tk.Button(
            self.window, text='IN', command=self.in_func, font=self.font_style)
        self.in_button.place(x=350, y=320, height=50, width=100)
        self.in_button.config(background='medium spring green')

    def in_func(self):
        InWindow(self.connection, self.cursor, self.font_style)

    def having_display(self):
        self.having_button = tk.Button(
            self.window, text='Having', command=self.having_func, font=self.font_style)
        self.having_button.place(x=550, y=320, height=50, width=100)
        self.having_button.config(background='salmon')
        # Default state of having_button is disable
        self.having_button.config(state='disable')

    def having_func(self):
        HavingWindow(self.connection, self.cursor, self.font_style)

    def aggregate(self):
        AggregateWindow(self.connection, self.cursor, self.font_style)

    def on_listbox_select(self, event):
        try:
            select_value = self.listBox.item(
                self.listBox.selection(), 'values')
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
            warning_label.configure(background='white')
            warning_label.place(x=20, y=20, width=460)
