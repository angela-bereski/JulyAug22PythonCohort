import random
from classes.player import *
from classes.pet import *
from .trick import *

class PetsGame:
    def __init__(self):
        self.leave = 0


    def start(self):
        message = print("Lets get started\n\n")
        petInput = str(input('Please give your pet character a name\n\n'))
        pet = Pet(petInput)
        game = True
        while game:
            if pet.hunger == 100:
                self.leave = 1
                if self.leave == 1:
                    game = False
            else:
                message = print("Game still testing")
                game = False