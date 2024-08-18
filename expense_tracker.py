import csv
import os

def initialize_csv(file_name='expenses.csv'):
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Description', 'Amount', 'Category'])

initialize_csv()
from datetime import datetime

def log_expense(file_name='expenses.csv'):
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Transport, Utilities): ")

    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount, category])

    print("Expense logged successfully!")
import pandas as pd

def display_summary(file_name='expenses.csv'):
    df = pd.read_csv(file_name)
    print("\nExpense Summary by Category:")
    summary = df.groupby('Category')['Amount'].sum()
    print(summary)

    total = df['Amount'].sum()
    print(f"\nTotal Expenses: {total}")
import matplotlib.pyplot as plt

def visualize_expenses(file_name='expenses.csv'):
    df = pd.read_csv(file_name)
    summary = df.groupby('Category')['Amount'].sum()

    summary.plot(kind='bar')
    plt.title('Expenses by Category')
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.show()
def menu():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Log Expense")
        print("2. View Summary")
        print("3. Visualize Expenses")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            log_expense()
        elif choice == '2':
            display_summary()
        elif choice == '3':
            visualize_expenses()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    menu()
