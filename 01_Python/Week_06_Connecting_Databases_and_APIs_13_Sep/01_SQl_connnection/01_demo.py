import mysql.connector 

# used to establish connection with mysql server
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '****'
)

# print gives the mysql connection object
print(mydb)
''' output : <mysql.connector.connection_cext.CMySQLConnection object at 0x00000241F8FEF8B0> '''

# gives cursor to mysql to perform operation
mycursor = mydb.cursor()

# to execute query we have to use cursor 
mycursor.execute('SHOW DATABASES')

# we are try to iterate through database present to print there name
for x in mycursor:
    print(x)
''' output : 
('company',)
('flights',)
('hostel',)
('information_schema',)
('library',)
('mysql',)
('org',)
('performance_schema',) '''