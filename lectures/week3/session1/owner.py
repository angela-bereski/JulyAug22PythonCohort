class Owner:
    # This constructor function contains the attributes that each instance has or can have
    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.createdAt = None
        self.updatedAt = None
        self.favFood = None
        self.instructor = False

# Methods - These are functions that provide action to our instances.  Things that we can do with or too each instance
    def printOwner(self):
        print(f'{self.firstName} {self.lastName}')

    def printAllInfo(self):
        print(f'{self.firstName} {self.lastName} has an id of {self.id} and a favorite food of {self.favFood}')

    def talks(self, other):
        print(f'{self.firstName} was caught talking to {other.firstName} in class')

    def addFavFood(self, food):
        # self.favFood.append(food)
        self.favFood = food
        return self

    def makeInstructor(self):
        self.instructor = True
        return self

    def printStatus(self):
        if self.instructor == False:
            print(f'{self.firstName} is a Student')
        else:
            print(f'{self.firstName} is an Instructor')

    
data01 = Owner(1, "Arvel", "Cavitt")
# data01.printOwner() 
# data01.printAllInfo()
data01.printStatus()
data02 = Owner(2, "Bernard", "Olaires")
# data02.printOwner()
data02.printStatus()
data03 = Owner(3, "Melissa", "Longenberger")
# data03.printOwner()
# data03.printAllInfo()
# data03.favFood = "Italian"
data03.addFavFood("Italian")
# data03.printAllInfo()
data03.printStatus()
# data03.instructor = True
data03.makeInstructor()
data03.printStatus()

# data01.talks(data02)

class Child(Owner): # Creating a chile that has all the same attributes that the owner does plus any extras that we want
    def __init__(self, id, firstName, lastName, age): # this determines what is required for each child to be created and will include the values from the owner class we also require
        super().__init__(id, firstName, lastName) # telling us what those values from the owner class are
        self.age = age # this is only required of a child instance not the owner because it is rude to ask an adult their age
    

data04 = Child(4, "Aiden", "O'Neil", 15)

data04.printAllInfo()
data04.addFavFood("Pizza").printAllInfo()
data04.printStatus()