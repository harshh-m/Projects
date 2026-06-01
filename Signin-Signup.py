users = {}

while True:

    print("\n=== Login & Signup System ===")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Signup
    if choice == "1":

        username = input("Create username: ")
        password = input("Create password: ")

        if username in users:
            print("Username already exists!")
        else:
            users[username] = password
            print("Signup Successful!")

    # Login
    elif choice == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print(f"Welcome, {username}! 🎉")
        else:
            print("Invalid Username or Password!")

    # Exit
    elif choice == "3":
        print("Exiting System...")
        break

    else:
        print("Invalid Choice!")