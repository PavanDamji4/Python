# This ic 63rd code of this pyhon course
# this code demonstrates the use of hybrid inheritance (basic example)

class parent:
    def show1(self):
        print("Parent 1")


class child1(parent):
    def show2(self ):
        print("Child 1")

class child2(parent):
    def show3(self):
        print("Child 2")

class Grandchild(child1,child2):
    def show4(self):
        print("GrandChild ")

o = Grandchild()
o.show1()
o.show2()
o.show3()
o.show4()