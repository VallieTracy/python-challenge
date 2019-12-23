import os
import csv

csvfile = os.path.join("Resources", "election_data.csv")



with open(csvfile, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

    



