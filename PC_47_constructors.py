# This is 47th code of this python course
# this code demonstrates the use of constructors in Class

class sample:

    def __init__(self):
        print("Hello, I am printing from the sample class")

s = sample()  # Constructor is automatically called when a object of that class is created

class sample2:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Sum : ",a+b)

s2 = sample2(5,5)
