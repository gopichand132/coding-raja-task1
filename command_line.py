import json
from datetime import datetime

# File to store transactions
TRANSACTIONS_FILE = 'transactions.json'

def load_transactions():
    try:
        with open(TRANSACTIONS_FILE, 'r') as file:
            transactions = json.load(file)
    except FileNotFoundError:
        transactions = {'income': [], 'expenses': []}
    return transactions

def save_transactions(transactions):
    with open(TRANSACTIONS_FILE, 'w') as file:
        json.dump(transactions, file)

def display_transactions(transactions):
    print("\nTransactions:")
    print("Income:")
    for income in transactions['income']:
        print(f"  - {income['category']}: {income['amount']}")

    print("\nExpenses:")
    for expense in transactions['expenses']:
        print(f"  - {expense['category']}: {expense['amount']}")

def add_transaction(transactions, transaction_type):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date_str = input("Enter date (YYYY-MM-DD, press Enter for current date): ")

    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')

    try:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    transaction = {'category': category, 'amount': amount, 'date': date.strftime('%Y-%m-%d')}
    transactions[transaction_type].append(transaction)
    save_transactions(transactions)
    print(f"{transaction_type.capitalize()} added successfully.")

def calculate_budget(transactions):
    income = sum(income['amount'] for income in transactions['income'])
    expenses = sum(expense['amount'] for expense in transactions['expenses'])
    remaining_budget = income - expenses
    return remaining_budget

def analyze_expenses(transactions):
    expense_categories = set(expense['category'] for expense in transactions['expenses'])
    
    print("\nExpense Analysis:")
    for category in expense_categories:
        total_category_expenses = sum(expense['amount'] for expense in transactions['expenses'] if expense['category'] == category)
        print(f"  - {category}: {total_category_expenses}")

def main():
    transactions = load_transactions()

    while True:
        print("\nBudget Tracker")
        print("1. Display Transactions")
        print("2. Add Income")
        print("3. Add Expense")
        print("4. Calculate Budget")
        print("5. Analyze Expenses")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            display_transactions(transactions)
        elif choice == '2':
            add_transaction(transactions, 'income')
        elif choice == '3':
            add_transaction(transactions, 'expenses')
        elif choice == '4':
            remaining_budget = calculate_budget(transactions)
            print(f"\nRemaining Budget: {remaining_budget}")
        elif choice == '5':
            analyze_expenses(transactions)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
