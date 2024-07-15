import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def roll_dice(number_of_rolls, sides):
    dice = Dice(sides)
    return [dice.roll() for _ in range(number_of_rolls)]

def calculate_score(rolls):
    return sum(rolls)

def main():
    sides = 6  

    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")

    number_of_rolls = int(input("Enter the number of rolls each player will make: "))

    player1_rolls = roll_dice(number_of_rolls, sides)
    player1_score = calculate_score(player1_rolls)
    print(f"{player1_name} rolls: {player1_rolls} (Total Score: {player1_score})")

    player2_rolls = roll_dice(number_of_rolls, sides)
    player2_score = calculate_score(player2_rolls)
    print(f"{player2_name} rolls: {player2_rolls} (Total Score: {player2_score})")

    if player1_score > player2_score:
        print(f"{player1_name} wins!")
    elif player2_score > player1_score:
        print(f"{player2_name} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()