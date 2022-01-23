# a loop is used for iterating over a sequence that is either a list tuple, a dictionary, a set and a string 
people = [ 'john', 'paul', 'sara','susan']

# simple for loop
for person in people:
    print(f'current person : {person}')
#break 
for person in people:
    if person == 'sara':
        break
    print(f'current person : {person}')

# continue 
for person in people:
    if person == 'sara':
        continue
    print (f'current person :{person}')
# range 
for i in range (len(people)):
    print(people[i])
for i in range (1,10):
    print(f'numbers: {i}')

# while loop execute a set of statement so far the conditions are true 
count = 10
while count < 100 * 100:
    print (f'count:{count}')
    count += 1


