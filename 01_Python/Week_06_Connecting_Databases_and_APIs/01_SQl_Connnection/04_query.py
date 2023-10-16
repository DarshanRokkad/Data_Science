import mysql.connector
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '****'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM pythonTest1.table2')
for row in mycursor.fetchall():
    print(row)
'''
(1, 'Darshan', 9.1)
(2, 'Sanketh', 9.4)
(3, 'Amogha', 9.6)
'''
mydb.close()