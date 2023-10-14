# Python

## Week 1 - [Basic Building](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_01_Basic_Building_30_Aug)
    1. Variables.  

    2. Mutable and Immutable objects.
        - list.
        - strings.  

    3. Operators.
        - arithmetic -> + , - , * , / , % , // .
        - logical -> and , or , not .
        - comparsion -> < , > , <= , >= .
        - bitwise -> & , | , ~ , ^ , << , >>.  

    4. Conditional statements.
        - if , elif and else.
        - is , in , == , != .  

    5. Looping 
        - for(start,stop,step).
        - while(condition).
        - while/for else .
        - loop contols -> break , continue and pass.  

##

## Week 2 - [Data structures](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_02_Data_Structures_31_Aug) 
    1. Print Function.
        - print("",var) 
        - print(f"{var}") 
        - print("{}".format(var))
        - print("{firstname}".format(firstname=var))
        - print returns 'None' type.  

    2. input Function.
        - input()  

    3. Type casting.
        - int(var) 
        - float(var) 
        - str(var)  

    4. Additional useful functions.
        - Address -> id(var).
        - Binary representation -> bin(var).
        - Deleting variable ->del var.  

    5. String.
        - Strings are immutable.  

    6. List.
        - Lists are Ordered and Mutable list.
        - List comprehension.
        - Shallow copy and Deep copy in 2D array.  

    7. Tuple.
        - Tuples are Ordered but Immutable list.  

    8. Set.
        - Sets are Unordered and Immutable list.
        - Sets contains Unique elements i.e no duplicates.
        - functions -> Subset , Superset , Union , Intersection , Difference , XOR.  

    9. Dictionary.
        - {key:value} Dictionary is present in the form of Key and value pair.
        - Dictionary comprehension.
        - Shallow copy and Deep copy in collections type values.

|Mutable|Unmutable|
|-|-|
|List|Tuple|
|Dictionary|Set|

|Ordered|Unordered|
|-|-|
|List|Set|
|Tuple||
|Dictionary||

|Hasable|Unhashable|
|-|-|
|int,float,bool,string|List|
|Tuple|Set|
||Dictionary|
##


## Week 3 - [Functions](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_03_Functions_2_Sep)
    1.Basics.
        - using of pass.
        - return values (None , Multiple values).
            - return None.
            - return Multiple values.
        - Default arguement function definition.
        - Keyword arguement function call.
        - Variable arugement [ def fun(*args) ]. (returns tuple)
        - Keyword arugement [ def fun(**kwargs) ]. (returns dictionary)  

    2.Generator functions.
        - range(start,end,step) genrator function.
        - yield.
        - To use memory efficiently.  

    3.Lambda functions.
        - Anonymous function(do not have a name).
        - Short hand of the function and not compulsary to use.  

    4.Map , Reduce and Filter.
        - Map.
            - Used to map between iterables using mapping function(maper).
            - Syntax : map(func,*iterable) --> map object.
        - Reduce.
            - Specially designed for the function with 2 parameters.
            - Syntax : reduce(func,iterable,intial value) --> respectively data type.
        - Filter.
            - To Filter out the elements in iterables based on some condition.
            - Syntax : filter(func,iterable) --> filter object.  

##


## Week 4 - [OOPS](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_04_Oops_4_Sep)
    1.Introduction.
        - Everything is a object in python.
        - class \<class name\>.
        - self parameter.
        - Constructor.
            - Syntax : def \_\_init\_\_(self).
            - It will automatically executed when the instance of the class is created.  

    2.Polymorphism.
        - A single function going to behave differently based on object.
        - Duck Typing.
        - Complie time polymorphism.
            - Method overloading .
            - Operator overloading .
        - Run time polymorphism.
            - Method overiding .  

    3.Encapsulation.
        - Binding data and function together in class.(Data + Function).
        - Private variable -> self.__var = value
        - In python private variables are not truely private.
            - Can modify the private variable -> obj._classname__var = value  

    4.Inheritance.
        - The method of aquiring the properties of the parent class to the child class.
        - Use : Code reusability.
        - Syntax : class child(parent):
        - Types: 
            1.Multilevel Inheritance. 
            2.Multiple Inheritance.  

    5.Abstract class.
        - Abstract method will give the blue print of the class and who want to use can inherit then implement and use it.
        - import abc.
        - Annotation -> @abc.abstractmethod  

    6.Decorator.
        - Decorator is used to add additional functionality to the function and avoid repeatative code. 
        - Annotation -> @decorator_function 
        - Calculating Time taken(import time).
            - time.time() -> Gives the current time.  

    7.Class variables and methods.
        - Used to pass data to class or access data from class without using \_\_init\_\_ method.
        - Anotation -> @classmethod.
        - These are common to all the objects of that class.
        - We can make external function as the class method.
            - \<classname\>.\<functionname\> = classmethod(\<function name\>)
        - To delete class variable or class methods.
            - delattr(\<class name\>,\<variable/function name\>)
            - del \<variable/function name\>  

    8.Static methods.
        - Used to reduce memory utilization.
        - Anotation -> @staticmethod.  

    9.Magic methods.
        - Magic or Dunder methods.
        - Adivsed to not to use dunder method.
        - internally \_\_new\_\_ is called before \_\_init\_\_.
        - dir(data_type) -> gives all the inbuilt function present in that data type class.  

    10.Property decorator.
        - Property is a decorator used to access or modify or delete the private or protected variable outside the class.
        1.Getter.
            - Anotation -> @property
        2.Setter.
            - Anotation -> @\<access function\>.setter
        3.Deleter.
            - Anotation -> @\<access function\>.deleter  

##

## Week 5 - [Files and Exception handling and Memory management](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_05_Files_ExceptionHandling_MemoryMangagement_5_Sep).
    1.Working with files.
        - pwd -> present working directory.
        - ls -> list of files present in the current folder.
        - f = open(filename,mode)
        - f.close() -> We have to close the file after using.
        - with open(file name , mode) as f -> file will be automatically opened and closed.
        - write operation.
            - Syntax -> f.write(content)
            - Erases the data if it is present in previously.
        - read operation.
            - Syntax -> data = f.read(content)
        - append operation.
            - Syntax -> f.write(content)
            - Adds the content to the end of the file.
        - f.seek(position) -> bring pointer to certian index.
        - f.tell() -> returns the position of the pointer.
        - os.path.getsize(filename) -> gives the size of the file.[import shutil]
        - shutil.copy(old,new) -> copy content of one file to another.[import stutil]
        - os.remove(filename) -> deletes the file.
        - os.rename(old,new) -> rename the file.  

    2.File reading and writing.
        - json.
            - import json
            - write -> json.dump(data,f) 
            - read -> data = json.load(f)
        - csv.
            - import csv
            - write -> w = csv.writer(f) and  w.writerow(i).
            - read -> r = csv.reader(f) and for i in r:
        - binary.
            - write -> f.write(b'data')
            - read -> print(f.read())  

    3.Buffered read and write other file methods.
        - import io.
        - Write -> file = io.BufferedWriter(f) and file.write(data)
        - Read -> file = io.BufferedReader(f) and data = file.read(chucks)  

    4.Logging and Debugger.
        - We can use logging to debug the code.
        - import logging.
        - Creating a log file -> logging.basicConfig(filename='file.log',level=logging.\<level\>).
        - logging -> loggging.\<level\>(message).
        - Hierarchy of logging levels.
            - 1. NOSET.
            - 2. DEBUG.
            - 3. INFO.
            - 4. WARNING.
            - 5. ERROR.
            - 6. CRITICAL.  

    5.Modules and import statement.
        - folder -> package.
        - file -> module.
        - methods are present inside the module.
        - from package import module.  

    6.Exception handling.
        - try.
        - except -> except Exception as e.
            - Exception class in the inbuilt class for handling exceptions.
        - else -> this block execute only on successfull execution of try block.
        - finally -> this block will execute always.
        - Custom exception handling.
            - class classname(Exception) -> have to inherit Exception class.
            - raise classname(message) -> this constructor should have variable to store this message.
        - Other general exceptions.
        - Best Practise of Exception Handling.
            - Use always a specific exception.
            - Print always a valid message.
            - Always log the error.
            - Always avoid to write multiple exception handling.
            - Prepare documentation.
            - Cleanup all the resources.  

    7.Multithreading.
        - Used to execute multiple process concurrently.
        - import threading.
        - Thread functions. 
            - threading.Thread(target=function_name,args=(args))
            - var.start() -> starts thread.
            - threading.Lock()
        - time.sleep(sec) -> Thread will sleep for some seconds [import time]. 
        - for downloading files.
            - import urllib.request
            - urllib.request.urlretrieve(url,file_name)  

    8.Multiprocessing.
        - multiprocessing.Process(target = function_name) -> create the multiple processes.
            - m.start() 
            - m.join() 
        - with multiprocessing.Pool(processes = number) as pool: -> Pool of process
            - var = pool.map(func,iterable)
        - multiprocessing.Queue() -> Use of Queue 
            - q.put(item)
            - q.get()
        - multiprocessing.Array('var',iterable) -> synchronized shared array.
        - multiprocessing.Pipe() -> returns 2 objects.
            - Use of send and recieve connection(In whatsapp messaging ).
            - connection.send(msg)
            - connection.recv()  

##

## Week 6 - [Connecting with databases and APIs](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_06_Connecting_Databases_and_APIs_13_Sep)
    1.Working with SQL.
        - Storing structured data.
        - mysql -u root -p -> collecting through terminal.
        - pip install mysql-connector-python.
        - import mysql.connector.
        - mydb = mysql.connector.connect(host = 'localhost',user = 'root',password = '***') -> used to connect to the database.
        - mydb.close() -> have to close the database after using.
        - mycursor = mydb.cursor() -> to get the cursor to the database.
        - mycursor.execute('sql query') -> used to execute the query.  

    2.Working with Mongodb.
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

    3.Working with API.
        - Api used to communicate between different application.
            - TCP -> Transmission Control Protocol.
            - HTTP -> Hyper Text Transfor Protocol.
            - SMTP -> Simple Mail Trangor Protocol.
        - WEB api -> they use http protocol to communicate. 
            - PUT , GET , POST and DELETE.
        - REST and SOUP.
            - REST -> Representational State Transfer.
            - SOUP -> Simple Object Access Protocol.  

    4.Flask.
        - from flask import Flask
        - app = Flask(\_\_name\_\_) -> Create the object of the flask class.
        - @app.route("/") -> This routes the function present in below it in the root page.
        - app.run(host='0.0.0.0')
        - Postman -> Used to test the code.  

##

## Week 7 - [Web and Image Scraping](https://github.com/DarshanRokkad/Data_Science/tree/master/01_Python/Week_07_Web_and_Image_Scraping_25_Sep)
    1. Web Scrapping.
        - Libraries.
            - import requests 
            - from bs4 import BeautifulSoup as bs
            - from urllib.request import urlopen
        - url_client = urlopen(url) -> we will get the http response.
        - raw_page = url_client.read() -> We will get a raw html page.
        - html_page = bs(raw_page,'html.parser') -> We will get the actual html page.
        - from this html page we can extract the data -> page.find_all(element,{'class':'class name'})
        - response = requests.get(href_link) -> to enter into inner page response we can request for page html after getting the response we can use page by converting into text.  
        
    2.Image Scrapping.
        - headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"} -> Have to add to avoid the blocking from google for scrapping.
        - with open(os.path.join(save_directory, f"{query}_{image_tags.index(image_tag)}.jpg"),"wb") as f: -> have write image data in the binary form inside dictionary format so that we can store in mongodb.
        - pip install -r requirements.txt -> before deployment.  
        
---
