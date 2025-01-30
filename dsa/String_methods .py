#Slicing 
b ="hello world "
print(b[:5])# print everything form first to 5th char 
print(b[2:5])# print everything from the second char to 5th

# 1. Basic String Functions
text = "Hello World"
print(len(text))  # Output: 11

# 2. String Case Manipulation
print(text.upper())       # Output: "HELLO WORLD" makes the entire string capital 
print(text.lower())       # Output: "hello world" makes the entire string lower 
print(text.title())       # Output: "Hello World" make the first letter of each word in string capital 
print(text.capitalize())  # Output: "Hello world" make the first leter of the first word capital 
print(text.swapcase())    # Output: "hELLO wORLD" changes uppercase to lower and viceversa 

# 3. Searching & Checking
print(text.find("World"))   # Output: 6
print(text.startswith("Hello"))  # Output: True
print(text.endswith("World"))    # Output: True
print(text.count("o"))  # Output: 2 how many times strong hvae been repeated 

# 4. String Modification
print(text.replace("World", "Python"))  # Output: "Hello Python"

# Whitespace Removal
text_with_spaces = "   Hello World   "
print(text_with_spaces.strip())   # Output: "Hello World"
print(text_with_spaces.lstrip())  # Output: "Hello World   " left strip 
print(text_with_spaces.rstrip())  # Output: "   Hello World" right strip

# 5. Splitting & Joining
fruits = "apple,banana,grape"
fruit_list = fruits.split(",")  
print(fruit_list)  # Output: ['apple', 'banana', 'grape']

joined_string = " - ".join(fruit_list)
print(joined_string)  # Output: "apple - banana - grape"

# 6. String Formatting
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))  # Using format()
print(f"My name is {name} and I am {age} years old.")  # Using f-strings

