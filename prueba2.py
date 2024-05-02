import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="patoduck"
)

mycursor=mydb.cursor()
variable=mycursor.execute("show tables")
print(variable)