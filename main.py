expenses = {}

def add_expense():
    currdate=input("Please enter the date of the expense in DD-MM-YYYY format:")
    type=str(input("Please enter the Category(Food,Travel,Shopping,Entertainment,Health,Others):"))
    index=type.lower().replace(" ","")
    if index=="food":
        add_food_expense(currdate)
    if index=="travel":
        add_travel_expense(currdate)
    if index=="shopping":
        add_shopping_expense(currdate)
    if index=="entertainment":
        add_entertainment_expense(currdate)
    if index=="health":
        add_health_expense(currdate)
    if index=="others":
        add_others_expense(currdate)
    

def add_food_expense(currdate):
    expense=float(input("Please enter the amount of money spent: "))
    if currdate not in expenses:
        expenses[currdate]={}
    if "food" not in expenses[currdate]:
        expenses[currdate]["food"] = []
    expenses[currdate]["food"].append(expense)
        
   

def add_travel_expense(currdate):
    expense=float(input("Please enter the amount of money spent: "))
    if currdate not in expenses:
        expenses[currdate]={}
    if "travel" not in expenses[currdate]:
        expenses[currdate]["travel"] = []
    expenses[currdate]["travel"].append(expense)


def add_shopping_expense(currdate):
    expense=float(input("Please enter the amount of money spent: "))
    if currdate not in expenses:
        expenses[currdate]={}
    if "shopping" not in expenses[currdate]:
        expenses[currdate]["shopping"] = []
    expenses[currdate]["shopping"].append(expense)


def add_entertainment_expense(currdate):
    expense=float(input("Please enter the amount of money spent: "))
    if currdate not in expenses:
        expenses[currdate]={}
    if "entertainment" not in expenses[currdate]:
        expenses[currdate]["entertainment"] = []
    expenses[currdate]["entertainment"].append(expense) 
    
def add_health_expense(currdate):
    expense=float(input("Please enter the amount of money spent: "))
    if currdate not in expenses:
        expenses[currdate]={}
    if "health" not in expenses[currdate]:
        expenses[currdate]["health"] = []
    expenses[currdate]["health"].append(expense)


def add_others_expense(currdate):
    expense=float(input("Please enter the amount of money spent: "))
    if currdate not in expenses:
        expenses[currdate]={}
    if "others" not in expenses[currdate]:
        expenses[currdate]["others"] = []
    expenses[currdate]["others"].append(expense)


def view_expense():
    d1=input("Enter the date in DD-MM-YYYY format: ")
    if d1 not in expenses:
        print("\nNo expenses for this day ")
    else:
        print(f"\nExpenses for {d1}: ")
        for category,amounts in expenses[d1].items():
            print(f"{category} : {amounts}")
        print()

def delete_expense():
    d1=input("Enter the date in DD-MM-YYYY format: ")
    if d1 not in expenses:
        print("\nNo expenses for this day ")
    category = input("Enter category to delete from: ").strip().lower()
    if category not in expenses[d1]:
        print("Category not found.\n")
        return
    print("Current expenses:", expenses[d1][category])
    amount = float(input("Enter amount to delete: "))
    if amount in expenses[d1][category]:
        expenses[d1][category].remove(amount)
        print("Expense removed.\n")
    else:
        print("Amount not found.\n")
    
def total_spending():
    d1=input("Enter the date in DD-MM-YYYY format: ")
    if d1 not in expenses:
        print("\nNo expenses for this day ")
    if d1 not in expenses:
        print("No expenses for today.\n")
        return

    total = 0
    for amounts in expenses[d1].values():
        total += sum(amounts)

    print(f"Total spending for {d1}: {total}\n")

def daily_report():
    view_expense()
    total_spending()

def weekly_report():
    print("\nWeekly Report:")
    total = 0

    for day in expenses:
        for amounts in expenses[day].values():
            total += sum(amounts)

    print(f"Total spending (all days): {total}\n")

def menu():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Spending")
        print("5. Daily Report")
        print("6. Weekly Report")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            total_spending()
        elif choice == "5":
            daily_report()
        elif choice == "6":
            weekly_report()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice.\n")

menu()