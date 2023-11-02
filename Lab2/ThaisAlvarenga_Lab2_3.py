'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers

DESCRIPTION: Asks the user to enter a number between 1 and 7. It outputs the equivalent day of the week
based on the user input

DATE: 01/02/2023
'''

# get user input
num = int(input("enter a number between 1 to 7: "))


print(num)

# check for the day of the week based on the num value assigned
if ( num == 1):
    print("You entered", num, "Today is Sunday")

elif ( num == 2):
    print("You entered", num, "Today is Monday")

elif ( num == 3):
    print("You entered", num, "Today is Tuesday")

elif ( num == 4):
    print("You entered", num, "Today is Wednesday")

elif ( num == 5):
    print("You entered", num, "Today is Thursday")

elif ( num == 6):
    print("You entered", num, "Today is Friday")

elif ( num == 7):
    print("You entered", num, "Today is Saturday")

# print warning for invalid daata
else:
    print("Invalid input. You should input number between 1 and 7")
