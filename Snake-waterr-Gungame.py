import random

print("=== Snake Water Gun Game ===")

choices = ["snake", "water", "gun"]

computer = random.choice(choices)

user = input("Enter snake, water, or gun: ").lower()

print(f"\nComputer chose: {computer}")

# Tie
if user == computer:
    print("It's a Tie!")

# Winning Conditions
elif (
    (user == "snake" and computer == "water") or
    (user == "water" and computer == "gun") or
    (user == "gun" and computer == "snake")
):
    print("You Win! 🎉")

# Valid Input but Lost
elif user in choices:
    print("Computer Wins! 🤖")

# Invalid Input
else:
    print("Invalid Input!")