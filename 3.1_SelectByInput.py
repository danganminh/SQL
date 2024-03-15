import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

id = input('Enter an ID: ')

sql = 'select * from employees WHERE id=?'
cursor.execute(sql, (id,))

for row in cursor:
    print(row)

connection.close()