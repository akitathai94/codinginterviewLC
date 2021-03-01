from random import randint
class Dice:
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_dice(self):
        total = 0
        for i in range(10):
            roll = randint(1, self.sides)
            total += roll
            print(f"Roll {i+1}th: ",roll)
        print(f"Total: {total}")
six_sides_dices = Dice(6)
six_sides_dices.roll_dice()

ten_sides_dices = Dice(10)
ten_sides_dices.roll_dice()

twenty_sides_dices = Dice(20)
twenty_sides_dices.roll_dice()