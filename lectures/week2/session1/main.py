from concurrent.futures import BrokenExecutor
from data import trainingSchool
print("print from data file", trainingSchool[0]['petsInClass'][0]['owner'])
print("a pet form data file", trainingSchool[0]['petsInClass'][0])

class Owner: # the name of the class
    def __init__(self, firstName, lastName): # constructor = required attributes for all instances of this class
        self.firstName = firstName
        self.lastName = lastName
        self.pets = [] # each owner has the ability to own muplitple pets

# This is a method that we can do with the owner above is how we create owners
    def printOwner(self):
        print(f"{self.firstName} {self.lastName}")

    def printPetsOwned(self):
        thePets = [] # and empty list to contain certian information
        for p in self.pets: # looping through all the pets listed in self.pets list
            thePets.append(p.name) # just adding the pets first name to  this new list of thePets
        print(f"{self.firstName} owns the following pet or pets {thePets}")

    def addPets(self, pet):
        self.pets.append(pet) # add to the chosen owner the (pet) we chose to self.pets (our list of pets)
        return self

class Pet:
    def __init__(self, breed, name, age, species):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.food = None # each pet has the ability to eat some sort of food

    def printPet(self):
        print(f"{self.name}")




#  Creating owners
melissa = Owner("Melissa", "Longenberger")
print("print from class", melissa)
melissa.printOwner()


#  Creating Pets
bear = Pet("Mixed", "Bear", 7, "Dog")
copper = Pet("Beagle", "Copper", 1, "Dog")
bear.printPet()

# print pets owned
melissa.printPetsOwned() # shouwl be an empty list as I haven't added pets to the owner yet

# Add pets to owners
melissa.addPets(bear) # just adds pets to the owner
melissa.printPetsOwned() # prints the list of owned pets again but after we added one

# Chaining methods
melissa.addPets(copper).printPetsOwned()