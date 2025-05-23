# This is the 6th code of this Python Course
# It demonstrates use of String

a = "Hi, Nice to meet you"
name = 'Rohan'

print(a, name)  # Prints both strings together with a space in between

b = """This is the three line String
line 1
line 2
line 3
You can also use "double Coat" in this"""
print(b)  # Multiline string using triple quotes

print(a[0])         # Accessing first character of string 'a'
print(name[0], name[1])  # Accessing individual characters of 'name'

print(name[0:3])    # Slicing from index 0 to 2 (3 is excluded)

print(name[-2:5])   # Slicing using negative index, -2 means 2nd last character

print(len(b))       # Returns length of the string 'b'
