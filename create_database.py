#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 19:29:59 2020

@author: polab
"""

import pymysql

# Connect mysql
connection = pymysql.connect(host='localhost',
                              user='root',
                              password='red91310',
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor: 
        # Create database
        cursor.execute("CREATE DATABASE IF NOT EXISTS delivery_db")
        connection.commit()
finally:
    cursor.close()
