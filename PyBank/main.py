#import dependencies
import os
import csv

#path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#create lists in order to store the data
individual_periods = []
profits_and_losses = []
next_pl_amount = []
former_pl_amount = []



#open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #loop through the rows in the csv file
    for row in csvreader:
        individual_periods.append(row[0])
        profits_and_losses.append(int(row[1]))

    net_profits = sum(profits_and_losses)
    next_pl_amount = profits_and_losses[1:]
    former_pl_amount = profits_and_losses[:-1]
    
    #using lists to find Average Change
    pl_change = [next_profit - former_profit for (next_profit, former_profit) in zip(next_pl_amount, former_pl_amount)]
    average_pl_change = round((sum(pl_change) / len(pl_change)), 2)
    
    

     


#print output
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(len(individual_periods)))
print("Total: " + "$" + format(net_profits, ","))
print("Average Change: " + "$" + format(average_pl_change, ","))
