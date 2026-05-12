'''
functions:
add_food_expense()
add_expense()
'''
import json
from datetime import datetime
from pprint import pprint

'''example = [
    {"name":"anirudh","age":19},
    {"name":"cheta","age":20}
]
'''

expenses = {}


def add_expense():
    global currdate
    currdate=input("Please enter the date of the expense in DD-MM-YYYY format:")
    type=str(input("Please enter the Category(Food,Travel,Shopping,Entertainment,Health,Others):"))
    index=type.lower().replace(" ","")

    if currdate not in expenses:
        expenses[currdate]={}
    if index=="food":
        add_food_expense()
    elif index=="travel":
        add_travel_expense()
    elif index=="shopping":
        add_shopping_expense()
    elif index=="entertainment":
        add_entertainment_expense()
    elif index=="health":
        add_health_expense()
    elif index=="others":
        add_others_expense()
    
    with open("expenses.json","w") as f:
        json.dump(expenses,f)

def add_food_expense():
    expense=float(input("Please enter the amount of money spent: "))
    if "food" not in expenses[currdate]:
        expenses[currdate]["food"]=0
    expenses[currdate]["food"] += expense


def add_travel_expense():
    expense=float(input("Please enter the amount of money spent: "))
    if "travel" not in expenses[currdate]:
        expenses[currdate]["travel"]=0
    expenses[currdate]["travel"] += expense
    

def add_shopping_expense():
    expense=float(input("Please enter the amount of money spent: "))
    if "shopping" not in expenses[currdate]:
        expenses[currdate]["shopping"]=0
    expenses[currdate]["shopping"] += expense


def add_entertainment_expense():
    expense=float(input("Please enter the amount of money spent: "))
    if "entertainment" not in expenses[currdate]:
        expenses[currdate]["entertainment"]=0
    expenses[currdate]["entertainment"] += expense 
    

def add_health_expense():
    expense=float(input("Please enter the amount of money spent: "))
    if "health" not in expenses[currdate]:
        expenses[currdate]["health"]=0
    expenses[currdate]["health"] += expense
    

def add_others_expense():
    expense=float(input("Please enter the amount of money spent: "))
    if "others" not in expenses[currdate]:
        expenses[currdate]["others"]=0
    expenses[currdate]["others"] += expense

def view_singleday_expenses():
    d=input("Please enter the from date in DD-MM-YYYY format:")

    with open("expenses.json","r") as f:
        expenses_dict = json.load(f)
    total = 0

    if d not in expenses_dict:
        print("No expenses for the entered date")
        return

    else:   
        for expense in expenses_dict[d].values():
            total += expense
    
    print(f"Total expenses for the date {d} is ₹{total}")

def view_multiday_expenses():
    d1=input("Please enter the from date in DD-MM-YYYY format:")
    d2=input("Please enter the to date in DD-MM-YYYY format:")

    try: 
        converted_d1 = datetime.strptime(d1,"%d-%m-%Y")
        converted_d2 = datetime.strptime(d2,"%d-%m-%Y")
    except ValueError as e:
        print(f"Invalid Format\nThe date Must be in DD-MM-YYYY Format only!!")
        return

    with open("expenses.json","r") as f:
        expenses_dict = json.load(f)

    print(f"Expenses between the dates {d1} and {d2} is as follows: ")

    for date in expenses_dict:
        curr = datetime.strptime(date,"%d-%m-%Y")
        if converted_d1 <= curr <= converted_d2:
            print(f"\nDate: {date}")
            for category in expenses_dict[date]:
                print(f"{category}: ₹{expenses_dict[date][category]}")

def delete_expense():
    try:
        d=input("Enter the date in DD-MM-YYYY Format: ")
        converted_d = datetime.strptime(d,"%d-%m-%Y")
    except ValueError as e:
        print(f"Invalid Format\nThe date Must be in DD-MM-YYYY Format only!!")
        return

    with open("expenses.json","r") as f:
        expenses_dict = json.load(f)
    if d not in expenses_dict:
        print("The entered date is not present in the expenses")
        return
    
    category = input("Enter the category to delete from: ").strip().lower()
    if category not in expenses_dict[d]:
        print("The entered category is not present in the expenses")
        return
        
    print(f"Current Expenses: ₹{expenses_dict[d][category]}")
    amt = float(input("Enter the amount of money you want to delete: "))
    if expenses_dict[d][category] <= amt:
        print("Sufficient amount is not present")
        return
    
    expenses_dict[d][category] -= amt
    print(f"₹{amt} successfully deleted")

    print(f"Current Expenses: ₹{expenses_dict[d][category]}")

    with open("expenses.json","w") as f:
        json.dump(expenses_dict,f)


'''for i in range(3):
    add_expense()
view_multiday_expenses()
delete_expense()
'''
add_expense()
view_singleday_expenses()