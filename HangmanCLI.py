import random

words = ["python", "computer", "coding", "developer", "github"]

word = random.choice(words)

guessed_letters = []
attempts = 6

print("=== Hangman Game ===")

while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win Check
    if "_" not in display_word:
        print("\nYou Won! 🎉")
        break

    guess = input("Guess a letter: ").lower()

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Wrong Guess
    if guess not in word:
        attempts -= 1
        print(f"Wrong Guess! Attempts Left: {attempts}")

# Lose Condition
if attempts == 0:
    print(f"\nYou Lost! The word was '{word}' 😢")