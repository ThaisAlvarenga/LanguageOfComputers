'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers

DESCRIPTION: Informs the traveler if the have to pay full price for their flight ticket
based on their age (children under 8 don't pay)

DATE: 01/02/2023

'''

# welcome text
print("Welcome to Etihad Airways")

# input traveler's age
age = int(input("Please enter the age of the traveler to reserve a ticket: "))

# check is user is under 8 years of age
if (age > 0) and (age <= 8):
    print("“The ticket is on us – you get to fly from US to Abu Dhabi for Free”")

# check if user has to pay full price
elif (age  > 8):
    print("You have to pay full price to fly to Abu Dhabi from the US ")

# catch all invalid data
else:
    print("Invalid/strange input")
