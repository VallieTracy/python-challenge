import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

voter_id = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])

    total_votes = len(voter_id)
    print(total_votes)


print("Election Results")
print("-----------------------")
print("Total Votes: " + format(total_votes, ","))    
print("-----------------------")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    



