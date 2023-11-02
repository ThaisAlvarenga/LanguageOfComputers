'''
NAME: Thais Alvarenga 
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Data visualizations of documents and lists. For some of the exercises,
I used numpy arrays as it appeared in the tutorials of WW3 and are further explained
in https://www.w3schools.com/python/numpy/numpy_creating_arrays.asp
DATE: 01/03/2023
'''
import numpy as np
import matplotlib.pyplot as plt
from random import *

# load data from file
def loadExpenses(filename):
     # open file for reading and close it automatically when done
    with open(filename, 'r') as f:
        # read all lines from file except first (header) row
        data = f.readlines()[1:] # skip header row
    # create empty lists to hold dates and amount of dirhams
    dates = []
    amounts = []
    # for each row in the file
    for row in data:
        # split the row into columns using comma as delimiter
        cols = row.strip().split(',')
         # add the date to the dates list
        dates.append(cols[0])
        # add the amount as a float to the amounts list
        amounts.append(float(cols[2]))
        
    # return two NumPy arrays for dates and amounts
    return np.array(dates), np.array(amounts)


def main():
     # create some data
     # num of femicides in Honduras for Jan 2023 based on age group
     # taken from https://derechosdelamujer.org/project/2023/
    ageGroups = ["0-9", "10-19", "20-29","30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90-99", "u/k"]
    numDeaths = [0, 3, 11, 4, 3, 3, 1, 1, 0, 0, 12]

    # ------------ Part 2 - 1 ------------
    # ------------ Line ------------

    # plot line
    plt.plot(ageGroups, numDeaths, 'b')

    # add axis labels
    plt.xlabel('age group')
    plt.ylabel('deaths')
    plt.title('Femicides in Honduras in Jan 2023 by age groups')

    # show the plot
    plt.show()

    # ------------ Part 2 - 2 ------------
    # ------------ Scatter Graph ------------
    
    # get colors for scatter plot points
    colors = np.random.rand(len(ageGroups))
    
    # create a numpy array from the y values
    y_arr = np.array(numDeaths)

    # multiply the y values by 40 to get the size of the points
    size = y_arr * 40

    # plot the scatter graph
    plt.scatter(ageGroups, numDeaths, c = colors, s = size, alpha = 0.5)

    # add axis labels
    plt.xlabel('age group')
    plt.ylabel('deaths')
    plt.title('Femicides in Honduras in Jan 2023 by age groups')

    # show the plot
    plt.show()

    # ------------ Part 2 - 3 ------------
    # -------- Plot Two Lines ------------

    # create some meaningful data: comparing cos with sin 
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    # plot the two lines
    plt.plot(x, y1, 'b--', label='sin(x)')
    plt.plot(x, y2, 'r-', label='cos(x)')

    # add axis labels and legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Comparison of sin and cos')

    # show the plot
    plt.show()


    # ------------ Part 2 - 4 ------------
    # ------------ Histogram ------------

    # create bins for the histogram
    bins = np.arange(len(ageGroups))

    # create a histogram
    plt.bar(bins, numDeaths, width=0.8, facecolor='g', alpha=0.75)

    # set the x-axis tick labels to be the age ranges
    plt.xticks(bins, ageGroups)

    # set the y-axis limit to a reasonable value
    plt.ylim(top=max(numDeaths)*1.1)

    # add axis labels and a title
    plt.xlabel('age group')
    plt.ylabel('deaths')
    plt.title('Femicides in Honduras in Jan 2023 by age groups')

    # show the plot
    plt.show()

    # ------------ Part 2 - 5 ------------
    # ------------ Fakedata.txt

    # load data from file
    data = np.loadtxt('fakedata.txt')

    # separate data into two arrays
    x = data[:,0]
    y1 = data[:,1]
    # make data for a second line from file
    y2 = np.random.rand(len(x))


    # plot the two lines with different colors
    plt.plot(x, y1, 'b--', label='y1')
    plt.plot(x, y2, 'r-.', label='y2')
    # I'm having this issue in which both lines have the same color

    # add axis labels and legend
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Plotting Fakedata.txt')


    # show the plot
    plt.show()


    # ------------ Part 2 - 6 ------------
    # ------------ Campus Dirhams ------------
    # load expenses from csv file
    dates, amounts = loadExpenses('campusDirhams.csv')

    # compute daily expenses
    dailyExpenses = {}
    for i in range(len(dates)):
        # get the current date
        date = dates[i]
        # get the current amount
        amount = amounts[i]
         # if the date already exists in dailyExpenses 
        if date in dailyExpenses:
             # add the amount to the existing value for the date
            dailyExpenses[date] += amount
        # else create a new key-value pair for the date and amount
        else:
            dailyExpenses[date] = amount

    # create arrays for plotting
    x = np.array(list(dailyExpenses.keys()))
    y = np.array(list(dailyExpenses.values()))

    # plot the data
    plt.plot(x, y)
    plt.xlabel('Date')
    plt.ylabel('Expenses')
    plt.title('Daily Expenses')
    plt.show()


main()




