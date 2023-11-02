'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Program outputs name and birth of the user according to their input
DATE: 16/02/2023

'''

#function to get user input
def getUserInput():
    
    name = str(input("Write your name:"))

    birthday = input("Write your birthday as an 8 digit number e.g., May 12 1953: 19530512:")

    return name, birthday

# end of function


# function to format user's name
def formatName(userName):
    # make all first letters in a word upper case
    userName = userName.title()
    # split the name in first name and last name
    formattedName = userName.split()

    # return the new format of the name
    return formattedName

# end of function


# function to format user's brithday
def formatBirthday(userBirthday):

    # split the birthday input by year, day and month 
    birthYear = userBirthday[0:4]
    birthMonth = userBirthday[4:6]
    birthDay =  userBirthday[6:]

    # rewrite the birthday as DD/MM/YYYY and assign to variable
    formattedBirthday = birthDay + "/" + birthMonth + "/" + birthYear

    # return the new birthday format
    return formattedBirthday

# end of function


def main():
    # get user input
    name, birthday = getUserInput()

    # reformat name
    name = formatName(name);

    # split and format  year
    birthday = formatBirthday(birthday)

    # print the output
    print(name[0], name[1], "was born on", birthday)

# end of function


main()
