import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

sql = """
        INSERT INTO employees(id, name, department, phone, email) VALUES (1, "Dang", "IT", "+55555", "dang@gmail.com");
        INSERT INTO employees VALUES (2, "Dang_2", "IT_2", "+555552", "dang_2@gmail.com");
        INSERT INTO employees(id, name, department, phone, email) VALUES (5, "Alice Johnson", "HR", "+111222333", "alice.johnson@example.com");
        INSERT INTO employees(id, name, department, phone, email) VALUES (6, "Bob Brown", "Sales", "+444555666", "bob.brown@example.com");
        INSERT INTO employees(id, name, department, phone, email) VALUES (7, "Emma White", "Operations", "+777888999", "emma.white@example.com");
        INSERT INTO employees(id, name, department, phone, email) VALUES (8, "Chris Lee", "Customer Support", "+222333444", "chris.lee@example.com");
        INSERT INTO employees(id, name, department, phone, email) VALUES (9, "Sarah Johnson", "Research and Development", "+666777888", "sarah.johnson@example.com");
        INSERT INTO employees(id, name, department, phone, email) VALUES (10, "Michael Davis", "Quality Assurance", "+999000111", "michael.davis@example.com");
"""

cursor.executescript(sql)

connection.commit()
connection.close()