
---

# Introduction to Variables

A variable serves as a container for a value, accommodating various types. The following multiline comment or docstring provides insight into its definition, allowing for both single and double quotes.

```python
"""
A variable is a container for a value, which can be of various types.
This is a multiline comment or docstring (used to define a function purpose).
It can be single or double quotes.
"""
```

## Variable Rules

- Variable names are case-sensitive (e.g., "Name" and "name" are distinct variables).
- Variables must commence with a letter or an underscore.
- Numeric characters are permissible but cannot initiate a variable name.

```python
"""
- Variable names are case-sensitive (Name and name are different variables).
- Must start with a letter or an underscore.
- Can have numbers but cannot start with one.
"""
```

## Multiple Assignment

The code segment below exemplifies the concept of multiple assignment, whereby values are simultaneously assigned to variables `x`, `y`, `name`, and `is_cool`.

```python
x, y, name, is_cool = (1, 2.5, 'john', True)
```

## Basic Math

Performing basic mathematical operations, the subsequent code computes the sum of variables `x` and `y`, storing the result in the variable `sum_ab`.

```python
sum_ab = x + y
```

## Casting

Demonstrating casting operations, the code converts the variable `x` to a string, `y` to an integer, and then to a float. The resulting type and value of `z` are subsequently printed.

```python
x = str(x)
y = int(y)
z = float(y)
print(type(z), z)
```

## Additional Operations

Introducing new variables `A`, `B`, and `C`, the code conducts various operations, including the calculation of the sum of `A` and `B`, as well as the computation of the remainder of the division of `B` by `C`.

```python
A = 10
B = 5
C = 3

sum_ab = A + B
remainder_bc = B % C
```

## Multiplication and Type Printing

The ensuing code multiplies the sum (`sum_ab`) by the remainder (`remainder_bc`) and assigns the result to the variable `multiplication_result`. Additionally, it prints the type and value of `multiplication_result`.

```python
multiplication_result = sum_ab * remainder_bc
print(type(multiplication_result), multiplication_result)
```

---
