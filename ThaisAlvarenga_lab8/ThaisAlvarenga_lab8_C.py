'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Computes average for grades read from a file
DATE: 24/02/2023

'''

import random

# function I used to make the grade file
def mkGradeFile(filename):

    # file path
    filename = "files/grades.txt"

    # open file to write
    writeGrades = open(filename, "w")

    # get random grade for 10 grades
    for grade in range(10):
        writeGrades.write(str(random.randint(1,100)) + "\n")

    # close file
    writeGrades.close()
    
# end of mkGradeFile



# function to read a file 
def readFile(filename):

    # open file for read
    studentGrades = open(filename, "r")

    # for each line in file
    for line in studentGrades:

        # clean the line
        line = line.rstrip()
        # append the line to grade list
        grade.append(int(line))
        
    # print grade just to check    
    print(grade)

    # close file
    studentGrades.close()
# end readFile



# function to get average of grade
def getAverage():

    # initalize variable to keep track of total
    total = 0

    # for each element in grade list
    for element in grade:
        # add element to total
        total += element

    # computer the average
    avg = total / len(grade)

    # return average
    return avg

    
        
# initialize variable to hold grade  
grade = []   

def main():

    # used this function to make a file with grades
    # mkGradeFile(filename)

    filename = "files/grades.txt"

    # read file to get grades
    readFile(filename)

    # compute average grade
    average = getAverage()

    # print average grade
    print("The average grade is:", average)
    
# end main



main()
