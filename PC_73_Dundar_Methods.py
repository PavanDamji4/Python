# This is 58th code of this python course
# This code demonstrates the us of Some magical or Dundar methods

class person:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        print("This is __str__ method and name is ",self.name)

    def __repr__(self):
       return f"This is __repr__ method and name is {self.name}"

p = person("Mahesh")
print(p.name)
print(str(p))
print(repr(p))