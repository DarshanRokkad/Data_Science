import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '****'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE DATABASE IF NOT EXISTS pythonTest1')

mycursor.execute('CREATE TABLE IF NOT EXISTS pythonTest1.table2 (Slno int not null primary key , Name varchar(25),Cgpa float )')

mydb.close()
