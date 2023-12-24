## Loops in Python

```markdown
# Loops in Python

A loop is used for iterating over a sequence, which can be a list, tuple, dictionary, set, or string.


people = ['john', 'paul', 'sara', 'susan']
```

## For Loop

```python
# Simple for loop
for person in people:
    print(f'Current person: {person}')

# Break statement
for person in people:
    if person == 'sara':
        break
    print(f'Current person: {person}')

# Continue statement
for person in people:
    if person == 'sara':
        continue
    print(f'Current person: {person}')
```

## Range and For Loop

```python
# Using range with for loop
for i in range(len(people)):
    print(people[i])

# Another range example
for i in range(1, 10):
    print(f'Numbers: {i}')
```

## While Loop

```python
# While loop executes a set of statements as long as the condition is true
count = 10
while count < 100 * 100:
    print(f'Count: {count}')
    count += 1
```

Loops are essential for iterating through data structures and executing a set of statements repeatedly. Understanding how to use `for` loops with different sequences and how to use `while` loops is crucial for efficient and dynamic programming.

```python
# Displaying results
```

These examples cover `for` loops, `break` and `continue` statements within loops, using `range` with loops, and implementing a `while` loop in Python.
