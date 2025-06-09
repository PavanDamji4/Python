# This is 38th code of this python course
# This code demonstrates the scope of variable in python
from pickle import GLOBAL


# def func():
#     y=23 #local variable
#     print(y)
#     print(x)
#
# x=34 # global variable
# func()
# print(y)

def func():
    global y
    y=23 #local variable
    print(y)
    print(x)

x=34 # global variable
func()
print(y)