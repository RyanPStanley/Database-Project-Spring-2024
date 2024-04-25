import matplotlib.pyplot as plt
import numpy as np
import csv
from datetime import datetime

# Create array for x- and y- coordinates
reviewsX = []
reviewsY = []

fig, ax = plt.subplots()
with open('dataReviews.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        if row[0] != 'gameName':
            reviewsY.append(float(row[2]))
            reviewsX.append((row[0])[9:-1])

# Create a line plot
ax.plot(reviewsX, reviewsY, linewidth=5.0)
for tick in ax.xaxis.get_major_ticks()[1::3]:
    tick.set_pad(15)
for tick in ax.xaxis.get_major_ticks()[2::3]:
    tick.set_pad(30)
fig.set_figwidth(30)
fig.set_figheight(8)
ax.set_title("Pokemon Games Review Numbers (out of 10)")
ax.set_facecolor("aliceblue")
plt.show()
