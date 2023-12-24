
```markdown
# Lists in Python

A list is a collection that is ordered and changeable, allowing duplicate members.




# Creating a list
numbers = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'grapes', 'pears']

# Using a constructor
numbers2 = list((1, 2, 3, 4, 5))
```

## Accessing List Elements

```python
# Getting a value
print(fruits[1])  # Output: 'oranges'

# Getting the length
print(len(fruits))  # Output: 4
```

## Modifying Lists

```python
# Appending to a list
fruits.append('mangoes')
print(fruits)

# Removing from a list
fruits.remove('pears')
print(fruits)

# Inserting into a specific position
fruits.insert(3, 'strawberries')
print(fruits)

# Changing values
fruits[0] = 'blueberries'
print(fruits)

# Removing with pop
fruits.pop(2)
print(fruits)
```

## List Operations

```python
# Reversing a list
fruits.reverse()
print(fruits)

# Sorting a list
fruits.sort()
print(fruits)

# Reverse sorting a list
fruits.sort(reverse=True)
print(fruits)
```

## List Exercises

```python
# List of states in Nigeria
states_in_nigeria = ['Lagos', 'Abuja', 'Kano', 'Ogun', 'Enugu', 'Rivers', 'Kaduna', 'Ekiti', 'Oyo', 'Delta', 'Borno']

# Get the length of states in Nigeria
length_of_states = len(states_in_nigeria)
print(length_of_states)

# Change the states to uppercase
states_uppercase = [state.upper() for state in states_in_nigeria]
print(states_uppercase)

# Change the states to lowercase
states_lowercase = [state.lower() for state in states_in_nigeria]
print(states_lowercase)

# Reverse sort
states_in_nigeria.sort(reverse=True)
print(states_in_nigeria)

# Get the position of specific states
positions = [states_in_nigeria[9], states_in_nigeria[10], states_in_nigeria[29], states_in_nigeria[1], states_in_nigeria[4]]
print(positions)

# Combine places with capitals
state_capitals = {'Lagos': 'Ikeja', 'Abuja': 'Abuja Capital Territory', 'Kano': 'Kano', 'Ogun': 'Abeokuta', 'Enugu': 'Enugu', 'Rivers': 'Port Harcourt', 'Kaduna': 'Kaduna', 'Ekiti': 'Ado-Ekiti', 'Oyo': 'Ibadan', 'Delta': 'Asaba', 'Borno': 'Maiduguri'}

combined_states_capitals = [f"{state} - {state_capitals[state]}" for state in states_in_nigeria]
print(combined_states_capitals)

# Delete the 7th state and the 25th state
del states_in_nigeria[6]
del states_in_nigeria[24]
print(states_in_nigeria)
```

These examples cover creating lists, accessing and modifying elements, performing list operations, and completing exercises related to a list of states in Nigeria. Understanding these concepts will enhance your proficiency in working with lists in Python.
