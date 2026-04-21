git"personal_expense_tracker" 
# Personal Expense Tracker

A simple Python-based console application to track daily expenses.

## Features
- Add expenses
- Delete expenses
- View expenses by date
- Categorize expenses into:
  - Food
  - Travel
  - Shopping
  - Entertainment
  - Health
  - Others
- Display total spending for a selected day
- Generate daily report
- Generate weekly report

## Technologies Used
- Python
- Dictionary and Lists for data storage

## How It Works
The program stores expenses in a nested dictionary structure.

- First level key: Date
- Second level key: Category
- Value: List of expenses under that category

Example structure:

```python
{
    "20-04-2026": {
        "food": [200, 150],
        "travel": [80]
    }
}