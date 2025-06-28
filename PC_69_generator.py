# This is 69th code of this python course
# This code demonstrates the use of generator

def count(nums):
    for n in nums:
        yield n

c = count([1,2,4,5,6,7,8,9,0])
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


print("Printing Cube")
# using generator to print square of numbers
def square(nums):
    for n in nums:
        yield n*n

s = square([1,2,3,4,5,6,7,8,9,0])
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
