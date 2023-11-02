
import matplotlib.pyplot as plt
import pandas as pd

# read csv file using pandas
data = pd.read_csv("total_cases.csv")


# convert column "World" into a list
world = list(data.World)

# convert column "Index" into a list which represents the number of days from day 0 to last day
index = list(data.index)

# automaticall, the program will assumee that the data is a float

# convert column "italy" into a list

italy = list(data["Italy"])

SouthKorea= list(data["South Korea"])

# plot series for cases worldwide
plt.plot(index,world, "m", label = "World")

# plot series for italy
plt.plot(index,italy, "g", label = "Italy")


# plot series for South Korea
plt.plot(index,SouthKorea, "b", label = "SouthKorea")

plt.ylabel("Total of reported Covid-19 cases")

plt.xlabel("Day")

plt.legend()

plt.show()
