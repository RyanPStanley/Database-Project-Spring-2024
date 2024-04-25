import matplotlib.pyplot as plt
import numpy as np
import csv

# Create array for x- and y- coordinates
x_axis = []
salesY = []
unitsY = []

fig, ax = plt.subplots(2)
with open('dataSales.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        if row[0] != 'GameName':
            unitsY.append(float((row[1])[1:]))
            salesY.append(float((row[2])[1:]))
            x_axis.append((row[0])[9:-1])

# Create a line plot


ax[0].bar(x_axis, unitsY, color='indianred')
ax[0].set_xticklabels([])
fig.set_figwidth(30)
fig.set_figheight(10)
ax[0].set_title("Unit Sales")
ax[0].set_yticklabels(['0', '5M', '10M', '15M', '20M', '25M', '30M'])
ax[0].set_ylabel("Copies sold")
ax[0].set_facecolor("mistyrose")

ax[1].bar(x_axis, salesY, color='limegreen')
for tick in ax[1].xaxis.get_major_ticks()[1::3]:
    tick.set_pad(15)
for tick in ax[1].xaxis.get_major_ticks()[2::3]:
    tick.set_pad(30)
fig.set_figwidth(30)
fig.set_figheight(10)
ax[1].set_title("All Time Sales")
ax[1].set_yticklabels(['0', '$200M', '$400M', '$600M', '$800M', '$1B', '$1.2B', '$1.4B', '$1.6B'])
ax[1].set_ylabel("Total Money Made (release to present)")
ax[1].set_facecolor("honeydew")
fig.suptitle('Pokemon Games\' Sales Data')
plt.show()

