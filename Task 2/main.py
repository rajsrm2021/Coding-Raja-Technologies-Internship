import sqlite3
import os

# Function to create a new transaction
def add_transaction(category, transaction_type, amount):
    conn = sqlite3.connect("budget_tracker.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO transactions (category, type, amount, date) VALUES (?, ?, ?, datetime('now'))",
                (category, transaction_type, amount))
    conn.commit()
    conn.close()

# Function to calculate remaining budget
def calculate_budget():
    conn = sqlite3.connect("budget_tracker.db")
    cur = conn.cursor()
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='Income'")
    income = cur.fetchone()[0] or 0
    cur.execute("SELECT SUM(amount) FROM transactions WHERE type='Expense'")
    expenses = cur.fetchone()[0] or 0
    conn.close()
    return income - expenses

# Function to analyze expenses by category
def analyze_expenses():
    conn = sqlite3.connect("budget_tracker.db")
    cur = conn.cursor()
    cur.execute("SELECT category, SUM(amount) FROM transactions WHERE type='Expense' GROUP BY category")
    expense_data = cur.fetchall()
    conn.close()
    return expense_data

# Main function to run the budget tracker
def main():
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. View Expense Analysis")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter income amount: "))
            add_transaction("Income", "Income", amount)
            print("Income added successfully!")
        elif choice == "2":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_transaction(category, "Expense", amount)
            print("Expense added successfully!")
        elif choice == "3":
            remaining_budget = calculate_budget()
            print(f"Remaining Budget: {remaining_budget}")
        elif choice == "4":
            expense_data = analyze_expenses()
            print("Expense Analysis:")
            for category, amount in expense_data:
                print(f"{category}: {amount}")
        elif choice == "5":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Check if the database file exists, if not, create it
    if not os.path.exists("budget_tracker.db"):
        with open("budget_tracker.db", "w"):
            pass
    main()
