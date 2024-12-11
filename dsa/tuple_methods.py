#tuple unlike list is unchangeable and ordered to add or remove something we first have to convert to a list 
#tuples can be added like list 
"""thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(thistuple[1])"""


# to add/remove/replace changes in a tuple     
"""x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)"""

#tuple methods 
print(dir(tuple))

#tuple count - number of times a specified value occurs in a tuple
"""thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)"""

#tuple.index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)