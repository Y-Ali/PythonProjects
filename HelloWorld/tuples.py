#how to add things to tuples
#this is a tuple:
essentials = ('bread', 'coffee', 'wifi')
print(essentials)

#first change the tuple to a List
newList = list(essentials)
print(newList)

#append something to the list, then change the list to a tuple.
newList.append("123")
newList = tuple(newList)

#changed tuple
essentials = newList
print(essentials)








