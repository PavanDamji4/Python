# This is 65th code of this python course
# This coures demonstrates the use of walrus operaotr

# Traditional Mehtod
a = int(input("Enter a Number : "))

if a>50:
    print("A is greater than 50")
else:
    print("A is smaller than 50")

# now using Walrus Operator

if b:=int(input("Enter a number : "))>50:
    print("A is greater than 50")
else:
    print("A is smaller than 50")

# Another Example
l=[1,2,3,4,5]
while (n:=len(l))>0:
    print(l.pop())