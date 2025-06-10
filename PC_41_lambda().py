# This is 41st code of this python course
# This code demonstrates the use of Lamda() functiona

# def sum(x,y):
#     return x+y
#
# print(sum(3,2))

# we can write the function using lamda

sum=lambda x,y: x+y
print(sum(4,3))


def sumsq(func):
    return func*func

print(sumsq(sum(2,2)))


str = lambda s: s

print(str("This is being printed using lamda function"))
