#print(dir(list))-- to check all methods
#use list.add/extend
"""list1 = [1,4,5]
list2=[4,7,8]
newlist= list.__add__(list1,list2)
print(newlist)"""

#using list.class
"""my_list = [1, 2, 3]
print(my_list.__class__)  # Output: <class 'list'>"""
#not understood

#list.append
list= [1,4,6,3,4]
list.append(5)
print(list)

#list.clear
"""list.clear()
print(list)"""

#list.copy

x=list.copy()
print(x)

#list.count
y = list.count(4)
print(y)

#list.extend(doubt -- why newlist gets the output as none)
"""list1 = [1,4,5]
list2=[4,7,8]
newlist=list1.extend(list2)
print(newlist)
print(list1)"""


#list.index(doubt why 4 index as 1 and not 4 )
x= list.index(6)
print(x)

#list.insert
list.insert(4,8)
print(list)

#list.pop
list.pop(4)
print(list)
 #list.remove(doubt -- why not remove the second 4 also )
list.remove(4)
print(list)
#list.remove 
list.reverse()
print(list)
#list.sort()to sort the list 
