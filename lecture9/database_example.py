import sqlite3

conn = sqlite3.connect("zoo.sqlite")

cursor = conn.cursor()


animals = [('Frog', 10), ('Snake', 5), ('Turtle', 11)]

cursor.executemany("insert into animal_count(name, count) values (?, ?)", animals)

result = cursor.execute("select * from animal_count")

for row in result:
	print(row)

conn.commit()

conn.close()