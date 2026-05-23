import sqlite3

connection = sqlite3.connect('student.db')

cursor = connection.cursor()

table_creation_query = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        grade INTEGER NULL,
        section VARCHAR(5) NOT NULL
    );
'''

cursor.execute(table_creation_query)

students_data = [
    ('Alice', 20, 85, 'A'),
    ('Bob', 22, 90, 'B'),  
    ('Charlie', 19, 78, 'A'),
    ('David', 21, 92, 'B'),
    ('Eve', 20, 88, 'A')
]

for value in students_data:
    cursor.execute('''
        INSERT INTO students (name, age, grade, section)
        VALUES (?, ?, ?, ?);
    ''', value)

data = cursor.execute('SELECT * FROM students;')
for row in data:
    print(row)

connection.commit()
connection.close()