accounts = {}

while True:

    print("\n=== Mini Banking System ===")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Create Account
    if choice == "1":

        username = input("Enter username: ")

        if username in accounts:
            print("Account already exists!")
        else:
            password = input("Create password: ")

            accounts[username] = {
                "password": password,
                "balance": 0
            }

            print("Account Created Successfully!")

    # Login
    elif choice == "2":

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in accounts and accounts[username]["password"] == password:

            print(f"\nWelcome {username}!")

            while True:

                print("\n1. Check Balance")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Logout")

                option = input("Enter your choice: ")

                # Check Balance
                if option == "1":
                    print(f"Balance: ₹{accounts[username]['balance']}")

                # Deposit
                elif option == "2":

                    amount = float(input("Enter amount to deposit: "))

                    accounts[username]["balance"] += amount

                    print("Money Deposited Successfully!")

                # Withdraw
                elif option == "3":

                    amount = float(input("Enter amount to withdraw: "))

                    if amount <= accounts[username]["balance"]:

                        accounts[username]["balance"] -= amount

                        print("Money Withdrawn Successfully!")

                    else:
                        print("Insufficient Balance!")

                # Logout
                elif option == "4":
                    print("Logged Out Successfully!")
                    break

                else:
                    print("Invalid Choice!")

        else:
            print("Invalid Username or Password!")

    # Exit
    elif choice == "3":
        print("Exiting Banking System...")
        break

    else:
        print("Invalid Choice!")