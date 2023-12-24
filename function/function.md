## Function in Python 

```markdown
# Functions in Python

A function is a block of code that only runs when it is called. In Python, we use indentation with tabs or spaces instead of curly brackets.

## Creating a Function

```python
# To define a function, use
def sayHello(name='sam'):
    print(f'Hello {name}')
```

## Calling a Function

```python
# To call a function, use
sayHello()
```

## Passing Information as Arguments

```python
# Information can be passed as an argument
def my_function(fname):
    print(fname + " Badmus ")

my_function('emil')
my_function('paul')
my_function('john')
```

## Function with Multiple Arguments and Return Statement

```python
# Another example
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(24, 44))
```

## Lambda Function

```python
# Lambda function
# A lambda function can take any number of arguments but can only have one expression
# Very similar to JS arrow function
getSum = lambda num1, num2: num1 + num2
print(getSum(2, 4))
```

Functions in Python are essential for organizing and reusing code. They allow you to modularize your code, making it more readable and maintainable.

These examples cover creating functions, calling functions, passing information as arguments, using functions with multiple arguments, and using lambda functions in Python.
