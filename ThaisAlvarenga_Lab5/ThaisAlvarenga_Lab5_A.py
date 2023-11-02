'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Converts km to mi, kg to lb and cm to in
DATE: 14/02/2023
'''
# function to do conversions according to user input
def doConversion(mod, val):

    # if user choose to convert km to mi
    if( mod == 1):

        # assign the result of conversion
        result = km_mi(val)
        # print original value and conversion
        print(val, "km =", result ,"mi")

    # if user choose to convert kg to pounds
    elif(mod == 2):
        
        # assign the result of conversion
        result = kg_lbs(val)
        # print original value and conversion
        print(val, "kg =", result ,"lbs")

    # if user choose to convert cm to inches
    elif(mod == 3):
        # assign the result of conversion
        result = cm_in(val)
        # print original value and conversion
        print(val, "cm =", result ,"in")

    # if user input an invalid number
    else:
        # print warning
        print("Invalid input")
# end of doConversion()

        

# function to convert from kilometers to miles
def km_mi(km):
    
    mi = km * 0.62

    return mi
# end of km_mi()



# function to convert kilograms to pounds
def kg_lbs(kg):

    lbs = kg * 2.2

    return lbs
# end of kg_lbs()



# function to convert centimeter to inches
def cm_in(cm):
    inch = cm * 0.39
    
    return (inch)
# end of cm_in()

# function to enter user input
def getUserInput():
    # input user choice to convert 
    mod = int(input("Press 1 to convert from km to mi \nPress 2 to convert kg to lbs \nPress 3 to convert cm to in: "))
    # input value user wants to be converted
    val = float(input("Input value you want to convert:"))

    return mod, val
# end of getUserInput()
    
# main function to run the program
def main():
    
    # get user input and assign it to respective variables
    mode, value = getUserInput()

    # make conversion according to user choice
    doConversion(mode, value)
   

# end of main()


main()
