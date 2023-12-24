# A function is a block of code which only runs when it is called .
# in python , we do not use curly brackets , we use identations with tabs or spaces 
# create a function 
 
# to define a function use 
def sayHello(name='sam'):
    print (f'Hello {name}')
# to call a function use 
sayHello()

# information can be passed as argument 

def my_function(fname):
    print(fname + " Badmus " )
my_function('emil')
my_function(' paul ')
my_function('john ')


# another example 
def getSum(num1 , num2):
    total = num1 + num2 
    return total
print(getSum(24, 44))

# lambda function 
# a lambda function can take any  number of arguments, but can only have one expression 
# very similar to Js arrow function 
getSum = lambda num1, num2: num1 + num2
print(getSum(2, 4 ))