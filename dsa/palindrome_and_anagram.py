#to check palindrome

word_to_check =input("input the word to be checked")
list =[x for  x in word_to_check]
ispalindrome = False

print(list)

for i in range (len(word_to_check)):
    if list[i] == list[-(i+1)]:
        ispalindrome=True

if ispalindrome:
    print("string is a palindrome")
else :
    print("not a palindrome")


#using dictionary to check anagrams 

x = input("first word")
y = input("second word")

dict1 = {}
dict2 = {}

for i in x:
    if i in dict1 :
        dict1[i] = dict1[i] +1
    else:
        dict1[i] = 1 

for k in y:
    if k in dict2 :
        dict2[k] = dict2[k] +1
    else:
        dict2[k] = 1 

if dict1 == dict2:
    print("word is an anagram")
else:
    print("word is not an anagram")


