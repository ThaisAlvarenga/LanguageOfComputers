''' Name: Thais Alvarenga NetdID: ata381
Course: [The Course Number]
Description:  Allows the user to enter the names of two people and their corresponding
dates of birth. It then prints out the names and dates of birth, and determines who is older.
Date: 04/02/2023
'''

# input 1st person's name
name1 = input("Enter the first person's name: ")
# input for 1st person's date of birth
birthdate1 = int(input("Enter their birthday at an 8 digit number (YYYYMMDD): "))
# input for 2nd person's name
name2 = input("Enter the first person's name: ")
# input 2nd person's birtdate
birthdate2 = int(input("Enter their birthday at an 8 digit number (YYYYMMDD): "))

# get day by leaving the last 2 digits in the birtdate number
day1 = birthdate1 % 100
# gets month by removing the last 2 digits and then the first 4 digits
# to leave the 2 digits in the middle that make up the month
month1 = birthdate1 // 100 % 100
# get year by removing last 4 digits using integer division
year1 = birthdate1 // 1000

# re[eat the above process for birthdate 2
day2 = birthdate2 % 100
month2 = birthdate2 // 100 % 100
year2 = birthdate2 // 1000

# write a space to separate output from input
print('')

# print person date of birth 
print(name1, "was born on", str(day1) + "/" + str(month1) + "/"+ str(year1))
print(name2, "was born on",  str(day2) + "/" + str(month2) + "/"+ str(year2))

# check if the two people were born on the same year
if year1 == year2:

    # check if people were born on the same month
    if (month1 == month2):
        # if they are born on the same day, they are the same age
        if (day1 == day2):
            print(name1, "and", name2, "are the same age!")
        # if name1 was born days before name2, name1 is older    
        elif (day1 < day2):
            print(name1, "is older than", name2)
        # else name2 would be older than name1
        else:
            print(name2, "is older than", name1)
    # if name1 was born a month before name2 than name1 is older   
    elif (month1 < month2):
        print(name1, "is older than", name2)
    # else name2 would be older 
    else:
        print(name2, "is older than", name1)
# if name1 was born years before name2, then name1 is older
elif (year1 < year2):
    print(name1, "is older than", name2)
# else name2 is older
else:
    print(name2, "is older than", name1)
