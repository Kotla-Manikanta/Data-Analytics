import mysql.connector

myDB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789"
)
print(myDB)