import matplotlib.pyplot as plt
import numpy as np
import csv

# Create array for x- and y- coordinates
years = []
salesY = []
unitsY = []
gameNames = []

fig, (ax1, ax2) = plt.subplots(1, 2)
with open('dataSales.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        if row[0] != 'GameName':
            unitsY.append(float((row[1])[1:]))
            salesY.append(float((row[2])[1:]))
            gameNames.append((row[0])[9:-1])

# Create a line plot

with open('dataGame.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for row in csvFile:
        if row[0] != 'GameName':
            years.append(row[1])

hbar1 = ax1.barh(gameNames, unitsY, color='salmon')
fig.set_figwidth(40)
fig.set_figheight(10)
ax1.set_title("Unit Sales")
ax1.set_xticklabels(['0', '5M', '10M', '15M', '20M', '25M', '30M'])
ax1.set_yticklabels(years)
ax1.set_xlabel("Copies sold")
ax1.invert_yaxis()
ax1.set_facecolor("mistyrose")
ax1.bar_label(hbar1, labels = gameNames, fontsize='9', label_type = 'center')
hbar2 = ax2.barh(gameNames, salesY, color='springgreen')
fig.set_figwidth(40)
fig.set_figheight(10)
ax2.set_title("All Time Sales")
ax2.set_xticklabels(['0', '$200M', '$400M', '$600M', '$800M', '$1B', '$1.2B', '$1.4B', '$1.6B'])
ax2.set_xlabel("Total Money Made (release to present)")
ax2.set_yticklabels(years)
ax2.set_facecolor("honeydew")
ax2.invert_yaxis()
ax2.bar_label(hbar2, labels = gameNames, fontsize='9', label_type = 'center')
fig.suptitle('Pokemon Games\' Sales Data')
plt.show()

