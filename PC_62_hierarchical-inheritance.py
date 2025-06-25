# This is 62nd code of this python course
# this code demonstrates the use of hierarchical inheritance (basic examples)

class parent1:

    def show1(self):
        print("Parent1 Class")

class parent2:

    def show2(self):
        print("Parent2 Class")

class Child(parent1,parent2):

    def show3(self):
        print("Child Class")


class GrandChild1(Child):

    def show4(self):
        print("Grandchild1 Class")

class GrandChild2(Child):

    def show5(self):
        print("Grandchild2 Class")


gc2 = GrandChild2()
gc2.show1()
gc2.show2()
gc2.show3()
gc2.show5()

gc1 = GrandChild1()
gc1.show1()
gc1.show2()
gc1.show3()
gc1.show4()
