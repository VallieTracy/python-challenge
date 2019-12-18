print("Financial Analysis")
print("-------------------------------------------------")

import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print(csv_reader)

    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    for row in csv_reader:
       print(row[1])

    #for row in csv_reader:
        #if float(row[1]) >= 1000000:
            #print(row)

def Numbers(number):
    print("Total Months: ")
    
    for numberValue in number:
        print(numberValue)
myList = ["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
Numbers(myList)
    

   




# Read in the CSV file
#with open(banking_csv, "r") as csvfile:

    # Split the data on commas
    #csvreader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    #for row in csvreader:
        #if float(row[1]) >= 10:
            #print(row)



    