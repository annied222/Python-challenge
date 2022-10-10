#Create a Python script that analyzes the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of Profit/Losses over the entire period
#   The changes in Profit/Lossess over the entire period, and the average of the changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (data and amount) over the entire period

import os
import csv 

csvpath=os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    print(csvreader)

    #Header in csv
    csvheader=next(csvreader)

    totalmonths=0

    print('\n')
    print("Financial Analysis")

    print("-" * 25)

    #Total number of months in dataset
    For row in csvreader:
        print(row)
        

    print(f"Total Months:"{totalmonths})