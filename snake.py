# inherit reptile from Reptile class


from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True


    def use_tongue_to_smell(self):
        return "i can use my tongue to smell food"

snake_object = Snake()

print(snake_object.eat()) # this function is inherited from Animal
print(snake_object.seek_heat()) # function is inherited from reptile
print(snake_object.use_tongue_to_smell()) # function from here

# create 2 more functions one with _ and the other with __
#execute them both - return message should explain encapsulation break down - public protected private