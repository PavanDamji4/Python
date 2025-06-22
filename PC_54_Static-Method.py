# This is 54th code of this python course
# This code demonstrates the use of Static method in the class in Python

class person:
    @staticmethod
    def info(name): #doesn't require any self
        print(f"My name is {name}")

p  = person()
person.info("Swayam")
p.info("Nagesh")