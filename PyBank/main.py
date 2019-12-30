#import dependencies
import os
import csv

#path to csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#create lists in order to store the data
individual_period = []
profits_and_losses = []
next_pl_amount = []
former_pl_amount = []
pl_change = []
individual_period_adjusted = []


#open the csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #loop through the rows in the csv file
    for row in csvreader:
        individual_period.append(row[0])
        profits_and_losses.append(int(row[1]))

    #summing the appended profits_and_losses list after looping 
    #through all data
    net_profits = sum(profits_and_losses)
    
    #altering the profits_and_losses to align so that
    #we can correctly subtract them 
    next_pl_amount = profits_and_losses[1:]
    former_pl_amount = profits_and_losses[:-1]
        
    #using lists to find Average Change
    pl_change = [next_profit - former_profit for (next_profit, former_profit) in zip(next_pl_amount, former_pl_amount)]
    average_pl_change = round((sum(pl_change) / len(pl_change)), 2)
    
    #need to remove the first individual_period because
    #there is no change during this period (this column has one less row than the first two)
    individual_period_adjusted = individual_period[1:]

    #find the indexes which correspond to the maximum and minimum profits and/or losses
    maximum_profit_index = pl_change.index(max(pl_change))
    minimum_profit_index = pl_change.index(min(pl_change))
    
    #find extreme profits and corresponding periods utilizing the indexes found above
    maximum_profit_period = individual_period_adjusted[maximum_profit_index]
    minimum_profit_period = individual_period_adjusted[minimum_profit_index]
    maximum_profit = pl_change[maximum_profit_index]
    minimum_profit = pl_change[minimum_profit_index]
    

     


#print output
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(len(individual_period)))
print("Total: " + "$" + format(net_profits, ","))
print("Average Change: " + "$" + format(average_pl_change, ","))
print("Greatest Increase in Profits: " + maximum_profit_period + " ($" + format(maximum_profit, ",") + ")")
print("Greatest Decrease in Profits: " + minimum_profit_period + " ($" + format(minimum_profit, ",") + ")")
