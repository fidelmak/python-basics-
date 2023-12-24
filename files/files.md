## Files in Python 

```markdown
# File Operations in Python

Python has functions for creating, reading, and updating files.

```python
# Open a file
myfile = open('myTxt.txt', 'w')

# Get information from the file
print('Name:', myfile.name)
print('Is closed:', myfile.closed)
print('Opening mode:', myfile.mode)
```

## Writing to a File

```python
# Let's write to the file
myfile.write('I love Python ')
myfile.write('and JavaScript')
myfile.close()
```

## Appending to a File

```python
# Let's append to the file
myfile = open('myTxt.txt', 'a')
myfile.write(' I prayed to God to clear my debt, and He did')
myfile.close()
```

## Reading from a File

```python
# To read from the file
myfile = open('myTxt.txt', 'r+')
text = myfile.read(100)
print(text)
```

File operations in Python allow you to create, write, and read from files. Understanding how to use file handling functions is crucial for working with external data and persisting information.

These examples cover opening a file, getting information about the file, writing to a file, appending to a file, and reading from a file in Python.
