'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: print the multiplication table for numbers between 1 and n
(n is a number entered by the user and it should be between 2 and 10).
DATE:08/02/2023
'''

# enter user input for number of multiplication table
num1 = int( input("Enter a number between 2 and 10: "))

# for each row in the table 
for row in range(1,num1+1):

    # for each column in the multiplication table
    for col in range(1, num1+1):
        # multiply number of row by number of column
        print(str(row*col), '\t', '|', '\t', end='')
    # print on next line
    print()
