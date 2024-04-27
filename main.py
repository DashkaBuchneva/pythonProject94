import sqlite3 as sq


with sq.connect("students.db") as con:
     cur = con.cursor()

     cur.execute("""CREATE TABLE IF NOT EXISTS students (
     students_id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT,
     last_name TEXT,
     age INTEGER,
     groupa TEXT,
     level INTEGER
     )""")

def add_students(cur, name, last_name, age, groupa, level):
     cur.execute()

with sq.connect("student.db") as con:
     cur = con.cursor()
     name = "Arina"
     last_name = "Petrova"
     age = 28
     groupa = "A345"
     level = 5
     add_students(cur, name, last_name, age, groupa, level)

