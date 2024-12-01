import sqlite3

filename = "Train.db"

connection = sqlite3.connect(filename)
cursor = connection.cursor()

Create_Query = """
CREATE TABLE IF NOT EXISTS Train(
Full_Name TEXT,
Age INTEGER,
Score FLOAT)"""

cursor.execute(Create_Query)

connection.commit()
connection.close()