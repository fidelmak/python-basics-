class client:
    def __init__(self, name, email, age):
        self.name= name
        self.email= email
        self.age = age
    def greetings(self):
        return f'my name is {self.name} and i am {self.age}'

    Paul = client('paul fidelis', 'paulfidelis@gmail.com', 37 )
    
print(paul.greetings)    