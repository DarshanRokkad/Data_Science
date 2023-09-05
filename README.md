# $$\color{lightgreen}\large{\text{Data \ Science}}$$


## $$\text{Python}$$

### $~~~~~~$ Week 1 - Basic Building
##### $~~~~~~~~~~~~~~~~~~~$ 1. Variables.
##### $~~~~~~~~~~~~~~~~~~~$ 2. Mutable and Immutable objects.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - list.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - strings.
##### $~~~~~~~~~~~~~~~~~~~$ 3. Operators.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - arithmetic -> + , - , * , / , % , // .
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - logical -> and , or , not .
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - comparsion -> < , > , <= , >= .
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - bitwise -> & , | , ~ , ^ , << , >>.
##### $~~~~~~~~~~~~~~~~~~~$ 4. Conditional statements.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - if , elif and else.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - is , in , == , != .
##### $~~~~~~~~~~~~~~~~~~~$ 5. Looping 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - for(start,stop,step).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - while(condition).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - while/for else .
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - loop contols -> break , continue and pass.
##

### $~~~~~~$ Week 2 - Data structures 
##### $~~~~~~~~~~~~~~~~~~~$ 1. Print Function.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - print("",var) 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - print(f"{var}") 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - print("{}".format(var))
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - print("{firstname}".format(firstname=var))
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - print returns 'None' type.
##### $~~~~~~~~~~~~~~~~~~~$ 2. input Function.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - input() 
##### $~~~~~~~~~~~~~~~~~~~$ 3. Type casting.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - int(var) 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - float(var) 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - str(var) 
##### $~~~~~~~~~~~~~~~~~~~$ 4. Additional useful functions.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Address -> id(var).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Binary representation -> bin(var).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Deleting variable ->del var.
##### $~~~~~~~~~~~~~~~~~~~$ 5. String.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Strings are immutable.
##### $~~~~~~~~~~~~~~~~~~~$ 6. List.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Lists are Ordered and Mutable list.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - List comprehension.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Shallow copy and Deep copy in 2D array.
##### $~~~~~~~~~~~~~~~~~~~$ 7. Tuple.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Tuples are Ordered but Immutable list.
##### $~~~~~~~~~~~~~~~~~~~$ 8. Set.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Sets are Unordered and Immutable list.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Sets contains Unique elements i.e no duplicates.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - functions -> Subset , Superset , Union , Intersection , Difference , XOR.
##### $~~~~~~~~~~~~~~~~~~~$ 9. Dictionary.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - {key:value} Dictionary is present in the form of Key and value pair.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Dictionary comprehension.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Shallow copy and Deep copy in collections type values.
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

### $~~~~~~$ Week 3 - Functions.
##### $~~~~~~~~~~~~~~~~~~~$ 1.Basics.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - using of pass.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - return values (None , Multiple values).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - return None.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - return Multiple values.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Default arguement function definition.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Keyword arguement function call.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Variable arugement [ def fun(*args) ]. (returns tuple)
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Keyword arugement [ def fun(**kwargs) ]. (returns dictionary)
##### $~~~~~~~~~~~~~~~~~~~$ 2.Generator functions.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - range(start,end,step) genrator function.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - yield.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - To use memory efficiently.
##### $~~~~~~~~~~~~~~~~~~~$ 3.Lambda functions.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Anonymous function(do not have a name).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Short hand of the function and not compulsary to use.
##### $~~~~~~~~~~~~~~~~~~~$ 4.Map , Reduce and Filter.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Map.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Used to map between iterables using mapping function(maper).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Syntax : map(func,*iterable) --> map object.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Reduce.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Specially designed for the function with 2 parameters.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Syntax : reduce(func,iterable,intial value) --> respectively data type.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Filter.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - To Filter out the elements in iterables based on some condition.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Syntax : filter(func,iterable) --> filter object.
##

### $~~~~~~$ Week 4 - OOPS.
##### $~~~~~~~~~~~~~~~~~~~$ 1.Introduction.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Everything is a object in python.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - class \<class name\>.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - self parameter.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Constructor.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Syntax : def \_\_init\_\_(self).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - It will automatically executed when the instance of the class is created.
##### $~~~~~~~~~~~~~~~~~~~$ 2.Polymorphism.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - A single function going to behave differently based on object.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Duck Typing.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Complie time polymorphism.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Method overloading .
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Operator overloading .
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Run time polymorphism.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Method overiding .
##### $~~~~~~~~~~~~~~~~~~~$ 3.Encapsulation.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Binding data and function together in class.(Data + Function).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Private variable -> self.__var = value
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - In python private variables are not truely private.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Can modify the private variable -> obj._classname__var = value
##### $~~~~~~~~~~~~~~~~~~~$ 4.Inheritance.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - The method of aquiring the properties of the parent class to the child class.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Use : Code reusability.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Syntax : class child(parent):
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Types: 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 1.Multilevel Inheritance. 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 2.Multiple Inheritance. 
##### $~~~~~~~~~~~~~~~~~~~$ 5.Abstract class.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Abstract method will give the blue print of the class and who want to use can inherit then implement and use it.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - import abc.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Annotation -> @abc.abstractmethod
##### $~~~~~~~~~~~~~~~~~~~$ 6.Decorator.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Decorator is used to add additional functionality to the function and avoid repeatative code. 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Annotation -> @decorator_function 
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Calculating Time taken(import time).
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - time.time() -> Gives the current time.
##### $~~~~~~~~~~~~~~~~~~~$ 7.Class variables and methods.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Used to pass data to class or access data from class without using \_\_init\_\_ method.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Anotation -> @classmethod.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - These are common to all the objects of that class.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - We can make external function as the class method.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - \<classname\>.\<functionname\> = classmethod(\<function name\>)
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - To delete class variable or class methods.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - delattr(\<class name\>,\<variable/function name\>)
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - del \<variable/function name\>
##### $~~~~~~~~~~~~~~~~~~~$ 8.Static methods.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Used to reduce memory utilization.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Anotation -> @staticmethod.
##### $~~~~~~~~~~~~~~~~~~~$ 9.Magic methods.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Magic or Dunder methods.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Adivsed to not to use dunder method.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - internally \_\_new\_\_ is called before \_\_init\_\_.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - dir(data_type) -> gives all the inbuilt function present in that data type class.
##### $~~~~~~~~~~~~~~~~~~~$ 10.Property decorator.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Property is a decorator used to access or modify or delete the private or protected variable outside the class.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 1.Getter.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Anotation -> @property
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 2.Setter.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Anotation -> @\<access function\>.setter
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ 3.Deleter.
###### $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$ - Anotation -> @\<access function\>.deleter

---
