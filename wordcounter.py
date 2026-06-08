print("=== Word Counter ===")

text = input("\nEnter your text:\n")

# Word Count
words = len(text.split())

# Character Count
characters = len(text)

# Sentence Count
sentences = text.count(".") + text.count("!") + text.count("?")

print("\n=== Results ===")
print(f"Words: {words}")
print(f"Characters: {characters}")
print(f"Sentences: {sentences}")