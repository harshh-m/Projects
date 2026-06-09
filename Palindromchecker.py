print("=== Palindrome Checker ===")

word = input("Enter a word: ").lower()

# Reverse Word
reversed_word = word[::-1]

# Check
if word == reversed_word:
    print(f"\n'{word}' is a Palindrome ✅")
else:
    print(f"\n'{word}' is NOT a Palindrome ❌")