# This is 61st code of this python course
# This code demonstrates the use of multiple inheritance

class parent:

    def show1(self):
        print("This is from parent class! ")

class child1(parent):

    def show2(self):
        print("This is from child1 class! ")

class child2(parent):

    def show3(self):
        print("This is from child2 class! ")

c1 = child1()
c2 = child2()

c1.show1()
c1.show2()
c2.show1()
c2.show3()