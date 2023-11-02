'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers

DESCRIPTION: Class 8: Working with files
How to read data from a file
Save things in a file
Basic search

Files are stored in long term memory, not in RAM
Files are always text, they have the same functionality as the input()
For a file, the smallest unit is the line

Extensions are usually .txt, .csv, .dat. CSV are the most used ones
These are text plain files, excel and word files usually have other instructions
about formatting. So Python will read everything and not understand.

DATE: 22/02/2023

'''

import random

words = []

def readFile(filename):
    # 1 import the file reader - function is called open("location of file", mode)
        # the mode tells if you should read, write or append the file
            # write will overwrite the data in the file
            # append will add the things to what is already in the file

    data = open(filename, 'r')
    
    # 2 loop through lines

    for line in data:
        line = line.rstrip()
        print(line)

        
    
def main():
    
    filename = "file1.txt"

    readFile(filename)
    
# end of main()

main()
