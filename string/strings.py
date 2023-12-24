# strings in python are surrounded by either single or double quotation marks . lets look 
# at string formatting and some string metods 

name = 'Paul'
age = 37

# Concatenate
print('Hello, my name is ' + name + ' and i am ' + str(age))

# string formatting
#argument by position 
print('my name is {name} and i am {age}'.format(name=name, age=age))
 # f-strings 
print(f'hello, my name is {name} and i am {age}')

#string methods
s = 'helloworld'

# capitalize string
print(s.capitalize())
# make all upper case
print(s.upper())
# make all lower case
print(s.lower())
# swapCase
print(s.swapcase())
#get length
print(len(s))
#replace 
print(s.replace('world', 'everyone'))
#count 
sub = 'h'
print(s.count(sub))
#start with 
print(s.startswith('hello'))
#end with 
print(s.endswith('world'))
#split into a list 
print(s.split())
#find position
print(s.find('r'))
#is all alphanumeric
print(s.isalnum())
# is all alphabetic
print(s.isalpha())
# is all numeric
print(s.isnumeric())

# here are your exercises 
# create a vaiable about your self using Name, age, day of birth, occupation, email, home address, phone number and relationship
# using f string concatenate with a statement about yourself 
# create a variable that explains your perception about the transfer window in 11 words 
# using split , split the variable
# get the lenght of the variable 
# verify whether is alphanumeric, numeric