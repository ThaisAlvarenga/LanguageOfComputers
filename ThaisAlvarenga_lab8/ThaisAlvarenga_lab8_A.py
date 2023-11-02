'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Reads and prints my favorite lyrics from file
DATE: 22/02/2023

'''

# function to read a file
def readFile(filename):

    # open file for read
    favoriteLyrics = open(filename, "r")

    # for each line of txt file
    for verse in favoriteLyrics:
        # remove any trailing characters from a string
        verse = verse.rstrip()
        # append verse to lyrics list
        lyrics.append(verse)
        # print
        print(verse)
        
    # close file
    favoriteLyrics.close()
    
# end of readFile()


# function gets num of words per line
def getWordsPerLine():
    # initialize a list to hold num of words per line
    wordCount = []
    # for each line of the lyrics
    for line in lyrics:
        #get the number of words 
        wordCount.append(len(line.split()))

    # return list with word count
    return wordCount

# end of getWordsPerLine()    



def printWordsPerLine(wordPerLineList):
    # for each line 
    for line in range(len(wordPerLineList)):
        # print the amount of words 
        print("Line ", line + 1, "has", wordPerLineList[line], "words")
        
# end of printWordsPerLine()



# arrray for lyrics    
lyrics = []



def main():

    # assign name of file to varaible
    filename = "files/lyrics.txt"
    
    # read the File
    readFile(filename)

    #print(lyrics)

    print("\nLine count:", len(lyrics))

    # make a list to keep track of word count of each line
    wordInLine = getWordsPerLine()

    # print the wordcount of each line
    printWordsPerLine(wordInLine)

 # end of main



main()
