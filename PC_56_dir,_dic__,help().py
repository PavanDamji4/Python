# This is 58th code of this python course
# This code demonstrates the use of dir, __dic__ and help() methods used in pythons

l = [1,2,3,4,5,6,7,8,9,10]
print(l.__dir__())
print(l.reverse())
print(l)

class info:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.work="Employee"

i = info("Pavan",23)
print(i.__dict__)

print(help(i))

