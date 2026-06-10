taken_usernames = ["admin", "harsh", "python", "developer"]

print("=== Username Availability Checker ===")

username = input("Enter a username: ").lower()

# Length Check
if len(username) < 4:
    print("Username must be at least 4 characters long.")

# Space Check
elif " " in username:
    print("Username should not contain spaces.")

# Special Character Check
elif not username.isalnum():
    print("Username should contain only letters and numbers.")

# Availability Check
elif username in taken_usernames:
    print("Username already taken ❌")

else:
    print("Username available ✅")