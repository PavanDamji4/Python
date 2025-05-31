# This is 24th code of this Python course
# This code demonstrates the use doc-Strings in Pyhon

def sum(a,b):
    '''This function gets 2 numbers and adds them and prints the sum of the number '''
    c=a+b
    print("Sum = ",c)

sum(10,20)
print(sum.__doc__)