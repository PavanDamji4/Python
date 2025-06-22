# This is 55th code of this python course
# This code demonstrates the use of ClassMethods


class person:
    name = "Anurag"
    def show(self):
        print(self.name)

    @classmethod       # to check the behaviour of @classmethod comment this and run
    def change(cls,n):
        cls.name= n

p=person()
p.show()
p.change("Ramesh")
p.show()
print(person.name)

