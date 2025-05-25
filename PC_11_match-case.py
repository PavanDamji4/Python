# This is 11th code of this Python course
# It demonstrates the use of match-case (similar to switch-case)

x = int(input("Enter a number : "))

match(x):
    case 1:
        print("This is one")
    case 2:
        print("This is two")
    case 3:
        print("This is three")
    case 4:
        print("This is four")
    case 5:
        print("This is five")
    case _:  # default case when none of the above match
        print("This number is greater than 5 and below 0")

y = int(input("Enter another number : "))

match(y):
    case 1:
        print("This is one")
    case 2:
        print("This is two")
    case 3:
        print("This is three")
    case 4:
        print("This is four")
    case 5:
        print("This is five")
    case _ if (y > 5):  # condition inside default case
        print("This number is greater than 5")
    case _ if (y < 0):  # another condition in default case
        print("This number is less than 0")
