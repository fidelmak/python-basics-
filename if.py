# If/ else conditions are used to decide to do something based on something being true or false 

x= 9
y = 69
w = 6


# comparison Operators (==, !=, >,<, >=, <=)- are used to compare values 

# simple if 
if x > y:
    print(f'{x} is greater than {y}')
# if / else statement
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# elif statement 
if x > y:
    print (f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# nexted if statement 
if x > 2:
    if x <= 10:
        print (f'{x} is greater than 2 and less than or equal to 10')
# logical operators (and , or, not )-- this is used to combine conditional statements 

# and 
if w > 2 and w <=10:
    print(f'{w} is greater than 2 and less than or equal to 10')
# or 
if w > 2 or w <=10:
    print(f'{w} is greater than 2 or less than or equal to 10')
# not
if not(x==y):
    print(f'{w} is not equal to {y}')
# membership operators  (not, not in )
numbers = [1,2,3,4,5,6,7]
# in 
if w in numbers:
    print(w in numbers )
# not in 
if y not in numbers:
    print(y not in numbers )
# identity operator  (is , is not )
# is 
if w is y:
    print(w is y )

#is not 
if w is not y:
    print(w is  not y )


