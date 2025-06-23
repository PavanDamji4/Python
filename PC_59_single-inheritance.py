# This is 60th code of this python course
# This course demonstrates the use of single inheritance

class parent:

    def show1(self):
        print("This is from parent class! ")

class child(parent):

    def show2(self):
        print("This is from child class! ")

c = child()
c.show1()
c.show2()