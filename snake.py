# inherit reptile from Reptile class

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True

    def use_tongue_to_smell(self):
        return "i can use my tongue to smell food"

    def _move(self): # protected encapsulation function example
        try:
            return snake_object._move()
        except RecursionError:
            return "this information is protected"

    def __blinks(self): # private encapsulation function examaple (still possible to access the hidden data)
        try:
            return snake_object.__blinks()
        except AttributeError:
            return "this info is private and hidden "


# watch video to clean up errors with try and except keys (20 mins in)
# "this information is protected or hidden"

snake_object = Snake()

#print(snake_object.eat()) # this function is inherited from Animal
#print(snake_object.seek_heat()) # function is inherited from reptile
#print(snake_object.use_tongue_to_smell()) # function from here and example of public encapsulation

# create 2 more functions one with _ and the other with __
#execute them both - return message should explain encapsulation break down - public protected private
print(snake_object._move()) # protected encapsulation
print(snake_object.__blinks()) #private encapsulation



# what type of errors & exceptions have you seen so far
# syntax error
# indentation error - value error - attribute error


# Try:
    # print("test")
    # return
# except name_of_error:
#    print()
#   return

# finally:
#       print("linked to logic above ")
