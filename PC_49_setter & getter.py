# This is 49th code of this python course
# this code demonstrates the use of setter and getter methods in python

class person:

    def __init__(self,name ):
        self._n = name

    @property
    def show(self) :
        print("Name : ",self._n)

    @show.setter
    def n(self,value):
        self._n=value

p = person("Pavan")
p.show
p.n = "Rohan"
p.show
