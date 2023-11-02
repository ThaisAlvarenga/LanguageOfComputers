'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Program outputs various modifications to a sentence input by user
DATE: 16/02/2023

'''

# function to capitalize the first letter of each word in sentence 
def capitalize(sent):
    # capitalize first letters in each sentence
    titledSentence = sent.title()
    # print sentence with capitalized words
    print(titledSentence)
    
# end of function

    
# function to get num of vowels in sentence sent
def getVowels(sent):

    # make a string containing all vowels
    vowels = "aeiou"
    # declare variable to keep track of count of vowels
    vowelNum = 0
    # make all words in sent lowercase to be able to compare to vowels
    lowCase = sent.lower()

    # for each letter in vowels
    for letter in vowels:
        # count how many times that letter appears in sent
        vowelNum += lowCase.count(letter)

    # return the number of vowels and the lower case which we will need later
    return vowelNum, lowCase

# end of function


# function to get and print the num of blank spaces in a sentence sent
def getBlankSpace(sent):

    # count number of spaces
    blankspaces = sent.count(" ")

    # print the number of spaces
    print("Num of spaces:", blankspaces)
    
# end of function


# function prints every word in sentence on a separate line AND
# prints the num of words in that sentence
def printWordsNSize(sent):
    # make a list out of the words in string sent
    words = sent.split()

    # print each word in the list
    for word in words:
        print(word)

    # print number of words in sent by using the length of the list
    print("Num of words:",len(words))
    
# end of function


# function to find how many times the word cat appears in sentence
def findCat(sent):

    # find the word cat in sentence
    numCat = sent.find("cat")

    # if you can't find cat, print that it was not found
    if(numCat < 0):
        print("Word cat not found")
    # else print the number of times cat appears in sent
    else:
        print("Num of cat found:", sent.count("cat"))
        
# end of function


def main():

    # get user input for sentence
    sentence = input("Write a sentence: ")

    # print original sentence
    print("Original:", sentence)

    # get amount of characters in sentence
    print("Num of characters", len(sentence))

    # capitalize first word in sentence
    capitalize(sentence)

    # vowels and lower case
    vowelCount, lowerCase = getVowels(sentence)
    
    # print num of vowels
    print("Num of vowels:", vowelCount)

    # find blank spaces
    getBlankSpaces(sentence)

    # print sentence in lower case
    print("Sentence in lower case:", lowerCase)

    # print words of sentence in separate line and the number of words
    printWordsNSize(sentence)


    # find cat in sentence
    findCat(sentence)
    
    # number of words in sentence but using one of the string methods
    # counting the spaces and adding one will give us the num of words
    print("Num of words (string method):", sentence.count(" ") + 1)

# end of function

main()
