import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

voter_id = []
candidate = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])

    total_votes = len(voter_id)
    print(total_votes)

    unique_candidate = list(dict.fromkeys(candidate))
    print(unique_candidate)
    Khan_count = candidate.count("Khan")
    print(Khan_count)
    Khan_percent = Khan_count / total_votes
    print(Khan_percent)


print("Election Results")
print("-----------------------")
print("Total Votes: " + format(total_votes, ","))    
print("-----------------------")

    



