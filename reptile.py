# inherit everything from Animal class into reptiles

from animal import Animal

# create reptile class

class Reptile (Animal): # write name of class in (parent-class) to inherit
    # parent class - base class super class

    def __init__(self):
        #to let it know to inherit everything from parent class
        super().__init__() #super is used to inherit everything from base class (EXAMQ)
        self.cold_blooded = True
        self.heart_chambers = [3,4]

    def seek_heat(self):
        return "looking for sun shine"

    def hunt(self):
        return "catch next meal"

#  create object of reptile class

reptile_object = Reptile()

#print(reptile_object.eat()) # from animal
#print(reptile_object.hunt()) # from reptile -here

