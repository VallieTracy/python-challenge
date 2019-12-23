#Import dependencies
import os 
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

#Variables to keep track of various data
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []


with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #print(csv_reader)

    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    for row in csv_reader:
       
       total_months = total_months + 1

       revenue_change = int(row["Profit/Losses"]) - prev_revenue
       prev_revenue = int(row["Profit/Losses"])
       revenue_change_list = revenue_change_list + [revenue_change]
       month_of_change = month_of_change + [row["Date"]]
       
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Average Revenue Change: ${revenue_avg}\n")

print(output)

    #for row in csv_reader:
        #if float(row[1]) >= 1000000:
            #print(row)

#def Numbers(number):
    #print("Total Months: ")
    
    #for numberValue in number:
        #print(numberValue)
#myList = ["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"]
#Numbers(myList)







   




# Read in the CSV file
#with open(banking_csv, "r") as csvfile:

    # Split the data on commas
    #csvreader = csv.reader(csvfile, delimiter=',')

    #header = next(csvreader)

    #for row in csvreader:
        #if float(row[1]) >= 10:
            #print(row)



    