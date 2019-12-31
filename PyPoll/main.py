#import dependencies
import os
import csv

#set path for csv file
csvpath = os.path.join("Resources", "election_data.csv")

#create empty lists where I can store data as I loop through the file
voter_id = []
candidate = []

#open csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    #loop through the rows in csv file
    for row in csvreader:
        #store data into the empty lists created above
        voter_id.append(row[0])
        candidate.append(row[2])

    #total votes cast can be determined by how many voter id's, after looping through the data,
    #are in the voted_id list.  My coding assumes that there are no errors, no multiple voter ids
    total_votes = len(voter_id)
    
    #if I print this, it will tell me all unique candidates
    unique_candidate = list(dict.fromkeys(candidate))
    
    #Numeric info on all candidates
    Khan_count = candidate.count("Khan")
    Khan_percent = (Khan_count / total_votes) * 100
    
    Correy_count = candidate.count("Correy")
    Correy_percent = (Correy_count / total_votes) * 100
    
    Li_count = candidate.count("Li")
    Li_percent = (Li_count / total_votes) * 100
    
    OTooley_count = candidate.count("O'Tooley")
    OTooley_percent = (OTooley_count / total_votes) * 100
    
    #create a function to determin the election winner
    def winner(list):
        return max(set(list), key = list.count)   
        
#print the results
#i made some minor changes to the formatting in order to make it more readable
print("Election Results")
print("-----------------------")
print("Total Votes: " + format(total_votes, ","))    
print("-----------------------")
print("Khan:     " + str(round(Khan_percent, 3)) + "% (" + format(Khan_count, ",") + ")")
print("Correy:   " + str(round(Correy_percent, 3)) + "% (" + format(Correy_count, ",") + ")")
print("Li:       " + str(round(Li_percent, 3)) + "% (" + format(Li_count, ",") + ")")
print("O'Tooley: " + str(round(OTooley_percent, 3)) + "% (" + format(OTooley_count, ",") + ")")
print("-----------------------")
print("Winner: " + winner(candidate))
print("-----------------------")

    



