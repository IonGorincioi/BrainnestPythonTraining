# Create a class called Dice that has attribute sides
# (the number of sides on the dice). Add a method roll
# that generates a random number between 1 and the number
# of sides on the dice.
import random


class Dice:

    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        side = random.randint(1, self.sides)
        return side


dice_face = Dice()
print(dice_face.roll())
