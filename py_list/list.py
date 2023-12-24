# A list is a collection which is ordered and changeable . Allows duplicate members
 
#create list 
numbers = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'grapes','pears']

# use a constructor 
numbers2 = list((1,2,3,4,5))
#print(fruits, numbers, numbers2)

# to get a value
print(fruits[1])
# get length
print(len(fruits))
# Append to list 
fruits.append('mangoes')
print(fruits)
# remove from a list 
fruits.remove('pears')
print(fruits)
# insert into position 
fruits.insert(3, 'strawberries')
print(fruits)
# change values
fruits[0] = 'blueberries'
print(fruits)
# remove with pop
fruits.pop(2)
print(fruits)
# reverse list 
fruits.reverse()
print(fruits)
#sort list
fruits.sort()
print(fruits)
# reverse sort 
fruits.sort(reverse=True)
print(fruits)

# here are your exercises
# make a lists of states in nigeria 
# get the lenght of states in nigeria 
# change the states to uppercase
# change the states to lowercase
# do a reverse sort
# get the position of the 10th, 11th, 30th, 2nd and 5th state in Nigeria
# change all the states to with their capitals 
# delete the 7th state and the 25th state   
 