def course_method():
    print('This is course file.')

# To colapse the path of the file 
import os , sys 
from os.path import dirname , join , abspath 
sys.path.insert(0,abspath(join(dirname(__file__),'..')))

from  payment_folder import payment_file

payment_file.payment_method()