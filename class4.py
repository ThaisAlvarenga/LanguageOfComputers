'''
NAME: Thais Alvarenga
COURSE: Language Of Computers
DESCRIPTION:

DATE:06/02/2023
'''

# demo loop (while)

#num = 1

#while (num <= 100):

#    if(num % 2 == 0):
#        print(num,"is even")

#    else:
#        print(num, "is odd")

#    num += 5;

#print("end")

# -----------------------------------------------

#for num in range(1,101):

    #if(num % 2 == 0):
        #print(num, "The num is even")

    #else:
        #print(num, "The num is odds")

# -----------------------------------------------

# accumulator, this is a variable that hosts the total and is correctly initialize
# so as to not affect the input data that we have
#total = 0;

#for students in range(1,4):
    #grade = float (input ("enter your grade: "))
    
    #total += grade;

#print(total)
# students will be 3 because that is its range
#print(total / students)

# -----------------------------------------------

'''
total = 0
grade = float(input("enter a grade or -1 to stop: "))

students = 0

while(grade != -1):

    total += grade

    students += 1

    grade = float(input("enter a grade or -1 to stop: "))
    # print(grade)

# get the average only if the num of students is not 0
if(students != 0):
    avg = (total / students)
    print("The avg is:", avg)

'''

import random
word = ''

for num in range(5):

    lotto = random.randint(1,100000)
    # another way of doing it could be
    lotto = int(random.random()*100)

    letter = random.choice('abcdefghijklmnopqrstuvwxyz')

    word += letter

    print(lotto)

print(word)
