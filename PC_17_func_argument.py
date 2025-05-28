# This is 17th code of this Python Course
# This code demonstrates the use of arguments in functions

# 1. Positional arguments
def display1(a, b, c):
    print("a =", a)
    print("b =", b)
    print("c =", c)

display1(1, 2, 3)  # Passing values directly in order

print("************************************************************")

# 2. Arbitrary positional arguments using *args
def display2(*numbers):
    print(type(numbers))  # Will print <class 'tuple'>
    for i in numbers:
        print(i)

display2(1, 2, 3, 4, 5, 6, 7)  # Can pass any number of values

print("*************************************************************")

# 3. Keyword arguments (order doesn't matter if keywords are specified)
def display3(fname, midname, lname):
    print("Hello,", fname, midname, lname)

display3(midname="Vishnu", fname="Pavan", lname="Damji")

print("*************************************************************")

# 4. Arbitrary keyword arguments using **kwargs
def display4(**names):
    print(type(names))  # Will print <class 'dict'>
    print("Hello,", names["fname"], names["midname"], names["lname"])

display4(midname="Vishnu", fname="Pavan", lname="Damji")

print("*************************************************************")

# 5. *args with a loop to calculate the sum of all passed values
def display5(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    return(sum)

a = 2
b = 3
c = 4

cal = display5(1, 2, 3, 4)  # Sum of 1+2+3+4 = 10
print(cal)
