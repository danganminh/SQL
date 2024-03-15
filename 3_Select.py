import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

sql = "select * from employees"
cursor.execute(sql)
print("\nPrint all data in table")
for row in cursor:
    print(row)


sql_2 = "select name, phone from employees"
cursor.execute(sql_2)
print("\nPrint name and phone in table")
for row in cursor:
    print(row)


sql_3 = 'select * from employees where name like "A%"'
cursor.execute(sql_3)
print("\nPrint name like A...")
for row in cursor:
    print(row)


connection.close()