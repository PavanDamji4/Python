# This is 12th code of this Python Course
# It demonstrates the use of for-loop

# Printing numbers from 1 to 20
a = 1
for a in range(1, 21):
    print(a)

# Looping through each character in a string
name = "Pavan"
for x in name:
    print(x)

# Looping through a list with mixed data
list = [1, 2, 3, 4, "one", "two", "three"]
for x in list:
    print(x)

# Printing only even numbers from the list
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in L:
    if x % 2 == 0:
        print(x)

# Using range with step: from 1 to 20 with step of 5
for n in range(1, 20, 5):
    print(n)
