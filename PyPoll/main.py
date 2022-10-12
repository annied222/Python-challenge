import os
import csv 

csvpath=os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    
    #Header in csv
    csvheader=next(csvreader)
    
print('\n')
print("Electuion Results")
print("-"*50)
print(f"Total Votes: ")
