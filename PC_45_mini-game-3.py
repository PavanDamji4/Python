# This is 45th code of this python course
# this code is a game of Rock paper and scissor...it also demonstrates the use of random

import random

from numpy.f2py.crackfortran import usepattern

print("*********** Welcome to the Game ***********")
print("Choose by numbers ( eg., 1,2 )")
print("1. Rock\n2. Paper\n3. Scissor\n4. Exit")

userpoints = 0
computerpoints = 0
b=True
while(b):
    uc = int(input("Your Choice : "))
    cc = random.choice([1,3])
    print(f"Computer choice : {cc}")



    if uc == 1 and cc == 3 or uc == 2 and cc == 3 or uc == 3 and cc == 1:
        print("_______________________________________________________________")
        print("Computer Won!")
        print("_______________________________________________________________")
        computerpoints+=1
    elif uc>4:
        print("_______________________________________________________________")
        print("Invalid number")
    elif uc == 1 and cc == 1 or uc == 2 and cc == 2 or uc == 3 and cc == 3:
        print("_______________________________________________________________")
        print("Its a draw!")
        print("_______________________________________________________________")

    elif uc==4:
        print("_______________________________________________________________")
        print("Exiting")
        print("_______________________________________________________________")
        print(f"Points : \nComputer = {computerpoints}\n You = {userpoints}")
        b = False
    else:
        print("_______________________________________________________________")
        print("You Won!")
        print("_______________________________________________________________")
        userpoints+=1




