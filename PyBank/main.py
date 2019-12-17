print("Financial Analysis")
print("-------------------------------------------------")

import os
import csv

# Path to collect data from the Resources folder
banking_csv = os.path.join('..', 'Resources', 'budget_data.csv')

with open(banking_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    for row in csv_reader:
        if float(row[1]) >= 1000000:
            print(row)
    

   




# Read in the CSV file
#with open(banking_csv, "r") as csvfile:

    # Split the data on commas
    #csvreader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    #for row in csvreader:
        #if float(row[1]) >= 10:
            #print(row)



    