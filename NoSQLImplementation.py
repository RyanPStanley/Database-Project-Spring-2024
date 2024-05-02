import json 
from decimal import Decimal
import boto3 
import csv

if __name__ == '__main__':

    gameNames = []
    releaseYears = []
    platforms = []
    generations = []
    unitSales = []
    allTimeSales = []
    reviewDates = []
    ratingNumbers = []
    

    with open('dataGame.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            if row[0] != 'GameName':
                gameNames.append(row[0])
                releaseYears.append(row[1])
                platforms.append(row[2])
                generations.append(row[3])

    with open('dataSales.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            if row[0] != 'GameName':
                unitSales.append(row[1])
                allTimeSales.append(row[2])

    with open('dataReviews.csv', mode ='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            if row[0] != 'GameName':
                reviewDates.append(row[1])
                ratingNumbers.append(row[2])
                
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Ryan-Database-Project')
    for i in range(len(gameNames)):
        gameName = gameNames[i]
        year = releaseYears[i]
        platform = platforms[i]
        gen = generations[i]
        unitSalesNum = unitSales[i]
        ATSnum = allTimeSales[i]
        date = reviewDates[i]
        rating = ratingNumbers[i]
        table.put_item(Item={
                        "GameName": gameName,
                        "ReleaseYear": year,
                        "Platform": platform,
                        "Generation": gen,
                        "UnitSales": unitSalesNum,
                        "AllTimeSales": ATSnum,
                        "ReviewDate": date,
                        "Rating": rating,
                    })

