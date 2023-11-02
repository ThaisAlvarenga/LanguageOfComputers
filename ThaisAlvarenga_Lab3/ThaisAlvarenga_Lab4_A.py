'''
NAME: Thais Alvarenga
COURSE: Language Of Computers
DESCRIPTION: Generates 10 numbers randomly between 1 and 1000,
printing each number, and its square

DATE:06/02/2023
'''
# import random module
import random

# repeat next steps 10 times
for count in range(10):
    # get a random number
    num = random.randint(1,1000)
    # calculate num's squared number
    sqr = num **2

    # print calculated values
    print("num =", num, "squared", sqr)
