# This is 42nd code of this python course
# This code demonstrates the use of Map function

def square(x):
    return x*x

print(square(4))


l = [1,2,3,4,5,6,7,8,9,10]
l2= list(map(square,l))
print(f"Square = {l2}")
l3 = list(map(lambda x:x*x*x,l))

print(f"Cube = {l3}")

def filter_func(a):
    return a<50

l4=list(filter(filter_func,l3))
print(f"Filtration = {l4}")


