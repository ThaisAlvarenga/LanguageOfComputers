'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Aks user to input an animal name, compares input to a list of animal
names and does some operations to that animal list. 
DATE: 16/02/2023

'''
# import module
import random


# function to check is user animal is in the animal list
def checkInList(useranimal, animals):
    # check if user animal is in my animal list
    if useranimal in animals:
        print("Your animal is in my list!")
    else:
        print("Your animal is not in my list :(")
# end of function


# function to compare user animal to random word in animal list
def checkWithRandomWord(useranimal, animals):
    
     # select a word from the list randomly
    randomWord = random.choice(animals)

    # compare random word with user input and print accordingly
    if(randomWord.lower() == useranimal.lower()):
        print("You guessed my random animal")
    else:
        print("You did not guess my random animal correctly")
# end of function



# function for two different ways to print the last elements        
def getLastElement(animals):

    # using negative index
    print("Last element:", animals[-1])
    # using the length to get index of last number
    print("Last element:", animals[len(animals)-1])
# end of function
    
def main():

    # set list of words
    myAnimals = ["panda", "cat", "dog", "horse", "fish", "falcon", "tardigrade"]

    #ask the user to enter an animal name
    userAnimal = input("Give me an animal")

    # check to see if an animal in list or not
    checkInList(userAnimal, myAnimals)

    # check if the user entered name is the same as the random word
    checkWithRandomWord(userAnimal, myAnimals)

    # find out how many times “cat” appears in the list
    catNum = myAnimals.count("cat")
    print("Num of cats in mmy list:", catNum)

    # print  2nd Element to 4th
    print("Print element 2 to 4",myAnimals[1:4])

    # print list in reverse
    print("Reverse list", myAnimals[::-1])

    # 2 different ways to get last element in list
    getLastElement(myAnimals)

    # replace the 2nd element in the above list with mouse.
    myAnimals[1] = "mouse"
    print("Replace element 2 with mouse: ", myAnimals)

    # append an animal to the list
    myAnimals.append("monkey")
    print("Append 1 animal", myAnimals)

    # remove the last animal
    myAnimals.pop()
    print("Remove last animal", myAnimals)
    
main()
