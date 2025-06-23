# This is 60th code of this python course
# This code demonstrates the use of method overridng in python

class parent:
    def show(self):
        print("Hey, I am from parent class")

class child(parent):
    def show(self):
        super().show()
        print("Hey, I am from child class")

c = child()
c.show()

