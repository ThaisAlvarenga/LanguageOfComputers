'''
NAME: Thais Alvarenga
DATE: 30/01/2023

Description: Add the total of your monthly expenses at NYUAD and calculates the
average of for all of the expenses
'''

# get user's expenses 
expense1 = float(input("Expenses for 1st week of the month: "))
print("Expense 1:", format(expense1, ".2f"), "AED")
expense2 = float(input("Expenses for 2nd week of the month: "))
print("Expense 2:", format(expense2, ".2f"), "AED")
expense3 = float(input("Expenses for 3rd week of the month: "))
print("Expense 3:", format(expense3, ".2f"), "AED")
expense4 = float(input("Expenses for 4th week of the month: "))
print("Expense 4:", format(expense4, ".2f"), "AED")
expense5 = float(input("Expenses for 5th week of the month: "))
print("Expense 5:", format(expense5, ".2f"), "AED")

# sum the total  of the expenses per week
total = expense1 + expense2 + expense3 + expense4 + expense5

# calculate the average of the expenses
avg = total/5


print()
print("Total:", format(total,".2f"), " AED")
print("Average expense per week:",format(avg,".2f"), " AED")
