# a class is like a blueprint for creating objects
# an object has properties and methods (function ) associated with it. almost everything in python is an object
# create a class
#class MyClass:
 #   x = 5
#p1 = MyClass()
class client:
    def __init__(self, name, age, email):
        self.name = name
        self.age= age
        self.email = email
    def greetings(self):
        return f'my name is {self.name} and i am {self.age}'
    # lets add another method 
    def has_birthday(self):
        return f'my birthday ought to be next we but mr {self.name} forgot to anounce it while he is {self.age}'
    # lets add a new object to it 
    def new_date(self):
        self.age+=1
#we can also extend a class
class customer():
    def __init__(self, name, age, email):
        self.name = name
        self.age= age
        self.email = email
        self.balance = 0
    def greetings(self):
        return f'my nsme is {self.name} and i am {self.age} my balance is {self.balance}'
    def set_balance(self, balance):
        self.balance= balance 
    # init an object
janet = customer('janet john', 56, "johnjanet@email" )

janet.set_balance(15000)
print(janet.greetings())

p1 = client('paul fidelis',  37, 'paulfidelis@gmail.com' )
p1.new_date()
print(p1.greetings())
print(p1.has_birthday())

   