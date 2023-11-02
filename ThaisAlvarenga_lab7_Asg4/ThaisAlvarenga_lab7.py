'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Create a board 9X9 and initialize to random num between 1 and 9.
Then do multiple manipulations to this board
DATE: 21/02/2023

'''

import random

# function to generate board
def generateBoard(newboard, height, width):
    
    # assign random numbers to each element in the board
    for row in range(height):
        
        currentRow = []
        # for the num of columns in board
        
        for column in range(width):
            # initialize the elements in each row to a num btw 1 and 9
            currentRow.append(random.randint(1,9))
            
        # add currentRow to board
        newboard.append(currentRow)
        
    # return created board
    return newboard

# end of generateBoard()


# function to print board
def printBoard(board):
    
    # for each row in board
    for row in board:
        
        # for each element in the row 
        for element in row:
            # print
            print(str(element)+ "\t" , end ="")
            
        # move to next line (row)
        print()
        
# end of printBoard()


# function that counts how many times num appears in board
def countNum(board, num):
    # initalize count variable
    count = 0
    
    for row in board:
        # add num of times num appears in row
        count += row.count(num)

    # return count
    return count

# end of countNum



# function to compute average of each element
def average(board, height, width ):
    
    # initialize total
    total = 0
    
    # for each row
    for row in board:
        # compute the total of the row
        total += sum(row)
        
    # compute average
    average = total / (height * width)

    # return average
    return average
        
# end of average()



# functions that deletes the row num appears in
def deleteRowWithNum(board, num):

    for row in board:
        # if num appears in boards
        if num in row:
            
            # remove the row
            board.remove(row)
            
# end of deleteRowWithNum()



# functions that changeElement()
def changeElement(board, element, newElement):
    
    for row in range(len(board)):
        
        for col in range(len(board[row])):
            # if element in boards contains element value
            if board[row][col] == element:
                # replace it with the new element value
                board[row][col] = newElement
                
# end of changeElement()



def main():
    # create variable to hold the board
    board = []
    # define width and height of board
    boardHeight = 9
    boardWidth = 9

    # generate elements in board
    board = generateBoard(board, boardHeight, boardWidth)

    # print board
    printBoard(board)

    # count how many 2's in board
    numOf2 = countNum(board, 2)
    # print 
    print("Number of times 2 appears in the board:", numOf2)

    # compute average of all the numbers in the board
    avg = average(board, boardHeight, boardWidth)
    print("Average of board elements:", avg)

    #delete rows that contain 6
    deleteRowWithNum(board, 6)

    #print board with 6 deleted
    print("Board without 6's:")
    printBoard(board)


    # print length of the board
    print("Length of board:", len(board))
    # print length of the first 
    print("Length of first element in board:", len(board[0]))
    # the length of last element
    print("Length of last element in board:", len(board[-1]))

    # append ["mouse", "camel"] to board
    board.append(["mouse", "camel"])
    # print boards
    print("Board with mouse, camel:")
    printBoard(board)

    # replace mouse with cat
    changeElement(board, "mouse", "cat")
    #print board with new change
    print("Board with cat instead of mouse:")
    printBoard(board)



main()
