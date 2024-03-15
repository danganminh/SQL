import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

sql = 'DELETE FROM employees where id=1'

cursor.execute(sql)

connection.commit()
connection.close()