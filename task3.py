import pandas as pd

expenses = pd.DataFrame(columns=["Date", "Description", "Amount"])

while True:
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter a description: ")
    amount = float(input("Enter the amount: "))

    new_expense = pd.DataFrame({"Date": [date], "Description": [description], "Amount": [amount]})
    expenses = pd.concat([expenses, new_expense], ignore_index=True)

    another = input("Add another expense? (yes/no): ")
    if another.lower() != "yes":
        break

expenses.to_csv("expenses.csv", index=False)

import pandas as pd
import matplotlib.pyplot as plt

expenses = pd.read_csv("expenses.csv")

expenses["Date"] = pd.to_datetime(expenses["Date"])

monthly_expenses = expenses.groupby(expenses["Date"].dt.strftime("%Y-%m"))["Amount"].sum()

plt.bar(monthly_expenses.index, monthly_expenses)
plt.xlabel("Month")
plt.ylabel("Total Expenses")
plt.title("Monthly Expense Report")
plt.xticks(rotation=45)
plt.show()

while True:
    selected_month = input("Enter the month (YYYY-MM) to view detailed expenses: ")
    if selected_month in monthly_expenses.index:
        print(expenses[expenses["Date"].dt.strftime("%Y-%m") == selected_month])
        break
    else:
        print("Month not found.")
