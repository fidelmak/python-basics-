## class in python 

```markdown
# Classes and Objects in Python

A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in Python is an object.

## Creating a Class

```python
class Client:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def greetings(self):
        return f"My name is {self.name} and I am {self.age} years old."

    def has_birthday(self):
        return f"My birthday ought to be next week, but Mr. {self.name} forgot to announce it while he is {self.age} years old."

    def new_date(self):
        self.age += 1
```

## Extending a Class

```python
class Customer:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0

    def greetings(self):
        return f"My name is {self.name}, I am {self.age} years old, and my balance is {self.balance}."

    def set_balance(self, balance):
        self.balance = balance
```

## Using the Classes

```python
# Creating an object from the extended class
janet = Customer('Janet John', 56, 'johnjanet@email')

# Setting balance for Janet
janet.set_balance(15000)

# Printing Janet's greetings
print(janet.greetings())
```

```python
# Creating an object from the initial class
p1 = Client('Paul Fidelis', 37, 'paulfidelis@gmail.com')

# Updating the age with the new_date method
p1.new_date()

# Printing Paul's greetings and birthday announcement
print(p1.greetings())
print(p1.has_birthday())
```

In Python, a class is like a blueprint that helps us create objects. Each object can have its own unique properties and behaviors. For example, we have a class called `Client` with a method to announce birthdays, and we also have an extended class called `Customer` that can track a person's balance. We create objects from these classes, like 'Janet' and 'Paul,' and use their methods to interact with their properties.





## Major aspects in Python 

The four pillars of object-oriented programming (OOP) are:

1. **Encapsulation:** This is the concept of bundling the data (attributes) and methods (functions) that operate on the data into a single unit called a class. Encapsulation helps in controlling access to the data and prevents accidental modification.

    **Example:**
    
    ```python
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print("Woof!")

    # Creating an object
    my_dog = Dog("Buddy", 3)

    # Accessing attributes
    print(my_dog.name)  # Output: Buddy

    # Calling a method
    my_dog.bark()  # Output: Woof!
    ```

2. **Abstraction:** Abstraction involves hiding the complex implementation details and exposing only the essential features of an object. It allows users to interact with the object without needing to understand its internal workings.

    **Example:**
    
    ```python
    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

    # Creating an object
    my_circle = Circle(5)

    # Calling the abstract method
    print(my_circle.area())  # Output: 78.5
    ```

3. **Inheritance:** Inheritance is a mechanism that allows a class to inherit properties and behaviors from another class. The class that is inherited from is called the parent or base class, and the class that inherits is called the child or derived class.

    **Example:**
    
    ```python
    class Animal:
        def __init__(self, species):
            self.species = species

        def make_sound(self):
            pass

    class Dog(Animal):
        def make_sound(self):
            return "Woof!"

    class Cat(Animal):
        def make_sound(self):
            return "Meow!"

    # Creating objects
    my_dog = Dog("Canine")
    my_cat = Cat("Feline")

    # Accessing inherited attribute
    print(my_dog.species)  # Output: Canine

    # Calling inherited method
    print(my_dog.make_sound())  # Output: Woof!
    ```

4. **Polymorphism:** Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables a single interface to represent different types or forms.

    **Example:**
    
    ```python
    class Bird:
        def fly(self):
            pass

    class Sparrow(Bird):
        def fly(self):
            return "Sparrow is flying."

    class Penguin(Bird):
        def fly(self):
            return "Penguin cannot fly."

    # Creating objects
    sparrow = Sparrow()
    penguin = Penguin()

    # Using polymorphism
    bird_list = [sparrow, penguin]

    for bird in bird_list:
        print(bird.fly())
    ```

These examples illustrate the core concepts of OOP using Python. Practicing with these examples can help reinforce your understanding of encapsulation, abstraction, inheritance, and polymorphism.










## Using Static in Class 
In Python, the term "static" is used in the context of class attributes or methods, and it's related to the concept of class-level members. Let's break down the key aspects:

### Static Variables (Class Variables):

Static variables are shared among all instances of a class. They belong to the class rather than an instance of the class. These variables are defined using the `@staticmethod` decorator or by defining them directly within the class.

**Example:**
```python
class MyClass:
    static_variable = 10  # Static variable

    def __init__(self, value):
        self.value = value  # Instance variable

    @staticmethod
    def static_method():
        print("This is a static method.")

# Accessing static variable
print(MyClass.static_variable)  # Output: 10

# Creating instances
obj1 = MyClass(5)
obj2 = MyClass(8)

# Accessing instance variable
print(obj1.value)  # Output: 5

# Accessing static variable through an instance (not recommended)
print(obj1.static_variable)  # Output: 10

# Accessing static variable through the class
print(MyClass.static_variable)  # Output: 10

# Calling static method
MyClass.static_method()  # Output: This is a static method.
```

### Static Methods:

Static methods are methods that are bound to a class rather than an instance of the class. They are defined using the `@staticmethod` decorator. Unlike regular methods, static methods don't have access to the instance or its attributes.

**Example:**
```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

# Calling static methods
result_add = MathOperations.add(3, 5)
result_multiply = MathOperations.multiply(2, 4)

print(result_add)       # Output: 8
print(result_multiply)  # Output: 8
```

### Use Cases for Static:

1. **Shared Information:** Static variables are useful when you want to share information among all instances of a class.

2. **Utility Functions:** Static methods are handy for utility functions related to the class but don't depend on instance-specific data.

3. **Constants:** Static variables can be used to define constants that remain the same for all instances.

It's important to note that while static methods and variables are accessible through instances, it's recommended to access them through the class itself, as this makes the code more readable and avoids potential confusion with instance-specific data.



















## Creating Libraries in Python using Class 
Creating a library using classes in Python involves organizing related functionalities into classes and modules, allowing users to easily import and use the library in their projects. Below is a step-by-step guide to creating a simple library using classes:

### Step 1: Define a Class

Start by defining classes that encapsulate related functionalities. Each class represents a specific module or category of features.

**Example: `MathOperations` class for mathematical operations:**
```python
# math_operations.py

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")
```

### Step 2: Create a Module

A module is a file that contains Python code. Each class should be defined in a separate module. Save the `MathOperations` class in a file named `math_operations.py`.

### Step 3: Use the Library

Now, users can import and use the library by importing the desired module (class) into their Python scripts or projects.

**Example: Using the `MathOperations` class in another script:**
```python
# main_script.py
from math_operations import MathOperations

# Create an instance of MathOperations
calculator = MathOperations()

# Use the methods of the class
result_add = calculator.add(3, 5)
result_subtract = calculator.subtract(8, 4)

print("Addition Result:", result_add)          # Output: Addition Result: 8
print("Subtraction Result:", result_subtract)   # Output: Subtraction Result: 4
```

### Step 4: Package the Library (Optional)

If your library grows more complex and includes multiple modules, you might want to organize them into a package. A package is a directory that contains multiple modules and a special `__init__.py` file.

**Example: Directory structure for a library named `mylibrary`:**
```
mylibrary/
│   __init__.py
│   math_operations.py
│   other_module.py
```

Users can then import modules from the package:

```python
# main_script.py
from mylibrary.math_operations import MathOperations
from mylibrary.other_module import SomeFunctionality
```

### Step 5: Distribute the Library (Optional)

If you want others to use your library, you can package and distribute it using tools like `setuptools` and upload it to the Python Package Index (PyPI).

Creating a library using classes in Python follows these steps, making it modular, reusable, and easy to maintain. It provides users with a clean and organized way to access specific functionalities within the library.
