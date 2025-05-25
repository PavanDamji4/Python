# This is 9th code of the Python Course
# It demonstrates the use of if-else and nested if-else

a = int(input("Enter a number : "))
if a > 0:
    print("POSITIVE")        # If number is greater than 0
else:
    print("NEGATIVE")        # If number is 0 or less


b = int(input("Enter number : "))
if b > 0:
    print("POSITIVE")
elif b < 0:
    print("NEGATIVE")
else:
    print("Zero")            # Executes when number is exactly 0


c = int(input("Enter number : "))
if c > 0:
    if c < 50:
        print("Number is positive and between 1 to 50")
    else:
        print("Number is positive and greater than 50")
elif c < 0:
    print("Number is negative")
else:
    print("Number is Zero")
