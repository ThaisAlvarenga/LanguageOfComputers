'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Reads and prints and writes my favorite lyrics to another file
DATE: 24/02/2023

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



# funciton to copy lyrics on a new file
def copyLyrics():

    # assign variable for location of file
    newFile = "files/lyricsCopy.txt"

    # open file to write
    filew = open(newFile, "w")

    # write each line of lyrics in copy file
    for line in lyrics:
        filew.write(line + "\n")

    # close the file
    filew.close()

    # print message to confirm it was copied
    print("\nLyrics copied to a new file")
    
# end of copy File



# arrray for lyrics    
lyrics = []



def main():

    # assign name of file to varaible
    filename = "files/lyrics.txt"
    
    # read the File
    readFile(filename)

    # copy lyrics to new file
    copyLyrics()

 # end of main



main()
