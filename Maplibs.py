print("=== Mad Libs Story Generator ===\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
food = input("Enter a food item: ")
verb = input("Enter an action word: ")

print("\n=== Your Funny Story ===\n")

story = f"""
One day {name} went to {place}.
Suddenly, a giant {animal} appeared!

{name} got scared and started to {verb}.
After some time, the {animal} became friendly
and offered {food} to {name}.

It became the funniest day ever! 😂
"""

print(story)