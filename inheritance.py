class Bird():
    wings = 2
    legs = 2
    eyes = 2
    beak = 1

    def __init__(self, can_fly, can_jump):
        self.can_fly = can_fly
        self.can_jump = can_jump
        print("The bird can fly {}, and also can jump {}".format(can_fly, can_jump))

    def who_am_i(self, name):
        print("I am a bird, my name is {}".format(name))

#mybird = Bird(True, False)
#mybird.who_am_i("peacock")

class Sparrow(Bird):
    def __init__(self, can_fly, can_jump):
        Bird.__init__(self, can_fly, can_jump)
    
    def who_am_i(self, name):
        print("I am a bird and I am free")

mySparrow = Sparrow(True, False)
mySparrow.who_am_i("Lola")
