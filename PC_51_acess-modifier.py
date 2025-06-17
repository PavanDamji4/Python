# This is 51st code of this python course
# this code demonstrates the use of access modifiers in oop ( i.e., private, protected , public)

class names:
    def __init__(self):
        self.name1 = "Public"
        self._name2 = "Protected"
        self.__name3 = "Private"

n = names()
print(n.name1)
print(n._name2) # can be accessed but should'nt
#print(n.__name) # cannot be accessed
print(n._names__name3) # accessing private using mangling techniq