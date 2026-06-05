print("=== Number System Converter ===")

while True:

    print("\n1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Exit
    if choice == "4":
        print("Exiting Converter...")
        break

    number = int(input("Enter a decimal number: "))

    # Binary
    if choice == "1":
        print(f"Binary: {bin(number)[2:]}")

    # Octal
    elif choice == "2":
        print(f"Octal: {oct(number)[2:]}")

    # Hexadecimal
    elif choice == "3":
        print(f"Hexadecimal: {hex(number)[2:].upper()}")

    else:
        print("Invalid Choice!")