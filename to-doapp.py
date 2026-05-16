task=[]

while True:
    print("1: Add  task")
    print("2:View tasks")
    print("3:Delete task")
    print("4:Exit")
    choice=int(input("Enter your chioce:"))
    if choice == 1:
        task.append(input("Enter the task:"))
        print("Task added successfully.")
    elif choice == 2:
        print("Tasks:")
        for t in task:
            print(t)
    elif choice == 3:
        task.remove(input("Enter the task to delete:"))
    elif choice ==4:
        break
    else:
        print("Invalid choice please try again.")