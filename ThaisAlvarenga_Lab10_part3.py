'''
NAME: Thais Alvarenga & Badr 
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: 
DATE: 01/03/2023

'''
import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("data.csv")

plt.plot(data)

plt.show()
