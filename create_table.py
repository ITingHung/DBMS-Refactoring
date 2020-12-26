#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:29:59 2020

@author: polab
"""

import pymysql
    
# Connect delivery_database
connection_db = pymysql.connect(host='localhost',
                                user='root',
                                password='red91310',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,
                                database = 'delivery_db')

try:
    with connection_db.cursor() as cursor:    
        # Create table
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
        
        cus_sql = 'INSERT INTO Customer (Phone, BirthDate, Gender, City) VALUES (%s, %s, %s, %s)'
        cus_val = [('0978-238-506', '1997-02-23', 'F', 'Tainan'), 
                    ('0935-508-785', '1998-12-02', 'M', 'Tainan'),
                    ('0921-656-779', '1996-10-15', 'F', 'Taipei'),
                    ('0934-556-888', '1996-05-05', 'F', 'Kaohsiung'),
                    ('0929-335-678', '1997-02-23', 'M', 'Tainan'),
                    ('0926-313-565', '1998-07-31', 'F', 'Taichung'),
                    ('0926-457-889', '1995-10-26', 'M', 'Taichung'),
                    ('0978-122-356', '1996-04-26', 'F', 'Kaohsiung'),
                    ('0933-377-688', '1996-06-29', 'F', 'Tainan'),
                    ('0923-234-665', '1996-05-05', 'M', 'Tainan')]
        cursor.executemany(cus_sql, cus_val)
        
        pla_sql = 'INSERT INTO Platform (Name, Employee_number, Capital, Country) VALUES (%s, %s, %s, %s)'
        pla_val = [('Books', '310', '10000', 'Taiwan'), 
                    ('YourStyle', '125', '3000', 'America'),
                    ('UberEat', '620', '5500', 'America'),
                    ('Yummy', '255', '90000', 'Japan'),
                    ('FoodPanda', '620', '3000', 'Taiwan'),
                    ('Foodyy', '56', '2000', 'Japan'),
                    ('3C Shop', '79', '5500', 'America'),
                    ('Pinkoi', '125', '8100', 'Taiwan'),
                    ('Taobao', '875', '20000', 'China'),
                    ('Shopee', '1021', '3000', 'China')]
        cursor.executemany(pla_sql, pla_val)

        del_sql = 'INSERT INTO Deliver (ID, Gender, Tenure, Platform_name) VALUES (%s, %s, %s, %s)'
        del_val = [('001', 'F', '10', 'Books'), 
                    ('002', 'M', '8', 'Books'),
                    ('003', 'F', '5', 'Books'),
                    ('004', 'M', '3', 'Books'),
                    ('005', 'M', '3', 'YourStyle'),
                    ('006', 'F', '5', 'YourStyle'),
                    ('007', 'M', '10', 'YourStyle'),
                    ('008', 'F', '3', 'UberEat'),
                    ('009', 'F', '3', 'UberEat'),
                    ('010', 'M', '3', 'UberEat'),
                    ('011', 'M', '5', 'Yummy'),
                    ('012', 'F', '3', 'Yummy'),
                    ('013', 'M', '1', 'FoodPanda'),
                    ('014', 'M', '1', 'FoodPanda'),
                    ('015', 'M', '7', 'Foodyy'),
                    ('016', 'M', '1', '3C Shop'),
                    ('017', 'F', '5', 'Pinkoi'),
                    ('018', 'M', '3', 'Pinkoi'),
                    ('019', 'M', '7', 'Taobao'),
                    ('020', 'M', '4', 'Shopee'),
                    ('021', 'M', '5', 'Shopee')]
                   
        cursor.executemany(del_sql, del_val)
        
        sho_sql = 'INSERT INTO Shop (Name, Employee_number, Country, Platform_name) VALUES (%s, %s, %s, %s)'
        sho_val = [('Muji', '50', 'Taipei', 'Books'), 
                    ('Uniqlo', '1325', 'Tainan', 'YourStyle'),
                    ('Net', '586', 'Tainan', 'YourStyle'),
                    ('Lativ', '50', 'Taiana', 'YourStyle'),
                    ('McDonald', '3120', 'Tainan', 'UberEat'),
                    ('MosBurger', '1325', 'Tainan', 'Yummy'),
                    ('Louisa', '2000', 'Taipei', 'FoodPanda'),
                    ('CakeBakery', '120', 'Taipei', 'Foodyy'),
                    ('Donutes', '120', 'Taipei', 'Foodyy'),
                    ('Apple', '7625', 'Taipei', '3C Shop'),
                    ('Acer', '3120', 'Kaohsiung', '3C Shop'),
                    ('YourDesign', '5', 'Taipei', 'Pinkoi'),
                    ('Nike', '2000', 'Kaohsiung', 'Taobao'),
                    ('Skechers', '2000', 'Tainan', 'Taobao'),
                    ('QueenShop', '120', 'Tainan', 'Shopee')]
        
        cursor.executemany(sho_sql, sho_val)
        
        car_sql = 'INSERT INTO Car (Plate_Number, Type, Year, Platform_name) VALUES (%s, %s, %s, %s)'
        car_val = [('ZY-056', 'Truck', '10', 'Books'),
                    ('GH-011', 'Van', '3', 'Books'),
                    ('AZ-088', 'Truck', '5', 'YourStyle'),
                    ('ZY-022', 'Van', '5', 'YourStyle'),
                    ('GH-015', 'Truck', '1', 'YourStyle'),
                    ('AB-026', 'Van', '10', 'UberEat'),
                    ('GH-091', 'Van', '1', 'UberEat'),
                    ('FQ-091', 'Van', '5', 'UberEat'),
                    ('FQ-033', 'Van', '1', 'Yummy'),
                    ('TY-085', 'Van', '3', 'FoodPanda'),
                    ('AB-062', 'Van', '3', 'FoodPanda'),
                    ('AB-027', 'Van', '3', 'Foodyy'),
                    ('AB-051', 'Van', '5', 'Foodyy'),
                    ('EJ-035', 'Truck', '7', '3C Shop'),
                    ('CQ-015', 'Truck', '5', 'Pinkoi'),
                    ('AB-013', 'Van', '3', 'Pinkoi'),
                    ('AB-011', 'Truck', '10', 'Taobao'),
                    ('AB-096', 'Truck', '7', 'Shopee'),
                    ('ZY-045', 'Truck', '1', 'Shopee')]
        cursor.executemany(car_sql, car_val)
        
        car_del_sql = 'INSERT INTO Car_Deliver (D_ID, C_Plate_Number) VALUES (%s, %s)'
        car_del_val = [('001', 'ZY-056'), ('001', 'GH-011'),
                        ('002', 'ZY-056'), ('002', 'GH-011'),
                        ('003', 'ZY-056'),
                        ('004', 'GH-011'),
                        ('005', 'AZ-088'), ('005', 'GH-015'),
                        ('006', 'ZY-022'),
                        ('007', 'AZ-088'), ('007', 'GH-015'),
                        ('008', 'AB-026'),
                        ('009', 'GH-091'),
                        ('010', 'FQ-091'),
                        ('011', 'FQ-033'),
                        ('012', 'FQ-033'),
                        ('013', 'TY-085'), ('013', 'AB-062'),
                        ('014', 'TY-085'), ('014', 'AB-062'),
                        ('015', 'AB-027'), ('015', 'AB-051'),
                        ('016', 'EJ-035'),
                        ('017', 'CQ-015'),
                        ('018', 'AB-013'),
                        ('019', 'AB-011'),
                        ('020', 'AB-096'),
                        ('021', 'ZY-045')]
        cursor.executemany(car_del_sql, car_del_val)
        
        odr_sql = 'INSERT INTO Order_record (Cus_Phone, D_ID, S_Name, C_Plate_Number) VALUES (%s, %s, %s, %s)'
        odr_val = [('0978-238-506', '001', 'Muji', 'ZY-056'), 
                    ('0935-508-785', '001', 'Muji', 'GH-011'),
                    ('0921-656-779', '005', 'Lativ', 'AZ-088'),
                    ('0934-556-888', '008', 'McDonald', 'AB-026'),
                    ('0929-335-678', '011', 'MosBurger', 'FQ-033'),
                    ('0926-313-565', '014', 'Louisa', 'TY-085'),
                    ('0926-313-565', '014', 'Louisa', 'AB-062'),
                    ('0926-457-889', '015', 'CakeBakery', 'AB-051'),
                    ('0978-122-356', '016', 'Acer', 'EJ-035'),
                    ('0933-377-688', '017', 'YourDesign', 'CQ-015'),
                    ('0923-234-665', '019', 'Skechers', 'AB-011'),
                    ('0923-234-665', '021', 'QueenShop', 'ZY-045')]
        cursor.executemany(odr_sql, odr_val)
        
        connection_db.commit()
finally:
    cursor.close()