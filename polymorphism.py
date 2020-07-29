class Animal():
    def __init__(self, name):
        self.name = name
        print(self.name)
    
    def speak(self):
        print("My name is {}".format(self.name))

#instantiat the objects
mydog = Animal("Dog")
mycat = Animal("Cat")

#Call the same function
mydog.speak()
mycat.speak()

# Or you can loop and call the same function
for pet in [mydog, mycat]:
    pet.speak()


class Bird():
    def __init__(self, name):
        self.name = name
        print(self.name)

    def speak(self):
        raise NotImplementedError("The subclass has to implement the method")


class Sparrow(Bird):
    def __init__(self, name):
        Bird.__init__(self, name)

    def speak(self):
        print("tweet tweet says {}".format(self.name))

class Duck(Bird):
    def speak(self):
        print("tweet tweet says {}".format(self.name))

my_bird = Bird("Birdy")
#my_bird.speak()

my_sparrow = Sparrow("Jack Sparrow")
my_duck = Duck("Donald Duck")

my_sparrow.speak()
my_duck.speak()
    