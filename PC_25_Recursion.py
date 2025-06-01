# This is 25th code of this python Course
# This code demonstrates the use of Recursion (i.e function calling itself)


def fact(x):
    if x==1:
        return (1)
    else:
        return x * fact(x-1)

x = int(input("Please Input any number for factorial number: "))
print(fact(x))



n = int(input("Please Input any number for fibonacci number: "))
def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(n))