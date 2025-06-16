# This is 48th code of this python course
# This code demonstrates the use of decorator in Pyhon


# use 1 : without arguments
def deco(fx):
    def mfx():
        print("The start to the function!")
        fx()
        print("The end of the function")
    return mfx

@deco
def say_hello():
    print("Hello Everyone")

say_hello()

# use 2 : with arguments

def wrap(func):
    def mfx(*args, **kwargs):
        print("Adding :")
        func(*args, **kwargs)
        print("Adding done ")
    return mfx

@wrap
def addition(x,y):
    print("Sum : ",x+y)

addition(4,4)

