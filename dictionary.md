

```markdown
# Dictionaries in Python

A dictionary is a collection that is unordered, changeable, and indexed. It does not allow duplicate members.

## Creating Dictionaries

```python
# Creating a dictionary
person = {
    'first_name': 'john',
    'last_name': 'Doe',
    'age': 30
}
# print(person)
```

Dictionaries are defined using curly braces `{}` and consist of key-value pairs.

```python
# Using a constructor
person2 = dict(first_name='sara', last_name='williams')
# print(person2)
```

Dictionaries can also be created using the `dict` constructor.

## Accessing Dictionary Elements

```python
# Getting values
print(person['first_name'])  # Output: 'john'
print(person.get('last_name'))  # Output: 'Doe'
```

You can access values using keys in square brackets or the `get` method.

## Modifying Dictionaries

```python
# Adding key/value
person['phone'] = '09019910189'
# Printing the values for person
print(person)

# Getting dictionary keys and values
print(person.items())
```

You can add key-value pairs and retrieve keys and values using the `items` method.

```python
# Copying a dictionary
person3 = person.copy()
print(person3)
person3['city'] = 'boston'
print(person3)
```

You can copy a dictionary using the `copy` method and modify the copied dictionary.

```python
# Removing an item
del person['age']
print(person)

# Or use
person.pop('phone')
print(person)
```

You can delete items from a dictionary using `del` or `pop`.

## List of Dictionaries

```python
# Creating a list of dictionaries
people = [
    {'name': 'martha', 'age': 30},
    {'name': 'kelvin', 'age': 40}
]
print(people)
```

You can have a list of dictionaries, each representing an individual.

```python
# Getting a particular value
print(people[1]['name'])  # Output: 'kelvin'
print(people[0]['age'])  # Output: 30
```

You can access specific values within the list of dictionaries.

This covers creating dictionaries, accessing elements, modifying dictionaries, and working with lists of dictionaries in Python.
```
