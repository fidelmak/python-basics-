
```markdown
# If/Else Conditions in Python

If/else conditions are used to decide to do something based on something being true or false.

```python
x = 9
y = 69
w = 6
```

## Comparison Operators

Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) are used to compare values.

```python
# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# If/else statement
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

# Elif statement
if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')

# Nested if statement
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')
```

## Logical Operators

Logical operators (`and`, `or`, `not`) are used to combine conditional statements.

```python
# And
if w > 2 and w <= 10:
    print(f'{w} is greater than 2 and less than or equal to 10')

# Or
if w > 2 or w <= 10:
    print(f'{w} is greater than 2 or less than or equal to 10')

# Not
if not(x == y):
    print(f'{w} is not equal to {y}')
```

## Membership Operators

Membership operators (`in`, `not in`) check if a value is present in a sequence.

```python
numbers = [1, 2, 3, 4, 5, 6, 7]

# In
if w in numbers:
    print(w in numbers)

# Not in
if y not in numbers:
    print(y not in numbers)
```

## Identity Operators

Identity operators (`is`, `is not`) check if two objects are the same or not.

```python
# Is
if w is y:
    print(w is y)

# Is not
if w is not y:
    print(w is not y)
```

These examples cover if/else conditions, comparison operators, logical operators, membership operators, and identity operators in Python. Understanding these concepts will help you make decisions based on different conditions in your programs.
