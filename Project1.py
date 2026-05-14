expense=[] #list of expense in form of dictionary
print("  Welcome To Expense Tracker   ")

while True:
    print("===Menu===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter Your Choice(1-4):")
       # Add Expense
    if(choice == "1"):
        date = int(input("Enter Date: "))
        category = input("Enter Category (e.g., Food, Transport): ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))  

        exp={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }                  

        expense.append(exp)
        print("\n Expense Added Successfully!") 

         #View Expenses
    elif(choice == "2"):
        if(len(expense)==0):
            print("\n No Expenses Recorded Yet.")
        else:
            print("===This is Your expense======")

            count=1

            for exp in expense:
                print(f"count:->  {exp['date']},{exp['category']},{exp['description']},{exp['amount']} ")
                count+=1
          #Total Expense Calculation
    elif(choice == "3"):
        total=0
        for exp in expense:
            total=total + exp["amount"]

        print("\nTotal Expense:$",total )
           # Exit
    elif(choice == "4"):
        print("Thanks for using Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid Choice ! Please SElect a valid option(1-4)")




