import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Leoleal5020",
  database="python"
)
print(mydb)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO algas (agTempo, agEspaco) VALUES (%s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()
