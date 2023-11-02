'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: User to enters their monthly expenses for one year and the program outputs the total
expenses for the year, the average expense per month, the minimum and maximm amount spent. 
DATE:07/02/2023
'''
# declare value for total
total = 0
# declare variable for maximum value
maximum = 0
# declare variable with a number bigger than all others
minimum = float('inf')

# initialize variable for condition of the while loop
stopInput = 0;

# while user does not exit program
while (stopInput != -1):
    # for each month of the year
    for month in range(12):
        # get user expense for each month
        monthExpense = float(input("Enter your expense for the month: "))
        # print number of month and the expense of that month
        print('Expense of month', str(month+1) + ': ', str(monthExpense))

        #add expense to the total
        total += monthExpense

        # if monthly expense is bigger than the maximum
        if(monthExpense > maximum):
            # set the expense of the month as max
            maximum = monthExpense
            
        # else if monthly expense is less than the minimum
        elif(monthExpense < minimum):
            # set the minimum to the expense of that month
            minimum = monthExpense
            
    # ask user to exit program
    stopInput = int(input('Enter -1 to exit program:'))
    # calculate the average expense per month of the year    
    avg = total/12

# print values calculated
print('total:', total)
print('avg expense:', avg)
print('min', minimum)
print('max:', maximum)
