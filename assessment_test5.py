import math
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
class Line: 
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        x1 = self.coor1[0]
        y1 = self.coor1[1]
        x2 = self.coor2[0]
        y2 = self.coor2[1]

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return distance
    
    def slope(self):
        pass

coordinate1 = (3,2)
coordinate2 = (8,10)
l = Line(coordinate1,coordinate2)
print(l.distance())

# Fill in the class
class Cylinder:
    pi = 3.1457
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        v = (4/3)*Cylinder.pi*self.radius*self.radius*self.height
        return v
    
c = Cylinder(2,3)
print(c.volume())


## For this challenge, create a bank account class that has two attributes:
# owner
# balance
# two methods:
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class BankAccount:
    balance = 0.0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Your balance amoutn is {}".format(self.balance))
        return self.balance

    def withdraw(self, amount):
        if(self.balance - amount <=0):
            print("You have insufficient amount in your account balance")
        else:
            self.balance = self.balance - amount
            print("Your balance amoutn is {}".format(self.balance))
        return self.balance

    
b = BankAccount("om",100.00)
b.deposit(50)
b.withdraw(100)
b.withdraw(75)

