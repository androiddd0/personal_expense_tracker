'''
functions:
add_food_expense()
add_expense()
'''
import json

'''example = [
    {"name":"anirudh","age":19},
    {"name":"cheta","age":20}
]

with open("example.json","w") as file:
    json.dump(example,file)
'''

currdate=input("Please enter the date of the expense in DD-MM-YYYY format:")
expenses = {}

def add_expense():
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


def view_expense():
    d1=input("Please enter the from date in DD-MM-YYYY format:")
    d2=input("Please enter the to date in DD-MM-YYYY format:")
    with open("expenses.json","r"):
        if d1 in expenses or d2 in expenses:
            data=json.dumps(expenses)
            print(data)
    

'''while 1:  
    add_expense()
    with open("expenses.json","w") as file:
        json.dump(expenses,file)
'''
for i in range(3):
    add_expense()
view_expense()