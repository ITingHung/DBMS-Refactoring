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
