print("=== Currency Converter ===")

print("\n1. INR to USD")
print("2. INR to EUR")
print("3. INR to GBP")

choice = input("\nEnter your choice: ")

amount = float(input("Enter amount in INR: "))

# Conversion Rates
usd_rate = 0.012
eur_rate = 0.011
gbp_rate = 0.0095

# Conversion Logic
if choice == "1":
    converted = amount * usd_rate
    print(f"₹{amount} = ${round(converted, 2)} USD")

elif choice == "2":
    converted = amount * eur_rate
    print(f"₹{amount} = €{round(converted, 2)} EUR")

elif choice == "3":
    converted = amount * gbp_rate
    print(f"₹{amount} = £{round(converted, 2)} GBP")

else:
    print("Invalid Choice!")