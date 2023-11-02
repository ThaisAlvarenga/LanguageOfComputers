'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generates a 10 character password with  2 capitalletters
5 small letters, 2 numbers between 0 and 9, and 1 character from this
selection @#$%&+ 
DATE:07/02/2023
'''
# import module
import random

# declare variable to hold password
password = ''

# declare variable to hold capital letters
capitalLetters = ''
# declare variable to hold lower case letter
lowercaseLetters = ''
# declare variable to store digits
digits = ''
# declare variable to store 1 character
character = ''

# randomly generate 2 capital letters
for i in range(2):
    capitalLetters += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# randomly generate 5 small letters
for i in range(5):
    lowercaseLetters += random.choice('abcdefghijklmnopqrstuvwxyz')

# generate 2 random digits betwee 0 and 9
for i in range(2):
    digits += str(random.randint(0,9))

# randomly choose a character
character = random.choice('@#$%&+')

# add all individually generated components to form a strong password
password += capitalLetters + lowercaseLetters + digits + character

# print password created
print("Your strong password is: ", password)

