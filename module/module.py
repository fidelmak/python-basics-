# lets talk about module which is basically a file  containing a set of fuctions to include in your
# application . there are core python modules you can install using the pip package manager including 
# flask and django as well as a custom modules 
import datetime
# we can also use import
from datetime import date
import time
from time import time 
# we can use the from to import time 
#today = datetime.date.today()
today= date.today()
timestamp = time()
# using pip module basically for installing packages in python 
from camelcase import CamelCase

c = CamelCase()
print(c.hump('hello there world'))

import validator
from validator import validate_email

email='tes@email.com'
if validate_email(email):
    print('email is valid')
else:
    print('email is invalid')

# pip install email validator

print(today)
print(timestamp)

