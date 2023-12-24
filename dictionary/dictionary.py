# dictionary is a collection which is unordered, changeable and indexed.No duplicate members

# create dict
person = {
    'first_name': 'john',
    'last_name': ' Doe',
    'age': 30
}
#print(person)
# using a constructor 
person2= dict(first_name='sara', last_name='williams')
#print(person2)

# get value 
print(person['first_name'])
print(person.get('last_name'))
#Add Key/value 
person['phone']='09019910189'
# printing the values for person 
print(person)
# to get dict keys 
print(person.items())
# to copy dict 
person3 = person.copy()
print(person3)
person3['city']= 'boston'
print(person3)
# to remove an item 

del(person['age'])
print(person)

# or use 
person.pop('phone')
print(person)

# to create a lists of  dictionaries 
people = [
    {'name': 'martha' , 'age': 30},
    
    {'name':'kelvin', 'age': 40}
]
print(people)
# to get a particular value 
print(people[1]['name'])
print(people[0]['age'])

#assignment 
