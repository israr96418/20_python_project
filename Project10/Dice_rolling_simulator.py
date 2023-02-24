import random
from dice_drawing import dice_drawings

def dice_rolling():
    dice_drawing = dice_drawings
    rolling = input("Roll the dice (Yes/No)?: ")

    while rolling.lower() == 'yes' or rolling.lower() == 'y' or rolling.lower() == 'Y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        rolling = input("Do you want to roll again (Yes/No): ")


if __name__ == '__main__':
    dice_rolling()
