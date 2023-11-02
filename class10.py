'''

In a text file, the columns are separated by a space
In a csv file, the columns are devided by a comma , 
'''

'''
# demo data visualization

import numpy as np
import pylab as pl

# get data
x1 = [1,2,3,4]
y1 = [1,4,6,8]

x2 = [1,4,5,10]
y2 = [1, 16, 25, 100]

# this plots in memory, we need a graphic resource to see the plot
pl.plot(x1,y1,x2,y2, "r--") # third argument is b for blue or r for r and -- for dash line
pl.savefig("thais.png")
pl.savefig("thais.eps") # this has better resolution

pl.title("My Basic Plot")
# makae lables
pl.xlabel("x axis")
pl.ylabel("y axis")

# set axis limits
pl.xlim(0.0, 5.0)
pl.ylim(0.0, 10.0)

# always has to be at the end
pl.show()

'''


'''
# importing data from a file

import numpy as np
import pylab as pl

# Use numpy to laod data in the file
# "fakedata.txt" unti  a 2-d srray called data
data = np.loadtxt("fakedata.txt")

# plot first column as x and second as y
pl.plot(data[:, 0], data[:,1], 'ro')
pl.xlabel('x')
pl.ylabel('y')
pl.xlim(0.0, 10.)
pl.show()

'''

'''
# HISTOGRAMS

import numpy as np
import pylab as pl

# make an array of random numbers with a gaussian distance
# mean = 5.0
# rms = 3.0 root-mean-squared deviation
# nnumber of points = 1000

data = np.random.normal(5.0,3.0,1000)

pl.hist(data)

pl.xlabel('data')

pl.show()
'''

# CSV file

data = np.loadtxt("diningdirhamsmay.csv", delimeter="")

# computer total
total = sum(data[:,1])

print(total)

# plot data
pl.plot(data[:,0], data[:,1], "g-")

# label data
pl.title("Expenses throughout may")
pl.xlabel("")
pl.ylabel("")

# save
pl.savefig("MayExpenses.png")
pl.savefig("MayExpenses.aps")

pl.show() 
