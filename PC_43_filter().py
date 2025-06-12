# This is 43rd code of this python course
# this code demonstrates the use of filter function

l=[2,3,4,23,5,3,35,3,6,199,343]

l2= list(filter(lambda x:x>50,l))

print(l2)

def func(x):
    return x<50

l3 = list(filter(func,l))
print(l3)