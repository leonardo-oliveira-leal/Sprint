import mysql.connector

mydb = mysql.connector.connect(
  host="54.166.197.65",
  user="Leonardo",
  password="sprint123",
  database="python"
)
print(mydb)

mycursor = mydb.cursor()

def insert(values):
  sql = "INSERT INTO algas (agTempo, agEspaco) VALUES (%s, %s)"

  mycursor.execute(sql, values)

  mydb.commit()