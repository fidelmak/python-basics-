# a tuple is a collection which is ordered and unchangeable 
#  it allows duplicate member.
# create a turple 
fruits = ('apples','oranges', 'grapes', 'pears')
# we can also use a constructor
fruits2 = tuple(('apples','grapes','ornages','pears'))
print(fruits,fruits2)

# single value needs a trailing comma
#fruit = ('apples',)
#print(fruit, type(fruit))
# getting a value
print(fruits[1])
# can't change values
#fruits[0] ='pears'
# get length
print(len(fruits))

# A set is a collection which is ordered and unindexed , No duplicate members

#create a set
fruit_set =  {'apples', 'oranges','pears','mango'}
#check if its in set
print('apples' in fruit_set)
# adding to a set
fruit_set.add('pawpaw')
print(fruit_set)
#duplicatw set 
fruit_set.add('apples')
print(fruit_set)
#clear a set 
fruit_set.clear()
print(fruit_set)
# to delete a set
del fruit_set
print(fruit_set)