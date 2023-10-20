# Files and Exception handling and Memory management
1. Working with files.
    - ```pwd``` -> present working directory.
    - ```ls``` -> list of files present in the current folder.
    - ```f = open(filename,mode)```
    - ```f.close()``` -> We have to close the file after using.
    - ```with open(file name , mode) as f``` -> file will be automatically opened and closed.
    - write operation.
        - Syntax -> ```f.write(content)```
        - Erases the data if it is present in previously.
    - read operation.
        - Syntax -> ```data = f.read(content)```
    - append operation.
        - Syntax -> ```f.write(content)```
        - Adds the content to the end of the file.
    - ```f.seek(position)``` -> bring pointer to certian index.
    - ```f.tell()``` -> returns the position of the pointer.
    - ```os.path.getsize(filename)``` -> gives the size of the file.[import shutil]
    - ```shutil.copy(old,new)``` -> copy content of one file to another.[import stutil]
    - ```os.remove(filename)``` -> deletes the file.
    - ```os.rename(old,new)``` -> rename the file.  

2. File reading and writing.
    - json.
        - ```import json```
        - write -> ```json.dump(data,f)``` 
        - read -> ```data = json.load(f)```
    - csv.
        - ```import csv```
        - write -> ```w = csv.writer(f)``` and  w.writerow(i).
        - read -> ```r = csv.reader(f```) and for i in r:
    - binary.
        - write -> ```f.write(b'data')```
        - read -> ```print(f.read())```  

3. Buffered read and write other file methods.
    - ```import io```.
    - Write -> ```file = io.BufferedWriter(f)``` and ```file.write(data)```
    - Read -> ```file = io.BufferedReader(f)``` and ```data = file.read(chucks)```  

4. Logging and Debugger.
    - We can use logging to debug the code.
    - ```import logging```.
    - Creating a log file -> ```logging.basicConfig(filename='file.log',level=logging.level)```.
    - logging -> ```loggging.level(message)```.
    - Hierarchy of logging levels.
        1. NOSET.
        2. DEBUG.
        3. INFO.
        4. WARNING.
        5. ERROR.
        6. CRITICAL.  

5. Modules and import statement.
    - folder -> package.
    - file -> module.
    - methods are present inside the module.
    - from package import module.  

6. Exception handling.
    - ```try```.
    - ```except``` -> except Exception as e.
        - Exception class in the inbuilt class for handling exceptions.
    - ```else``` -> this block execute only on successfull execution of try block.
    - ```finally``` -> this block will execute always.
    - Custom exception handling.
        - ```class classname(Exception)``` -> have to inherit Exception class.
        - ```raise classname(message)``` -> this constructor should have variable to store this message.
    - Other general exceptions.
    - Best Practise of Exception Handling.
        - Use always a specific exception.
        - Print always a valid message.
        - Always log the error.
        - Always avoid to write multiple exception handling.
        - Prepare documentation.
        - Cleanup all the resources.  

7. Multithreading.
    - Used to execute multiple process concurrently.
    - ```import threading```.
    - Thread functions. 
        - ```threading.Thread(target=function_name,args=(args))```
        - ```var.start()``` -> starts thread.
        - ```threading.Lock()```
    - ```time.sleep(sec)``` -> Thread will sleep for some seconds [import time]. 
    - for downloading files.
        - ```import urllib.request```
        - ```urllib.request.urlretrieve(url,file_name)```  

8. Multiprocessing.
    - multiprocessing.Process(target = function_name) -> create the multiple processes.
        - ```m.start()``` 
        - ```m.join()``` 
    - ```with multiprocessing.Pool(processes = number) as pool:``` -> Pool of process
        - ```var = pool.map(func,iterable)```
    - ```multiprocessing.Queue()``` -> Use of Queue 
        - ```q.put(item)```
        - ```q.get()```
    - ```multiprocessing.Array('var',iterable)``` -> synchronized shared array.
    - ```multiprocessing.Pipe()``` -> returns 2 objects.
        - Use of send and recieve connection(In whatsapp messaging ).
        - ```connection.send(msg)```
        - ```connection.recv()```  
