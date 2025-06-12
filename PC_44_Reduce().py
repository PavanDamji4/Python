# This is 44th code of this python course
# This code demonstrates the use of Reduce Function
from functools import reduce

def add(x,y):
    return x+y


l=[1,2,3,4,5,6,7,8,9,10]
l2 = reduce(add,l)

print(f"Addition : {l2}")

l3= reduce(lambda x,y:x-y,l)
print(f"Substration : {l3}")