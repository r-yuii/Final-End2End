import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='rootpass'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE db_final")

print("Done creating the database.")