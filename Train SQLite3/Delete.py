import sqlite3

filename = "Train.db"

connection = sqlite3.connect(filename)
cursor = connection.cursor()

full = entry_full.get()
age = entry_age.get()
score = entry_score.get()

Query = "DELETE * FROM Train WHERE 1=1"
param = []

if full:
    Query += "AND Full_Name = ?"
    param.append(full)

if age:
    Query += "AND Age = ?"
    param.append(age)

if score:
    Query += "AND Score = ?"
    param.append(score)

cursor.execute(Query, param)
result = cursor.fetchall()

for i in result:
    Entry_Show.insert(END, f"{i[0]}, {i[1]}, {i[2]}\n")

connection.commit()
connection.close()