#import dependencies
import os
import csv

#path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#create lists in order to store the data
individual_periods = []

#open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #loop through the rows in the csv file
    for row in csvreader:
        individual_periods.append(row[0])


#print output
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(len(individual_periods)))
