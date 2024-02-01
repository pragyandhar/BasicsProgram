import random


class dice:
    def roll_dice(self):
        print(f"The number is: {random.randrange(1, 7)}")


diceroll = dice()
'''Run the code: diceroll.roll_dice() to roll the dice'''
while 1:
    diceroll.roll_dice()
