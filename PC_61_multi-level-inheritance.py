# This is 62nd code of this python course
# This code demonstrates the use of multi-level inheritance

class parent:

    def show1(self):
        print("This is from parent class! ")

class child(parent):

    def show2(self):
        print("This is from child class! ")

class grandchild(child):

    def show3(self):
        print("This is from grand child class! ")


gc = grandchild()
gc.show1()
gc.show2()
gc.show3()