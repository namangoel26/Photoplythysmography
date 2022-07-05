# First let’s download the dataset and plot the signal, just to get a feel for the data and start finding ways of meaningfully analysing it. I use pandas for most of my data tasks, and matplotlib for most plotting needs.

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("data.csv") #Read data from CSV datafile

plt.title("Heart Rate Signal") #The title of our plot
plt.plot(dataset.hart) #Draw the plot object
plt.show() #Display the plot

#Detecting the first peaks
# The first step is to find the position of all the R-peaks. To do this we need to determine Regions of Interest (ROI’s), namely for each R-peak in the signal. After we have these, we need to determine their maxima.Most of this code will also be re-written to C for use on an embedded ARM chip, so we need to keep it simple and efficient.we’ll use the position of the highest point in the ROI as the position of the beat.

# Now to work: first separate the different peaks from one another. For this we draw a moving average, mark ROI’s where the heart rate signal lies above the moving average, and finally find the highest point in each ROI as such:


