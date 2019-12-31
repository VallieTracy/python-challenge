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

    #total votes cast can be determined by how many voter id's there are
    #my coding assumes that there are no errors, no multiple voter ids
    total_votes = len(voter_id)
    
    #if I print this, it will tell me all unique candidates
    unique_candidate = list(dict.fromkeys(candidate))
    
    #numeric info on all candidates
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
#format changes: comma separators in numbers & aligned the candidate names and vote count
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

#print results to .txt file
file = "election_results.txt"
with open(file, "w") as f:
    print("Election Results", file=f)
    print("-----------------------", file=f)
    print("Total Votes: " + format(total_votes, ","), file=f)    
    print("-----------------------", file=f)
    print("Khan:     " + str(round(Khan_percent, 3)) + "% (" + format(Khan_count, ",") + ")", file=f)
    print("Correy:   " + str(round(Correy_percent, 3)) + "% (" + format(Correy_count, ",") + ")", file=f)
    print("Li:       " + str(round(Li_percent, 3)) + "% (" + format(Li_count, ",") + ")", file=f)
    print("O'Tooley: " + str(round(OTooley_percent, 3)) + "% (" + format(OTooley_count, ",") + ")", file=f)
    print("-----------------------", file=f)
    print("Winner: " + winner(candidate), file=f)
    print("-----------------------", file=f)
    f.close()

    



