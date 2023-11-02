'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Computes your projected expenses for the next two years.
User enters their expense for each month from Jan to December for each year.
Program prints each expense per month, the total for each year and the the sum
of the totals  for both years.
DATE:08/02/2023

'''

# declare variables to keep track of yearly expenses and the total expense of
# two years
yearlyTotal = 0
totalForYears = 0

# for each year
for year in range (2):

    # print to show user which year they are in
    print("Expenses for year", str(year + 1), ":")

    # for each month in the year
    for month in range(12):
        # get expense for the month
        monthly = float(input("Expense for month: "))
        # print the expense
        print("Month", str(month + 1), ": ", monthly)

        # add the expense of that month to the yearly total
        yearlyTotal += monthly

    # print the total expenses of the year
    print("Total spent for year", str(year + 1), ": ", yearlyTotal)
    print()

    # add expenses of the year to the total expese for the 2 years
    totalForYears += yearlyTotal

    # set the yearly total back to 0 to reuse variable for year 2
    yearlyTotal = 0
    
# print total for all years
print("Total for both years:", totalForYears)
