'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Etisalat databse allows the user to enter “1” to add a customer name,
“2” to look up (search for) a customer, and “3“to delete a customer”
DATE: 22/02/2023

'''

# function to print menu
def printMenu():
    # print option of choices for user
    print("1. Add a customer")
    print("2. Look up a customer")
    print("3. Delete a customer")
    print("-1. Quit")
    
# end printMenu

# function to add a costumer to costumers list
def addCostumer(customers):
    # enter costumer information
    name = input("Enter name:")
    phone = input("Enter phone #:")
    balance = float(input("Enter the balance owed at the end of the month:"))

    # add costumer to list
    customers.append([name, phone, balance])

    # tell user costumer was added
    print("Costumer has been added")
    
# end addCostumer


# function to find a costumer in database
def findCustomer(customers):
    
    # initialize list to host the found costumer
    foundCustomer = []

    # input mode for search of customer
    mode = input("Search by name (n) or phone number (p)? ")
    
    # if user choose to search by name
    if mode == "n":
        
        # input name
        name = input("Enter name: ")

        # for each person on customer list
        for person in customers:
            
            # if cutomer's name is equal to input name
            if person[0] == name:
                
                # then the found customer is that person
                foundCustomer = person
                
            
    # if user is searching by phone number    
    if mode == "p":
        
        # input phone number
        phone = input("Enter phone #: ")

        # for each person on customer list
        for person in customers:
            
            # if cutomer's phone # is equal to input phone
            if person[1] == phone:
                # then the found customer is that person
                foundCustomer = person
                
    # if we found the costumer
    if foundCustomer:
        
        # print their info
        print("Name:", foundCustomer[0])
        print("Phone:", foundCustomer[1])
        print("Balance owed:", foundCustomer[2], "AED")
        
    # else tell user that costumer was not found
    else:
        print("Sorry. The customer is not an Etisalat customer")
        
# end findCustomer


# function to delete a costumer from database
def deleteCustomer(customers):

    # if costumer list is empty
    if len(customers) == 0:
        # no costumers left so return
        print("No customers left to delete.")
        return
        
    # else if list has costumers   
    else:
        # input mode for search of customer
        mode = input("Search by name (n) or phone number (p)? ")
    
        # if user choose to search by name
        if mode == "n":
            
            # input name
            name = input("Enter name: ")

            # for each person on customer list
            for person in customers:
                
                # if cutomer's name is equal to input name
                if person[0] == name:
                    
                    # remove customer
                    customers.remove(person)
                    print("Customer has been deleted")
                # else tell user that costumer was not found
                else:
                    print("Sorry. The customer is not an Etisalat customer")
                
        # if user is searching by phone number    
        if mode == "p":
            
            # input phone number
            phone = input("Enter phone #: ")

            # for each person on customer list
            for person in customers:
                
                # if cutomer's phone # is equal to input phone
                if person[1] == phone:
                    # remove customer
                    customers.remove(person)
                    print("Customer has been deleted")

                # else tell user that costumer was not found
                else:
                    print("Sorry. The customer is not an Etisalat customer")
        
# end deleteCustomer()


# inisitalize multidimensional list that will serve as database
customers = []



def main():
    # initialize user choice variable
    userChoice = 0

    # print welcome message
    print("Welcome to the Etisalat Database!")

    # while choice is not -1 (to exit)
    while userChoice != -1:

        # Print the menu
        printMenu()

        # Get the user's choice
        userChoice = int(input("Enter your choice: "))

        # if 1 then add costumer
        if userChoice == 1:
            addCostumer(customers)

        # if 2 then search for costumer
        elif userChoice == 2:
            findCustomer(customers)

        # if 3 delete a customer
        elif userChoice == 3:
            deleteCustomer(customers)

        # if -1 quit program
        elif userChoice == -1:
            break

        # else input not valid
        else:
            print("Invalid choice. Please reenter selection")
            # print menu again
            printMenu()
            
    # print exit message
    print("Thank you for using Etisalat")
            



main()
