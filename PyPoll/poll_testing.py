import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

votes = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        votes.append(row[0])










    print("Election Results")
    print("-----------------------")
    print("Total Votes: " + str(len(votes)))
    print("-----------------------")

