# create animal class
# syntax class Name:

class Animal:

    # --init-- to declare class attributes
    def __init__(self): #self refers to current class
        self.alive = True
        self.spine = True


    def sleep (self): #method called sleep for self class
        return "8 hours sleep is advised.."

    def eat (self):
        return "eat if you like to stay alive"

    # create an object of the class before using it


cat = Animal()

#print(cat.eat()) # absatracted how was eat created or what info is available