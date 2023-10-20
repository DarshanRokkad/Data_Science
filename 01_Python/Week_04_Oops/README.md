# OOPS
1. Introduction.
    - Everything is a object in python.
    - class class name.
    - self parameter.
    - Constructor.
        - Syntax : ```def \_\_init\_\_(self)```.
        - It will automatically executed when the instance of the class is created.  

2. Polymorphism.
    - A single function going to behave differently based on object.
    - Duck Typing.
    - Compile time polymorphism.
        - Method overloading .
        - Operator overloading .
    - Run time polymorphism.
        - Method overiding .  

3. Encapsulation.
    - Binding data and function together in class.(Data + Function).
    - Private variable -> ```self.__var = value```
    - In python private variables are not truely private.
        - Can modify the private variable -> ```obj._classname__var = value``` 

4. Inheritance.
    - The method of aquiring the properties of the parent class to the child class.
    - Use : Code reusability.
    - Syntax : ```class child(parent):```
    - Types:  
        1. Multilevel Inheritance. 
        2. Multiple Inheritance.  

5. Abstract class.
    - Abstract method will give the blue print of the class and who want to use can inherit then implement and use it.
    - ```import abc```.
    - Annotation -> ```@abc.abstractmethod```  

6. Decorator.
    - Decorator is used to add additional functionality to the function and avoid repeatative code. 
    - Annotation -> ```@decorator_function``` 
    - Calculating Time taken(```import time```).
        - ```time.time()``` -> Gives the current time.  

7. Class variables and methods.
    - Used to pass data to class or access data from class without using \_\_init\_\_ method.
    - Anotation -> ```@classmethod```.
    - These are common to all the objects of that class.
    - We can make external function as the class method.
        - ```classname.functionname = classmethod(function name)```
    - To delete class variable or class methods.
        - ```delattr(class name,variable/function name)```
        - ```del variable/function name```  

8. Static methods.
    - Used to reduce memory utilization.
    - Anotation -> ```@staticmethod```.  

9. Magic methods.
    - Magic or Dunder methods.
    - Adivsed to not to use dunder method.
    - internally \_\_new\_\_ is called before \_\_init\_\_.
    - ```dir(data_type)``` -> gives all the inbuilt function present in that data type class.  

10. Property decorator.
    - Property is a decorator used to access or modify or delete the private or protected variable outside the class.  
    
    a. Getter.  
        - Anotation -> ```@property```  
    b. Setter.  
        - Anotation -> ```@access function.setter```  
    c. Deleter.  
        - Anotation -> ```@access function.deleter```  
