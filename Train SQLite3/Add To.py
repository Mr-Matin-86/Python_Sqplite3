import sqlite3

filename = "Train.db"

connection = sqlite3.connect(filename)
cursor = connection.cursor()

full = entry_full.get()
age = entry_age.get()
score = entry_score.get()

records = [full, age, score]
Insert_Query = """INSERT INTO Train(Full_Name, Age, Score) VALUES(?, ?, ?)"""

cursor.execute(Insert_Query, records)

connection.commit()
connection.close()