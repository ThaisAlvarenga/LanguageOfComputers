'''
NAME: Thais Alvarenga & Badr 
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Data visualization of most used songs on TikTok
DATE: 01/03/2023

'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read csv file
data = pd.read_csv('data.csv') 

# Start with Song col as index , set rotation to 90, and customize marker
songStreamed =data.set_index('Songs').plot(rot=90, colormap='jet', marker='.', markersize=10) 

# Fit all the songs horizontally
songStreamed.set_xticks(np.arange(len(data)))

# write x axis label 
songStreamed.set_xticklabels(data.Songs)

# Set y label
songStreamed.set_ylabel("Streams (in billions)")
# Set x label
songStreamed.set_xlabel("Songs")

# title
plt.title('Most popular songs on TikTok worldwide \n Jan-June 2022 (in billions)', fontstyle='italic')

# Make the text visible (add padding)
plt.tight_layout() 

# show graph
plt.show()

