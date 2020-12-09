# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 13:25:22 2020

@author: user
"""
# https://www.w3schools.com/python/python_mysql_create_db.asp

import pymysql
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.scrolledtext import ScrolledText

# # Create database
# connection = pymysql.connect(host='localhost',
#                               user='root',
#                               password='red91310',
#                               charset='utf8mb4',
#                               cursorclass=pymysql.cursors.DictCursor)
# try:
#     with connection.cursor() as cursor: 
#         cursor.execute("CREATE DATABASE IF NOT EXISTS delivery_db")
# finally:
#         cursor.close()

# Create table to database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='red91310',
                             db = 'delivery_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)    

# create table
try:
    with connection.cursor() as cursor:
        # Read a single record
        customer_table = '''CREATE TABLE IF NOT EXISTS Customer(Phone VARCHAR(20) PRIMARY KEY,
                                                                BirthDate VARCHAR(10) NOT NULL,
                                                                Gender VARCHAR(2) NOT NULL,
                                                                City VARCHAR(20) NOT NULL)'''
        
        platform_table = '''CREATE TABLE IF NOT EXISTS Platform(Name VARCHAR(100) PRIMARY KEY,
                                                                Employee_number INT NOT NULL,
                                                                Capital INT NOT NULL,
                                                                Country VARCHAR(20) NOT NULL)'''
    
        deliver_table = '''CREATE TABLE IF NOT EXISTS Deliver(ID VARCHAR(20) PRIMARY KEY,
                                                              Gender VARCHAR(2) NOT NULL,
                                                              Tenure INT NOT NULL,
                                                              Platform_name VARCHAR(100) NOT NULL,
                                                              FOREIGN KEY (Platform_name) REFERENCES Platform(Name))'''
        
        shop_table = '''CREATE TABLE IF NOT EXISTS Shop(Name VARCHAR(100) PRIMARY KEY,
                                                        Employee_number INT NOT NULL,
                                                        Country VARCHAR(20) NOT NULL,
                                                        Platform_name VARCHAR(100) NOT NULL,
                                                        FOREIGN KEY (Platform_name) REFERENCES Platform(Name))'''
        
        car_table = '''CREATE TABLE IF NOT EXISTS Car(Plate_Number VARCHAR(20) PRIMARY KEY,
                                                      Type VARCHAR(20) NOT NULL,
                                                      Year INT NOT NULL,
                                                      Platform_name VARCHAR(100) NOT NULL,
                                                      FOREIGN KEY (Platform_name) REFERENCES Platform(Name))'''
        
        car_deliver_table = '''CREATE TABLE IF NOT EXISTS Car_Deliver(D_ID VARCHAR(20) NOT NULL,
                                                                      C_Plate_Number VARCHAR(20) NOT NULL,
                                                                      PRIMARY KEY (D_ID, C_Plate_Number),
                                                                      FOREIGN KEY (D_ID) REFERENCES Deliver(ID),
                                                                      FOREIGN KEY (C_Plate_Number) REFERENCES Car(Plate_Number))'''
       
        order_table = '''CREATE TABLE IF NOT EXISTS Order_record(Cus_Phone VARCHAR(20) NOT NULL,
                                                                 D_ID VARCHAR(20) NOT NULL,
                                                                 S_Name VARCHAR(100) NOT NULL,
                                                                 C_Plate_Number VARCHAR(20) NOT NULL,
                                                                 PRIMARY KEY (Cus_Phone, D_ID, S_Name, C_Plate_Number),
                                                                 FOREIGN KEY (Cus_Phone) REFERENCES Customer(Phone),
                                                                 FOREIGN KEY (D_ID) REFERENCES Deliver(ID),
                                                                 FOREIGN KEY (S_Name) REFERENCES Shop(Name),
                                                                 FOREIGN KEY (C_Plate_Number) REFERENCES Car(Plate_Number))'''

        cursor.execute(customer_table)
        cursor.execute(platform_table)
        cursor.execute(deliver_table)
        cursor.execute(shop_table)
        cursor.execute(car_table)
        cursor.execute(car_deliver_table)    
        cursor.execute(order_table)    
        # cursor.execute('TRUNCATE TABLE Car_Deliver') 
        # cursor.execute('TRUNCATE TABLE Order')     
        # cursor.execute('TRUNCATE TABLE Customer')    
        # cursor.execute('TRUNCATE TABLE Deliver')    
        # cursor.execute('TRUNCATE TABLE Shop')    
        # cursor.execute('TRUNCATE TABLE Car')    
        # cursor.execute('TRUNCATE TABLE Platform') 
        
        # cus_sql = 'INSERT INTO Customer (Phone, BirthDate, Gender, City) VALUES (%s, %s, %s, %s)'
        # cus_val = [('0978-238-506', '1997-02-23', 'F', 'Tainan'), 
        #            ('0935-508-785', '1998-12-02', 'M', 'Tainan'),
        #            ('0921-656-779', '1996-10-15', 'F', 'Taipei'),
        #            ('0934-556-888', '1996-05-05', 'F', 'Kaohsiung'),
        #            ('0929-335-678', '1997-02-23', 'M', 'Tainan'),
        #            ('0926-313-565', '1998-07-31', 'F', 'Taichung'),
        #            ('0926-457-889', '1995-10-26', 'M', 'Taichung'),
        #            ('0978-122-356', '1996-04-26', 'F', 'Kaohsiung'),
        #            ('0933-377-688', '1996-06-29', 'F', 'Tainan'),
        #            ('0923-234-665', '1996-05-05', 'M', 'Tainan')]
        # cursor.executemany(cus_sql, cus_val)
        
        # pla_sql = 'INSERT INTO Platform (Name, Employee_number, Capital, Country) VALUES (%s, %s, %s, %s)'
        # pla_val = [('Books', '310', '10000', 'Taiwan'), 
        #            ('YourStyle', '125', '3000', 'America'),
        #            ('UberEat', '620', '5500', 'America'),
        #            ('Yummy', '255', '90000', 'Japan'),
        #            ('FoodPanda', '620', '3000', 'Taiwan'),
        #            ('Foodyy', '56', '2000', 'Japan'),
        #            ('3C Shop', '79', '5500', 'America'),
        #            ('Pinkoi', '125', '8100', 'Taiwan'),
        #            ('Taobao', '875', '20000', 'China'),
        #            ('Shopee', '1021', '3000', 'China')]
        # cursor.executemany(pla_sql, pla_val)

        # del_sql = 'INSERT INTO Deliver (ID, Gender, Tenure, Platform_name) VALUES (%s, %s, %s, %s)'
        # del_val = [('001', 'F', '10', 'Books'), 
        #            ('002', 'M', '8', 'Books'),
        #            ('003', 'F', '5', 'Books'),
        #            ('004', 'M', '3', 'Books'),
        #            ('005', 'M', '3', 'YourStyle'),
        #            ('006', 'F', '5', 'YourStyle'),
        #            ('007', 'M', '10', 'YourStyle'),
        #            ('008', 'F', '3', 'UberEat'),
        #            ('009', 'F', '3', 'UberEat'),
        #            ('010', 'M', '3', 'UberEat'),
        #            ('011', 'M', '5', 'Yummy'),
        #            ('012', 'F', '3', 'Yummy'),
        #            ('013', 'M', '1', 'FoodPanda'),
        #            ('014', 'M', '1', 'FoodPanda'),
        #            ('015', 'M', '7', 'Foodyy'),
        #            ('016', 'M', '1', '3C Shop'),
        #            ('017', 'F', '5', 'Pinkoi'),
        #            ('018', 'M', '3', 'Pinkoi'),
        #            ('019', 'M', '7', 'Taobao'),
        #            ('020', 'M', '4', 'Shopee'),
        #            ('021', 'M', '5', 'Shopee')]
                   
        # cursor.executemany(del_sql, del_val)
        
        # sho_sql = 'INSERT INTO Shop (Name, Employee_number, Country, Platform_name) VALUES (%s, %s, %s, %s)'
        # sho_val = [('Muji', '50', 'Taipei', 'Books'), 
        #            ('Uniqlo', '1325', 'Tainan', 'YourStyle'),
        #            ('Net', '586', 'Tainan', 'YourStyle'),
        #            ('Lativ', '50', 'Taiana', 'YourStyle'),
        #            ('McDonald', '3120', 'Tainan', 'UberEat'),
        #            ('MosBurger', '1325', 'Tainan', 'Yummy'),
        #            ('Louisa', '2000', 'Taipei', 'FoodPanda'),
        #            ('CakeBakery', '120', 'Taipei', 'Foodyy'),
        #            ('Donutes', '120', 'Taipei', 'Foodyy'),
        #            ('Apple', '7625', 'Taipei', '3C Shop'),
        #            ('Acer', '3120', 'Kaohsiung', '3C Shop'),
        #            ('YourDesign', '5', 'Taipei', 'Pinkoi'),
        #            ('Nike', '2000', 'Kaohsiung', 'Taobao'),
        #            ('Skechers', '2000', 'Tainan', 'Taobao'),
        #            ('QueenShop', '120', 'Tainan', 'Shopee')]
        
        # cursor.executemany(sho_sql, sho_val)
        
        # car_sql = 'INSERT INTO Car (Plate_Number, Type, Year, Platform_name) VALUES (%s, %s, %s, %s)'
        # car_val = [('ZY-056', 'Truck', '10', 'Books'),
        #            ('GH-011', 'Van', '3', 'Books'),
        #            ('AZ-088', 'Truck', '5', 'YourStyle'),
        #            ('ZY-022', 'Van', '5', 'YourStyle'),
        #            ('GH-015', 'Truck', '1', 'YourStyle'),
        #            ('AB-026', 'Van', '10', 'UberEat'),
        #            ('GH-091', 'Van', '1', 'UberEat'),
        #            ('FQ-091', 'Van', '5', 'UberEat'),
        #            ('FQ-033', 'Van', '1', 'Yummy'),
        #            ('TY-085', 'Van', '3', 'FoodPanda'),
        #            ('AB-062', 'Van', '3', 'FoodPanda'),
        #            ('AB-027', 'Van', '3', 'Foodyy'),
        #            ('AB-051', 'Van', '5', 'Foodyy'),
        #            ('EJ-035', 'Truck', '7', '3C Shop'),
        #            ('CQ-015', 'Truck', '5', 'Pinkoi'),
        #            ('AB-013', 'Van', '3', 'Pinkoi'),
        #            ('AB-011', 'Truck', '10', 'Taobao'),
        #            ('AB-096', 'Truck', '7', 'Shopee'),
        #            ('ZY-045', 'Truck', '1', 'Shopee')]
        # cursor.executemany(car_sql, car_val)
        
        # car_del_sql = 'INSERT INTO Car_Deliver (D_ID, C_Plate_Number) VALUES (%s, %s)'
        # car_del_val = [('001', 'ZY-056'), ('001', 'GH-011'),
        #                ('002', 'ZY-056'), ('002', 'GH-011'),
        #                ('003', 'ZY-056'),
        #                ('004', 'GH-011'),
        #                ('005', 'AZ-088'), ('005', 'GH-015'),
        #                ('006', 'ZY-022'),
        #                ('007', 'AZ-088'), ('007', 'GH-015'),
        #                ('008', 'AB-026'),
        #                ('009', 'GH-091'),
        #                ('010', 'FQ-091'),
        #                ('011', 'FQ-033'),
        #                ('012', 'FQ-033'),
        #                ('013', 'TY-085'), ('013', 'AB-062'),
        #                ('014', 'TY-085'), ('014', 'AB-062'),
        #                ('015', 'AB-027'), ('015', 'AB-051'),
        #                ('016', 'EJ-035'),
        #                ('017', 'CQ-015'),
        #                ('018', 'AB-013'),
        #                ('019', 'AB-011'),
        #                ('020', 'AB-096'),
        #                ('021', 'ZY-045')]
        # cursor.executemany(car_del_sql, car_del_val)
        
        # odr_sql = 'INSERT INTO Order_record (Cus_Phone, D_ID, S_Name, C_Plate_Number) VALUES (%s, %s, %s, %s)'
        # odr_val = [('0978-238-506', '001', 'Muji', 'ZY-056'), 
        #            ('0935-508-785', '001', 'Muji', 'GH-011'),
        #            ('0921-656-779', '005', 'Lativ', 'AZ-088'),
        #            ('0934-556-888', '008', 'McDonald', 'AB-026'),
        #            ('0929-335-678', '011', 'MosBurger', 'FQ-033'),
        #            ('0926-313-565', '014', 'Louisa', 'TY-085'),
        #            ('0926-313-565', '014', 'Louisa', 'AB-062'),
        #            ('0926-457-889', '015', 'CakeBakery', 'AB-051'),
        #            ('0978-122-356', '016', 'Acer', 'EJ-035'),
        #            ('0933-377-688', '017', 'YourDesign', 'CQ-015'),
        #            ('0923-234-665', '019', 'Skechers', 'AB-011'),
        #            ('0923-234-665', '021', 'QueenShop', 'ZY-045')]
        # cursor.executemany(odr_sql, odr_val)
        
        # connection.commit()
finally:
    cursor.close()

# http://www.dealingdata.net/2016/08/21/Python-MySQL-GUI/
class aggregate_interface(object):
    def __init__(self, ip, user, pswd, db, fontStyle, table_name):
        self.ip=ip
        self.user=user
        self.pswd=pswd
        self.db=db
        self.fontStyle = fontStyle
        self.table_name = table_name
        
        self.window = tk.Toplevel()
        self.window.wm_title("Aggregate")
        self.window.geometry('800x400')
        self.window.configure(background='white')
        
        self.table_label = tk.Label(self.window, text=f'Table: {table_name}', anchor='w', font=self.fontStyle)
        self.table_label.place(x=20, y=20, height=30, width=200)
        self.table_label.config(background='white')
        
        self.record_label = tk.Label(self.window, text='', anchor='w', font=self.fontStyle)
        self.record_label.place(x=20, y=50, height=30, width=200)
        self.record_label.config(background='white')
        
        self.condition_label = tk.Label(self.window, text='Condition', font=self.fontStyle)
        self.condition_label.place(x=20, y=100, height=30, width=760)
        self.condition_label.config(background='gray80')
        
        # Count button
        self.count_button = tk.Button(self.window, text=f'Count', font=self.fontStyle, command=self.condition)
        self.count_button.place(x=20, y=200, height=30, width=760)
        self.count_button.config(background='gold')
        
        # Clean combobox
        self.clean_button = tk.Button(self.window, text=f'Clean', font=self.fontStyle, command=self.clean_value)
        self.clean_button.place(x=630, y=20, height=30, width=150)
        self.clean_button.configure(background='white')
        
        self.display_condition()
        self.total_record(table_name)
    
    def display_condition(self):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            
            # Display select table
            cur.execute(f'SHOW COLUMNS FROM {self.table_name}')
            table_columns = cur.fetchall()
            # Combo
            combo_label, self.column_combo = [], []
            for i in range(len(table_columns)):
                combo_label.append(tk.Label(self.window, text=table_columns[i][0], font=self.fontStyle))
                combo_label[i].place(x=20+190*(i), y=130, height=30, width=190)
                cur.execute(f'SELECT DISTINCT {table_columns[i][0]} FROM {self.table_name}')
                self.column_combo.append(ttk.Combobox(self.window, values=cur.fetchall(), font=self.fontStyle))
                self.column_combo[i].place(x=20+190*(i), y=160, height=30, width=190)   
        finally:
            cur.close()
    
    def total_record(self, table_name):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            
            # Show total number of record
            cur.execute(f'SELECT COUNT(*) FROM {self.table_name}')
            count_total = cur.fetchone()[0]
            self.record_label.config(text=f'Total Record: {count_total}')           
        finally:
            cur.close() 
        
    def condition(self):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SHOW COLUMNS FROM {self.table_name}')
            table_columns = cur.fetchall()
            
            # count
            for i in range(len(self.column_combo)):
                if self.column_combo[i].get():
                    self.condition = f'{table_columns[i][0]}="{self.column_combo[i].get()}"'
                    cur.execute(f'SELECT COUNT({table_columns[i][0]}) FROM {self.table_name} WHERE {self.condition}')
            count_condition = cur.fetchone()[0]
            self.count_result = tk.Label(self.window, text=f'Record: {count_condition}', background='gray80', font=self.fontStyle)
            self.count_result.place(x=630, y=360, height=30, width=150)
            
            # find int atribute for sum, max, min, avg.
            aggregate_list = ['Sum', 'Max', 'Min', 'Avg']
            for i in range(len(table_columns)):
                self.agg_result = []
                if table_columns[i][1]=='int':
                    for agg in range(len(aggregate_list)):
                        cur.execute(f'SELECT {aggregate_list[agg]}({table_columns[i][0]}) FROM {self.table_name}')
                        agg_total = cur.fetchone()[0]
                        cur.execute(f'SELECT {aggregate_list[agg]}({table_columns[i][0]}) FROM {self.table_name} WHERE {self.condition}')
                        agg_condition = cur.fetchone()[0]
                        self.agg_result.append(tk.Label(self.window, 
                                                        text=f'{aggregate_list[agg]}: {round(agg_condition, 0)}/{round(agg_total, 0)}', 
                                                        background='gray80', 
                                                        font=self.fontStyle))
                        self.agg_result[agg].place(x=20+190*i, y=240+30*agg, height=30, width=190)         
        finally:
            cur.close() 

    def clean_value(self):
        for i in range(len(self.column_combo)):
            self.column_combo[i].set('')
        
class button_interface(object):
    def __init__(self, ip, user, pswd, db, fontStyle):
        self.ip=ip
        self.user=user
        self.pswd=pswd
        self.db=db
        self.fontStyle = fontStyle
        
        self.window = tk.Toplevel()
        self.window.wm_title("Button Interface")
        self.window.geometry('800x700')
        self.window.configure(background='white')
        
        # Combo
        self.combo_label = tk.Label(self.window, text="Table", font=self.fontStyle)
        self.combo_label.place(x=20, y=20, width=100)
        self.combo_label.config(background='gray80')
        
        # Search field
        # Search button
        self.search_button = tk.Button(self.window, text="Search", font=self.fontStyle, command=self.sendSearch)
        self.search_button.place(x=350, y=15, width=100)
        # Search status
        self.status_label = tk.Label(self.window, text='', font=self.fontStyle)
        self.status_label.configure(background = 'white')
        self.status_label.place(x=20, y=60, width=760)
        
        # Condition field
        self.condition_label = tk.Label(self.window, text='Condition', font=self.fontStyle)
        self.condition_label.place(x=20, y=90, height=30, width=760)
        self.condition_label.config(background='gray80')
        self.label = []
        for i in range(4):
            self.label.append(tk.Label(self.window, text='', font=self.fontStyle))
            self.label[i].place(x=20+190*(i), y=120, height=30, width=190)
        
        # Result field
        self.result = tk.Label(self.window, text='Result', font=self.fontStyle)
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
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
            table_name = cur.fetchall()
            self.table_combo = ttk.Combobox(self.window, font=self.fontStyle,
                                            values=[table_name[i][2] for i in range(len(table_name))])
            self.table_combo.place(x=120, y=20, height=30, width=200)
        finally:
            cur.close()
            
    def sendSearch(self):
        self.select_button = tk.Button(self.window, text='Select', font=self.fontStyle, command=self.select_fun)          
        self.select_button.place(x=720, y=15, width=60)
        self.select_button.config(background='light sky blue')
        
        for i in range(len(self.label)):
            self.label[i].config(text='')
        self.listBox.delete(*self.listBox.get_children())
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            # Display select table
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            table_columns = cur.fetchall()
            self.listBox.config(columns=table_columns)
            for i in range(len(table_columns)):
                self.listBox.heading(i, text=table_columns[i][0])
                self.listBox.column(i, stretch='True', anchor='center', width='190')
          
            # Entry
            text, self.entry = [], []
            for i in range(len(table_columns)):
                self.label[i].config(text=table_columns[i][0])
                text.append(tk.StringVar())
                self.entry.append(tk.Entry(self.window, textvariable=text[i], font=self.fontStyle))
                self.entry[i].place(x=20+190*(i), y=150, height=40, width=190)
                
            # Buttons
            function_label = tk.Label(self.window, text="Function", font=self.fontStyle, background='goldenrod1')
            function_label.place(x=20, y=200, height=30, width=150) 
            
            insert_button = tk.Button(self.window, text="Insert", font=self.fontStyle, command=self.insert)
            insert_button.place(x=200, y=200, height=30, width=100) 
            insert_button.config(background='Gold')
            
            delete_button = tk.Button(self.window, text="Delete", font=self.fontStyle, command=self.delete)
            delete_button.place(x=330, y=200, height=30, width=100) 
            delete_button.config(background='Gold')
            
            update_button = tk.Button(self.window, text="Update", font=self.fontStyle, command=self.update)
            update_button.place(x=460, y=200, height=30, width=100) 
            update_button.config(background='Gold')
            
            aggregate_button = tk.Button(self.window, text="Aggregate", font=self.fontStyle, command=self.aggregate)
            aggregate_button.place(x=590, y=200, height=30, width=100) 
            aggregate_button.config(background='Gold')
            
            clean_button = tk.Button(self.window, text="Clean", font=self.fontStyle, command=self.clean)
            clean_button.place(x=720, y=200, height=50, width=60) 
            
            self.select_columns_combo = ttk.Combobox(self.window, font=self.fontStyle)          
            self.select_columns_combo.place(x=420, y=400, height=30, width=120)
            
            self.agg_combo = ttk.Combobox(self.window, font=self.fontStyle)        
            self.agg_combo.place(x=380, y=300, height=30, width=100)
            
            cur.execute(f'SELECT * FROM {self.table_combo.get()}')
            table_result = cur.fetchall()
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
        finally:
            cur.close()
            
    def select_fun(self):
        self.listBox.delete(*self.listBox.get_children())
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            select_value = {}
            condition = ''
            table_columns = cur.fetchall()
            for i in range(len(table_columns)):
                select_value[table_columns[i][0]] = self.entry[i].get()
                if select_value[table_columns[i][0]] != '' and condition=='':
                    condition = condition + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
                elif select_value[table_columns[i][0]] != '':
                    condition = condition + ' AND ' + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
            cur.execute(f'SELECT * FROM {self.table_combo.get()} WHERE {condition}')
            table_result = cur.fetchall()
            if table_result:
                for row in table_result:
                    self.listBox.insert('', 'end', values=row)
        finally:
            cur.close()
    
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
        self.exist_label = tk.Label(self.window, text='EXIST', font=self.fontStyle, background='pale green')
        self.exist_label.place(x=100, y=400, height=30, width=75)
        self.exist_combo = ttk.Combobox(self.window, font=self.fontStyle, values=['EXISTS', 'NOT EXISTS'])        
        self.exist_combo.place(x=200, y=400, height=30, width=100)
        self.exist_button = tk.Button(self.window, text='Send', command=self.exist_func, font=self.fontStyle)
        self.exist_button.place(x=720, y=400, height=30, width=60)
        self.exist_button.config(background='medium spring green')
        self.equal_label = tk.Label(self.window, text='=', font=self.fontStyle, background='pale green')
        self.equal_label.place(x=550, y=400, height=30, width=30)
        
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            # Display select table
            cur.execute(f'SELECT * FROM information_schema.tables WHERE table_schema = "delivery_db"')
            table_name = cur.fetchall()
            self.select_table_combo = ttk.Combobox(self.window, font=self.fontStyle, 
                                                  values=[table_name[i][2] for i in range(len(table_name))])          
            self.select_table_combo.place(x=310, y=400, height=30, width=100)
            self.select_table_combo.bind("<<ComboboxSelected>>", self.create_column_combo)
            
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            current_table_columns = cur.fetchall()
            self.current_columns_combo = ttk.Combobox(self.window, font=self.fontStyle, 
                                                     values=[current_table_columns[i][0] for i in range(len(current_table_columns))])          
            self.current_columns_combo.place(x=590, y=400, height=30, width=120)            
        finally:
            cur.close() 
            
    def exist_func(self):
        self.listBox.delete(*self.listBox.get_children())
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_combo.get()} \
                        WHERE {self.exist_combo.get()} \
                        (SELECT * FROM {self.select_table_combo.get()} \
                         WHERE {self.table_combo.get()}.{self.current_columns_combo.get()}={self.select_table_combo.get()}.{self.select_columns_combo.get()})')
            table_result = cur.fetchall()
            if table_result:
                for row in table_result:
                    self.listBox.insert('', 'end', values=row)
            self.status_label.configure(text = '')
            self.status_label.configure(background = 'white')            
        finally:
            cur.close() 
            
    def create_column_combo(self, event):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            cur.execute(f'SHOW COLUMNS FROM {self.select_table_combo.get()}')
            select_table_columns = cur.fetchall()
            self.select_columns_combo['values'] = [select_table_columns[i][0] for i in range(len(select_table_columns))]
        finally:
            cur.close()
            
    def in_display(self):
        self.nested_label = tk.Label(self.window, text='Nested', font=self.fontStyle, background='pale green')
        self.nested_label.place(x=20, y=360, height=70, width=75)
        self.in_label = tk.Label(self.window, text='IN', font=self.fontStyle, background='pale green')
        self.in_label.place(x=100, y=360, height=30, width=75)
        self.in_combo = ttk.Combobox(self.window, font=self.fontStyle, values=['IN', 'NOT IN'])        
        self.in_combo.place(x=380, y=360, height=30, width=90)
        self.in_entry = tk.Entry(self.window, font=self.fontStyle)
        self.in_entry.place(x=500, y=360, height=30, width=210)
        self.in_button = tk.Button(self.window, text='Send', command=self.in_func, font=self.fontStyle)
        self.in_button.place(x=720, y=360, height=30, width=60)
        self.in_button.config(background='medium spring green')
        
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            # Display select table
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            table_columns = cur.fetchall()
            self.column_combo = ttk.Combobox(self.window, font=self.fontStyle,
                                             values=[table_columns[i][0] for i in range(len(table_columns))])        
            self.column_combo.place(x=200, y=360, height=30, width=150)                       
        finally:
            cur.close() 
            
    def in_func(self):
        self.listBox.delete(*self.listBox.get_children())
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SELECT * FROM {self.table_combo.get()} \
                        WHERE {self.column_combo.get()} {self.in_combo.get()} ({self.in_entry.get()})')
            table_result = cur.fetchall()
            if table_result:
                for row in table_result:
                    self.listBox.insert('', 'end', values=row)
            self.status_label.configure(text = '')
            self.status_label.configure(background = 'white')            
        finally:
            cur.close() 
        
    def having_display(self):   
        self.groupby_label = tk.Label(self.window, text='Grouped by', font=self.fontStyle, background='light salmon')
        self.groupby_label.place(x=20, y=260, height=30, width=150)
        self.having_label = tk.Label(self.window, text='Having', font=self.fontStyle, background='light salmon')
        self.having_label.place(x=20, y=300, height=30, width=150)
        self.ope_combo = ttk.Combobox(self.window, values=['>', '<', '=', '>=', '<='], font=self.fontStyle)        
        self.ope_combo.place(x=510, y=300, height=30, width=50)
        self.condition_entry = tk.Entry(self.window, font=self.fontStyle)
        self.condition_entry.place(x=590, y=300, height=30, width=120)
        self.having_button = tk.Button(self.window, text='Send', command=self.having_func, font=self.fontStyle)
        self.having_button.place(x=720, y=260, height=70, width=60)
        self.having_button.config(background='salmon')
        
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            # Display select table
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            table_columns = cur.fetchall()
            self.groupby_combo = ttk.Combobox(self.window, font=self.fontStyle,
                                              values=[table_columns[i][0] for i in range(len(table_columns))])        
            self.groupby_combo.place(x=200, y=260, height=30, width=200)
            
            self.havcol_combo = ttk.Combobox(self.window, font=self.fontStyle,
                                             values=[table_columns[i][0] for i in range(len(table_columns))])        
            self.havcol_combo.place(x=200, y=300, height=30, width=150)  
            self.havcol_combo.bind("<<ComboboxSelected>>", self.create_agg_combo)
        
        finally:
            cur.close()
            
    def having_func(self):
        self.listBox.delete(*self.listBox.get_children())
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SELECT {self.groupby_combo.get()}, {self.agg_combo.get()}({self.havcol_combo.get()})\
                        FROM {self.table_combo.get()} \
                        GROUP BY {self.groupby_combo.get()} \
                        HAVING {self.agg_combo.get()}({self.havcol_combo.get()}) {self.ope_combo.get()} {self.condition_entry.get()}')
            table_result = cur.fetchall()
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
        finally:
            cur.close()
            
    def create_agg_combo(self, event):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            # Display select table
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            table_columns = cur.fetchall()
            
            # Find int column
            int_column = []
            for i in range(len(table_columns)):
                if table_columns[i][1]=='int':
                    int_column.append(table_columns[i][0])  
                    
            if self.havcol_combo.get() in int_column: 
                self.agg_combo['values'] = ['Sum', 'Max', 'Min', 'Avg', 'Count']
            else:
                self.agg_combo['values'] = ['Count']
        finally:
            cur.close()
            
    def aggregate(self):
        aggregate_interface(self.ip, self.user, self.pswd, self.db, self.fontStyle, self.table_combo.get())

    def insert(self):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            insert_value = []
            for i in range(len(self.entry)):
                insert_value.append(self.entry[i].get())
            cur.execute(f'INSERT INTO {self.table_combo.get()} VALUES{tuple(insert_value)}')  
            con.commit()
            self.listBox.insert('', tk.END, text=str(cur.lastrowid), values=tuple(insert_value))
        finally:
            cur.close()
        self.update_listbox()
        
    def delete(self):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            delete_value = {}
            condition = ''
            table_columns = cur.fetchall()
            for i in range(len(table_columns)):
                delete_value[table_columns[i][0]] = self.entry[i].get()
                if delete_value[table_columns[i][0]] != '' and condition=='':
                    condition = condition + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
                elif delete_value[table_columns[i][0]] != '':
                    condition = condition + ' AND ' + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
            cur.execute(f'DELETE FROM {self.table_combo.get()} WHERE {condition}')  
            con.commit()
        # except:
        #     warning_window = tk.Toplevel()
        #     warning_window.wm_title("Warning")
        #     warning_window.geometry('500x100')
        #     warning_window.configure(background='white')
        #     warning_label = tk.Label(warning_window, 
        #                              text='Please enter condition for deletion!', font=self.fontStyle)
        #     warning_label.configure(background = 'white')
        #     warning_label.place(x=20, y=20, width=460)
        finally:
            cur.close()
        self.update_listbox()
    
    def update(self):
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            update_value = {}
            condition = ''
            table_columns = cur.fetchall()
            for i in range(1, len(table_columns)):
                update_value[table_columns[i][0]] = self.entry[i].get()
                if condition=='':
                    condition = condition + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
                elif update_value[table_columns[i][0]] != '':
                    condition = condition + ', ' + str(f'{table_columns[i][0]}="{self.entry[i].get()}"')
            cur.execute(f'UPDATE {self.table_combo.get()} SET {condition} WHERE {table_columns[0][0]}="{self.entry[0].get()}"')
            con.commit()
        finally:
            cur.close()
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
                                     text='[Not allowed] More than one tuples are choosen!', font=self.fontStyle)
            warning_label.configure(background = 'white')
            warning_label.place(x=20, y=20, width=460)
            
    def update_listbox(self):
        self.listBox.delete(*self.listBox.get_children())
        try:
            # Connect to db
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
            # Display select table
            cur.execute(f'SHOW COLUMNS FROM {self.table_combo.get()}')
            table_columns = cur.fetchall()
            self.listBox.config(columns=table_columns)
            for i in range(len(table_columns)):
                self.listBox.heading(i, text=table_columns[i][0])
                self.listBox.column(i, stretch='True', anchor='center', width='190')
            cur.execute(f'SELECT * FROM {self.table_combo.get()}')
            table_result = cur.fetchall()
            if table_result:
                for row in table_result:
                    self.listBox.insert('', 'end', values=row)
        finally:
            cur.close()
      
class query_interface(object):
    def __init__(self, ip, user, pswd, db, fontStyle):
        self.ip=ip
        self.user=user
        self.pswd=pswd
        self.db=db
        self.fontStyle = fontStyle
        
        window= tk.Toplevel()
        window.wm_title("Query Interface")
        window.geometry('800x600')
        window.configure(background='white')
        self.fontStyle = font.Font(family='Calibri', size=15)
        
        # Query field
        self.query_label = tk.Label(window, text="Query", font=self.fontStyle)
        self.query_label.place(x=20, y=70, height=100, width=100)
        self.query_label.config(background='gray80')
        self.query_entry = ScrolledText(window)
        self.query_entry.place(x=120, y=70, height=100, width=660)
        
        # Query button
        self.query_button = tk.Button(window, text="Send Query", font=self.fontStyle, command=self.sendQuery)
        self.query_button.place(x=20, y=170, width=760)
        
        # Query status
        self.status_label = tk.Label(window, text='', font=self.fontStyle)
        self.status_label.configure(background = 'white')
        self.status_label.place(x=20, y=220, width=760)
        
        # Result field
        self.result = tk.Label(window, text='Result', font=self.fontStyle)
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
        
    def sendQuery(self):
        self.listBox.delete(*self.listBox.get_children())
        # Setting the query
        self.query = self.query_entry.get('1.0', tk.END)
        try:
            con = pymysql.connect(self.ip, self.user, self.pswd, self.db)
            cur = con.cursor()
    
            # Send select statement
            cur.execute(self.query)
            con.commit()
            # # Display select table
            # table_columns = cur.description
            # self.listBox.config(columns=table_columns)
            # for i in range(len(table_columns)):
            #     self.listBox.heading(i, text=table_columns[i][0])
            #     self.listBox.column(i, stretch='True', anchor='center', width='190')
          
            # table_result = cur.fetchall()
            # if table_result:
            #     for row in table_result:
            #         self.listBox.insert('', 'end', values=row)
            
            # self.status_label.configure(text = 'Query Success')
            # self.status_label.configure(background = 'chartreuse3', fg='white')
        # except:
        #     self.status_label.configure(text = 'Query Failed')
        #     self.status_label.configure(background = 'orange red', fg='white')
        finally:
            cur.close()
        
class db_interface(object):
    def __init__(self, window, ip, user, pswd, db):
        self.ip=ip
        self.user=user
        self.pswd=pswd
        self.db=db

        # Set the window title 
        window.wm_title("Database Interface")
        window.geometry('800x200')
        window.configure(background='white')
        self.fontStyle = font.Font(family='Calibri', size=15)
        
        # Select button
        self.query_button = tk.Button(window, text="Query", font=self.fontStyle, command=self.query)
        self.query_button.place(x=275, y=100)
        self.button_button = tk.Button(window, text="Button", font=self.fontStyle, command=self.button)
        self.button_button.place(x=425, y=100)
        
        self.choose_label = tk.Label(window, text="Please choose a way for SQL:", font=self.fontStyle)
        self.choose_label.place(x=190, y=40, width=400)
        self.choose_label.configure(background='white')
    
    def query(self):
        query_interface(self.ip, self.user, self.pswd, self.db, self.fontStyle)
        
    def button(self):
        button_interface(self.ip, self.user, self.pswd, self.db, self.fontStyle)

            
# Create the GUI and pass it to our App class
def main(host, user, password, db):
    window= tk.Tk()
    db_interface(window, host, user, password, db)
    window.mainloop()

if __name__ == "__main__":
    main(host='localhost', user='root', password='red91310', db = 'delivery_db')