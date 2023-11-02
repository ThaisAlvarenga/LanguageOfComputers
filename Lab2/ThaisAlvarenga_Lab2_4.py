'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers

DESCRIPTION: Ask the user to enter two different numbers and determines the max
and the min numbers. It also determines if they are the same number

DATE: 01/02/2023

'''
# assign first number
num1 = int(input("Give me a number: "))

# assign second number
num2 = int(input("Now give me another number: "))

# check inputs
# print(num1, num2)

# check if both numbers are the same
if (num1 == num2):
    print("Both numbers are the same.")
    
# check if num1 is bigger
elif(num1 > num2):
    print("Maximum number is", num1)
    print("Minimum number is", num2)
                
# else num2 is bigger 
else:
    print("Maximum number is", num2)
    print("Minimum number is", num1)

