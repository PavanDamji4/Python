# This is 18th code of this python course
# This code demonstrates the use of List

# Creating a list with numbers and a string
l = [1,2,3,4,5,6,7,8,9,10,"Pavan"]
print(type(l))
print(l)  # Print the entire list

# Accessing elements using indexing
print(l[0])   # First element
print(l[3])   # Fourth element
print(l[5])   # Sixth element

# List slicing
print(l[1:5])     # Elements from index 1 to 4
print(l[5:11])    # Elements from index 5 to 10

print(l[:])       # Full list copy using slicing

# Negative indexing in slicing
print(l[-10:-1])  # Elements from second to second-last
print(l[-5:])     # Last 5 elements

# List comprehension: generate a list from 10 to 20
print([i for i in range(10, 21)])

# List comprehension: multiplying each element by 2
print([i*2 for i in range(1, 11)])

# List comprehension with condition: even numbers from 1 to 9
print([i for i in range(1, 10) if(i%2==0)])

# Membership operators in list
print(1 in l)           # True: 1 is in the list
print("pavan" in l)     # False: lowercase 'pavan' not in list
print("Pav" in l)       # False: partial match doesn't count
print("Pavan" in l)     # True: exact string match

# Membership operators in string
str = "Hello"
print("H" in str)       # True
print("Hell" in str)    # True
print("ello" in str)    # True

l2 = [1,2,3,4,5,6,7,8,9,10]
print(l2[0:11:2])

l3=l+l2
print(l3) # Merging / Concatinating the multiple tuples
