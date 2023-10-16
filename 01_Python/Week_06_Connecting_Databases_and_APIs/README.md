# Connecting with databases and APIs
1. Working with SQL.
    - Storing structured data.
    - mysql -u root -p -> collecting through terminal.
    - pip install mysql-connector-python.
    - import mysql.connector.
    - mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = '***') -> used to connect to the database.
    - mydb.close() -> have to close the database after using.
    - mycursor = mydb.cursor() -> to get the cursor to the database.
    - mycursor.execute('sql query') -> used to execute the query.  

2. Working with Mongodb.
    - Storing unstructured data.
    - pip install pymongo.
    - import pymongo
    - client = MongoClient(url) -> Creates the client for the mongodb database present on cloud.
    - db = client['database name'] -> Creating database.
    - collection = db['collection name'] -> Creating collection inside the database.
    - collection.insert_one(data) -> inserting a single dictionary.
    - collection.insert_many(data) -> inserting a list of dictionaries.
    - collection.find() -> gives interator to the collection to iterate over it.
    - collection.drop() -> to drop all the values of the collection.  

3. Working with API.
    - Api used to communicate between different application.
        - TCP -> Transmission Control Protocol.
        - HTTP -> Hyper Text Transfor Protocol.
        - SMTP -> Simple Mail Trangor Protocol.
    - WEB api -> they use http protocol to communicate. 
        - PUT , GET , POST and DELETE.
    - REST and SOUP.
        - REST -> Representational State Transfer.
        - SOUP -> Simple Object Access Protocol.  

4. Flask.
    - from flask import Flask
    - app = Flask(\_\_name\_\_) -> Create the object of the flask class.
    - @app.route("/") -> This routes the function present in below it in the root page.
    - app.run(host='0.0.0.0')
    - Postman -> Used to test the code.  
