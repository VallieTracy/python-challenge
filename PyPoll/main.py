import os
import csv

csvfile = os.path.join("Resources", "election_data.csv")

with open(csvfile, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)

output = (
    f"Election Results\n"
    f"--------------------\n"
    f"Total Votes\n"
    f"--------------------\n")

print(output)

