#Create a Python script that analyzes the records to calculate each of the following values:
#   The total number of months included in the dataset
#   The net total amount of Profit/Losses over the entire period
#   The changes in Profit/Lossess over the entire period, and the average of the changes
#   The greatest increase in profits (date and amount) over the entire period
#   The greatest decrease in profits (data and amount) over the entire period

import os
import csv 

csvpath=os.path.join("Resources","budget_data.csv")
#budget_csv=os.path.join("..","Resources","budget_data.csv"

totalmonths=[]
nettotal=[]
profitlosses=[]
rowcount=0

with open(csvpath) as csvfile:
    
    csvreader=csv.reader(csvfile)
    
    #Header in csv
    csvheader=next(csvreader)
    
    for row in csvreader:
        totalmonths.append(row[0])
        nettotal.append(int(row[1]))
    for i in range(len(totalmonths)-1):
        profitlosses.append(int(nettotal[i+1]-nettotal[i]))

print('\n')
print("Financial Analysis")
print("-"*50)
print(f"Total Months: {len(totalmonths)}")
print(f"Total: ${sum(nettotal)}")
print(f"Average Change: ${int(sum(profitlosses)/(rowcount-1))}")
print(f"Greatest Increase in Profits: {totalmonths[profitlosses.index(max(profitlosses))+1]} (${max(profitlosses)})")
print(f"Greatest Increase in Profits: {totalmonths[profitlosses.index(min(profitlosses))+1]} (${min(profitlosses)})")
print('\n')

outputpath=os.path.join("analysis","budget_analysis.txt")

with open(outputpath,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["-"*50])
    csvwriter.writerow([f"Total Months: {len(totalmonths)}"])
    csvwriter.writerow([f"Total: ${sum(nettotal)}"])
    csvwriter.writerow([f"Average Change: ${int(sum(profitlosses)/(rowcount-1))}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {totalmonths[profitlosses.index(max(profitlosses))+1]} (${max(profitlosses)})"])
    csvwriter.writerow([f"Greatest Increase in Profits: {totalmonths[profitlosses.index(min(profitlosses))+1]} (${min(profitlosses)})"])
    