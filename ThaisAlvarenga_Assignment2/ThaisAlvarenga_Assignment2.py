'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generates the following carpet pattern
DATE: 11/02/2023

'''

myRow = 28
myCol = 28

# First star line
for row in range(myRow):
    print("*", end = "")

print()

for row in range(myRow):
    print("*", end = "")

print()


for row in range(3):
    for column in range(7):
        print("*", end = "")
    for column in range(6):
        print(" ", end = "")
    for column in range(2):
        print("*", end = "")
    for column in range(6):
        print(" ", end = "")
    for column in range(7):
        print("*", end = "")
    print()


# Penultimate Patter (3's)
for row in range(5):
    for column in range(3):
        print("*", end = "")

    for column in range(3):
        print(" ", end = "")

print()

for row in range(4):
    for column in range(3):
        print(" ", end = "")

    for column in range(3):
        print("*", end = "")

print()

#diamond pattern
diamondHeight = 7  # size of diamond
width = myCol - 4  # width of output

# print a diamond pattern to the side of an accent pattern
for i in range(diamondHeight):
    # print left diamond
    for j in range(diamondHeight - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    # print separator
    print(" " * ((width - 2 * diamondHeight) // 4), end="")
    # print right accent pattern
    for j in range(2 * i + 1):
        print("*", end="")
    print()
# reverse the diamond
for i in range(diamondHeight - 2, -1, -1):
    # print left diamond
    for j in range(diamondHeight - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    # print separator
    print(" " * ((width - 2 * diamondHeight) // 4), end="")
    # print right accent pattern
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# dotted pattern
numStar = 4  # size of the pattern

# loops for the number of stars 
for colSection in range(numStar):
    # print a row of 4 asterisks
    for star in range(numStar):
        print("*", end="")
    # print some spaces
    print("   ", end="")
    # print a row of 3 asterisks
    for star in range(numStar-1):
        print("*", end="")
    # print some spaces
    print("   ", end="")
    # print a row of 2 asterisks
    for star in range(numStar-2):
        print("*", end="")
    # print some spaces
    print("  ", end="")
    # print a single asterisk
    print("*", end="")
    # print some spaces
    print("  ", end="")
    # print a row of 3 asterisks
    for star in range(numStar-1):
        print("*", end="")
    # print some spaces
    print("   ", end="")
    # print a row of 2 asterisks
    for star in range(numStar-2):
        print("*", end="")
    # print a newline
    print()

# 3 star checker pattern from before
for row in range(5):
    for column in range(3):
        print("*", end = "")

    for column in range(3):
        print(" ", end = "")

print()

for row in range(4):
    for column in range(3):
        print(" ", end = "")

    for column in range(3):
        print("*", end = "")

print()


# Last 2 Rows of star lines (like from before)      
for row in range(28):
    print("*", end = "")

print()

for row in range(myRow):
    print("*", end = "")
    
print()
