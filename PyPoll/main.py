import os
import csv 

csvpath=os.path.join("Resources","election_data.csv")

ballotID=[]
candidate=[]
charlie=0
diana=0
raymon=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)
    
    #Header in csv
    csvheader=next(csvreader)

    #Creating lists for the columns
    for row in csvreader:
        ballotID.append(row[0])
        candidate.append(row[2])
    
    for i in range(len(candidate)):
        if candidate[i]=="Charles Casper Stockham":
            charlie=charlie+1
        elif candidate[i]=="Diana DeGette":
            diana=diana+1
        elif candidate[i]=="Raymon Anthony Doane":
            raymon=raymon+1
    
    if charlie>diana and charlie>raymon:
        winner="Charles Casper Stockham"
    elif diana>charlie and diana>raymon:
        winner="Diana DeGette"
    elif raymon>charlie and raymon>diana:
        winner="Raymon Anthony Doane"

print('\n')
print("Election Results")
print("-"*40)
print(f"Total Votes: {len(ballotID)}")
print("-"*40)
print(f"Charles Casper Stokham: {round(((charlie/len(ballotID))*100),3)}% ({charlie})")
print(f"Diana DeGette: {round(((diana/len(ballotID))*100),3)}% ({diana})")
print(f"Raymon Anthony Doane: {round(((raymon/len(ballotID))*100),3)}% ({raymon})")
print("-"*40)
print(f"Winner: {winner}")
print("-"*40)
print('\n')

#Creating a text file to exported
outputpath=os.path.join("analysis","poll_analysis.txt")
#what will be said in the text file
#contains the same as the output above
with open(outputpath,'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-"*40])
    csvwriter.writerow([f"Total Votes: {len(ballotID)}"])
    csvwriter.writerow(["-"*40])
    csvwriter.writerow([f"Charles Casper Stokham: {round(((charlie/len(ballotID))*100),3)}% ({charlie})"])
    csvwriter.writerow([f"Diana DeGette: {round(((diana/len(ballotID))*100),3)}% ({diana})"])
    csvwriter.writerow([f"Raymon Anthony Doane: {round(((raymon/len(ballotID))*100),3)}% ({raymon})"])
    csvwriter.writerow(["-"*40])
    csvwriter.writerow(f"Winner: {winner}")
    csvwriter.writerow(["-"*40])