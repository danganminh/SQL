import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# opps
sql = 'UPDATE employees SET phone="+456456" where id="2"'
cursor.execute(sql)

connection.commit()
connection.close()