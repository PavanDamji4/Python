# This is 50th code of this python course
# This code demonstrates the use of Inheritance in python

class parent:
    def show1(self):
        print("I am from parent class !")
class child(parent):
    def show2(self):
        print("I am from child class!")
c = child()
c.show1()
c.show2()
