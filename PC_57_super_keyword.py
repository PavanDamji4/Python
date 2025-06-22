# This is 57th code of this python course
# This code demonstrates the use of super keyword in python

# super keyword for method calling
class parent:
    def show(self):
        print("This is method show() from parent class")

class child(parent):
    def show2(self):
        super().show()
        print("This is method show2() from child class")

c= child()
c.show2()

# super keyword for constructor calling

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Name : ",self.name)
        print("Age : ",self.age)

class personwork(person):
    def __init__(self,name,age,work):
        super().__init__(name, age)
        self.work = work
        print(f"Work : {self.work}")

p = personwork("Rohan",34,"Labour")
