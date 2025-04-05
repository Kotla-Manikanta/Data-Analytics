import mysql.connector 

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="newdb"
)
print(conn)

cursor = conn.cursor()

