

```markdown
# Tuples in Python

A tuple is a collection that is ordered and unchangeable. It allows duplicate members.

## Creating Tuples

```python
# Creating a tuple
fruits = ('apples', 'oranges', 'grapes', 'pears')

# Using a constructor
fruits2 = tuple(('apples', 'grapes', 'oranges', 'pears'))
print(fruits, fruits2)
```

In a tuple, values are enclosed within parentheses `()`.

```python
# Single value needs a trailing comma
# fruit = ('apples',)
# print(fruit, type(fruit))
```

When creating a tuple with a single value, a trailing comma is needed to distinguish it from a regular value in parentheses.

## Accessing Tuple Elements

```python
# Getting a value
print(fruits[1])  # Output: 'oranges'

# Can't change values
# fruits[0] = 'pears'
```

Tuples are immutable, meaning you cannot change their values once they are defined.

```python
# Getting the length
print(len(fruits))  # Output: 4
```

## Sets in Python

A set is a collection that is ordered and unindexed, with no duplicate members.

## Creating Sets

```python
# Creating a set
fruit_set = {'apples', 'oranges', 'pears', 'mango'}

# Checking if 'apples' is in the set
print('apples' in fruit_set)  # Output: True
```

Sets use curly braces `{}` and are defined with unique values.

```python
# Adding to a set
fruit_set.add('pawpaw')
print(fruit_set)  # Output: {'apples', 'oranges', 'pears', 'mango', 'pawpaw'}
```

You can add elements to a set using the `add` method.

```python
# Duplicate set element (no effect)
fruit_set.add('apples')
print(fruit_set)  # Output: {'apples', 'oranges', 'pears', 'mango', 'pawpaw'}
```

Sets automatically handle duplicate values by ignoring them.

```python
# Clearing a set
fruit_set.clear()
print(fruit_set)  # Output: set()
```

The `clear` method removes all elements from the set.

```python
# Deleting a set
del fruit_set
# print(fruit_set)  # Uncommenting this line would result in an error since the set no longer exists
```

The `del` keyword deletes the set entirely.

These examples cover creating tuples, accessing elements, and working with sets in Python. Understanding these concepts will help you effectively use tuples and sets in your Python programs.
```
