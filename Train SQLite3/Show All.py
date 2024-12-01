import sqlite3

filename = "Train.db"

connection = sqlite3.connect(filename)
cursor = connection.cursor()

cursor.execute("SELECT * FROM Train")
result = cursor.fetchall()

for i in result:
    Entry_Show.insert(END, f"{i[0]}, {i[1]}, {i[2]}\n")

connection.close()