import pandas as pd
df = pd.read_csv("expenses.csv")
print(df.head())
print(df.info())
total_expense = df["Amount"].sum()
print(f"Total expense is = Rs {total_expense}")
expense_by_group = df.groupby("Category")["Amount"].sum()
#finding the identity of the index where maximum value exists.

highest_spending = expense_by_group.idxmax()
print(f"Expense category with the highest spending = {highest_spending}")
#business_question show me all expenses greater than 1000
greater_than_1000= df[df["Amount"]>1000]
print("Expenses greater than Rs 1000")
print(greater_than_1000)
#i learnt how to filter data today

#next ques: how many expenses are greater than 1000?

print(f"No. of expenses greater than Rs 1000 = {greater_than_1000.shape[0]} ")