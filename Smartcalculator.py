history = []

while True:

    print("\n=== Calculator With History ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. View History")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Exit
    if choice == "6":
        print("Exiting Calculator...")
        break

    # View History
    elif choice == "5":

        print("\n=== Calculation History ===")

        if len(history) == 0:
            print("No calculations yet.")
        else:
            for item in history:
                print(item)

    # Math Operations
    elif choice in ["1", "2", "3", "4"]:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Addition
        if choice == "1":
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"

        # Subtraction
        elif choice == "2":
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"

        # Multiplication
        elif choice == "3":
            result = num1 * num2
            operation = f"{num1} × {num2} = {result}"

        # Division
        elif choice == "4":

            if num2 == 0:
                print("Cannot divide by zero!")
                continue

            result = num1 / num2
            operation = f"{num1} ÷ {num2} = {result}"

        print("Result:", result)

        history.append(operation)

    else:
        print("Invalid Choice!")