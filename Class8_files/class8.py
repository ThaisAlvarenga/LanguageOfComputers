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
        words.append(line)
        print(line)
    
    print(words)

    # this is very important
    data.close()

    

def copyFile(filename, filename2):
     data = open(filename, 'r')
     dataw = open(filename2, "w")

     for line in data:
         print(line.rstrip())

         if("Imagine" in line):
             line = line.replace("Imagine", "unimagine")
             
         dataw.write(line)

     print(line)
     data.close()
     
    

def writeFile():
    myFile = "newFile.txt"

    filew = open(myFile, "w")

    #filew.write("Hello from newfile \n")
    #filew.write("This is another hello\n")

    filew.write("hello NYUAD \n")

    # closing the file is very important to make sure it writes correctly
    filew.close()
        

    
def main():

    
    #filename = "file1.txt"

    #readFile(filename)

    # select a word at random
    #secretWord = random.choice(words)

    #print("secret word is:", secretWord)
    

    #filename = "grades.txt"

    #writeFile()

    #print( (sum(words)) / (len(words)) )


    filename = "imagine.txt"

    filename2 = "unimagine.txt"

    copyFile(filename, filename2)
    

    
    
    
# end of main()

main()




'''
HangMan game:

word is word

_ _ _ _

_ _ r _

   _______________
  |              |
  |              |
  |              |
 _|_             |
/   \            |
\_ _/            |
  |              |
 _|_             |
  |              |
  |              |
  |              |
 / \   __________|






When player looses

   _________
  /         \
 |           |
 |    RIP    |
 |           |
 |           |
 |           |
 /____________\
 
'''
    

