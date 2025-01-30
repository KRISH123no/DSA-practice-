"""abs function"""# - #Returns the absolute value of a number
x = abs(-7.25)
print(x)

"""all function""" #- 	#Returns True if all items in an iterable object are true
mylist = [True, True, True]
x = all(mylist)
print(x)
#or
mylist = [0, 1, 1]
x = all(mylist)
print(x) # Returns False because 0 is the same as False




"""any function""" #- Returns True if any item in an iterable object is true
mylist = [False, True, False]
x = any(mylist)
#1 - true
#0 - false

"""ascii()""" #-	Returns a readable version of an object. Replaces none-ascii characters with escape character
x = ascii("My name is Ståle")
print(x)



"""bin()"""#-	Returns the binary version of a number
x = bin(36)
print(x)

# The result will always have the prefix 0b


"""bool()"""#-	Returns the boolean value of the specified object
x = bool(1)
print(x)

"""complex function"""
x = complex(3, 5)
print(x)

"""filter function"""
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)

"""map"""
def myfunc(a):
  return len(a) 

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))


"reduce - getting one value from the list"# for this u have to  - from funools import reduce
from functools import reduce
nums = [ 54,32,23,23,23,23,23]
def sum(a,b):
  return a+b
sum = reduce(sum,nums)
print(sum) 