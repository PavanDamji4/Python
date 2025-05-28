# This is 16th code of this Python Course
# This demonstrates the use of user-defined functions

def greater(a, b):  # Function to find the greater number
    if a > b:
        print(a, "is greater!")
    else:
        print(b, "is greater!")

def table(a):  # Function to print multiplication table
    i = 1
    while i <= 10:
        print(a, "*", i, "=", a * i)
        i += 1

x = 34
y = 23
greater(x, y)
greater(2, 4)

z = 2
table(2)
