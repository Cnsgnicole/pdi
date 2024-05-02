import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="sesiones"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT nombre address FROM sesion")

myresult = mycursor.fetchall()
class usuario:
  def __init__(self, nombre, contra):
    self.nombre = nombre
    self.contra = contra
  pass

for x in myresult:
  print("Bienvenido ", x)