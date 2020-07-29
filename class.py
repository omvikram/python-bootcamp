class Sample():

    sample_type = "area"

    def __init__(self, param1, param2):
        self.length = param1
        self.breadth = param2

    def sample_area(self):
        print("This is the area of {} and {}".format(self.length,self.breadth))
        return self.length*self.breadth


my_sample = Sample(2,3)
print(my_sample)
print(my_sample.length)
print(my_sample.breadth)
print(my_sample.sample_type)
print(my_sample.sample_area())