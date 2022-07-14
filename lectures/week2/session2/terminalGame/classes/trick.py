class Trick:
    def __init__(self,name, difficulty):
        self.name = name
        self.difficulty = difficulty


    def leveledUp(self, level):
        original = self.difficulty
        self.difficulty += level
        print(f'Trick leveled up from {original} to {self.difficulty}')
        return self

