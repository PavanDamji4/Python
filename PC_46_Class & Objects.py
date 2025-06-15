#  This code is the 46th code and start of the Object Oriented Programming (OOP)

class person:
    name = "Pavan"
    Salary = "-1000"
    def output(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.Salary}")



p = person()
print(p.name)
print(p.Salary)
print("")

p.output()

print("")

p2= person()
p2.name = "Rohan"
p2.Salary = 2000
p2.output()