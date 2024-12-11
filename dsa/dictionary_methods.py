#print(dir(dict))

#dictionaries
"""dict = {"my_name" : "krish" ,   "my_age" : 4  , "couse" : "cse"}
for key,value in dict.items():
    print(f"{key} : {value}")


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
  # OR 

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}



print(myfamily)
"""
#dictionary methods 



dict = {"my_name" : "krish" ,   "my_age" : 4  , "couse" : "cse"}


#dict.clear
"""dict.clear()
print(dict)"""
my_dict = { "mew " : 10 , "new": 30 , "kew" : 20}


#dict.copy
"""my_dict= dict.copy()
print(my_dict)"""


#dict = dict.fromkeys(dict["my_name"] , 0) ---  works a new whole dictionary so this wont work
"""dict=dict = dict.fromkeys(dict , 0)
print(dict)
"""


# dict.get

"""y = dict.get("my_name")
print(y)"""

#dict.items - Returns a list containing a tuple for each key value pair
"""x = dict.items()
print(x)  """

#dict.keys - prints the keys for u 
"""z = dict.keys()
dict["color"] = "white" # adds a new key which is also printed 
print(z)"""


#dict.pop - removes the key
"""dict.pop("my_age")

print(dict)"""

#dict.popitem() - removes the last get 
"""dict.popitem()
print(dict)"""

#dict.setdefault(key , value) - 
# so makes a new key if key not present which is the first value dict(x,y) 
#x is the key if x is present it will print the value of x as set in original list but if key not present is will add x as a key with y as value 

"""dict.setdefault("my_caste" , "my_name")
x = dict.setdefault("my_name" ,  "dronkeo")
print(dict)
print(x)"""


#dict.update
"""dict.update({"color": "White"})
print(dict)"""

"""dict.update({"my_name":"Tvish"}) #-- this replaces the already existing key's value :)
print(dict)"""

x = dict.values()

print(x)