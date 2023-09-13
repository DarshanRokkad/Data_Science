def payment_method():
    print('This is a payment file')

# To colapse the path of the file 
import os , sys 
from os.path import dirname , join , abspath 
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from course_folder import course_file
course_file.course_method()