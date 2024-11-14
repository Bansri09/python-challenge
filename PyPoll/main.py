# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_results.txt")  # Output file path

# Initialize variables to track the election data
totalVotes = 0  # Track the total number of votes cast
votes_per_candidate = {}

# Open the CSV file and process it
with open(file_to_load, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    reader = csv.reader(csvfile, delimiter=',')
 
    # Skip the header row
    header = next(reader)
    
    # Loop through each row of the dataset and process it
    for row in reader:
        # Print a loading indicator (for large datasets)
        #print(". ", end="")
        # Increment the total vote count for each row
        totalVotes += 1
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1   
        
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(totalVotes))
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 
winner = max(votes_per_candidate, key=votes_per_candidate.get)
print(f"Winner: {winner}")

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    f = open(file_to_output, "w")
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write("Total Votes: " + str(totalVotes)+ "\n")
    f.write("-------------------------\n")

for candidate, votes in votes_per_candidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")"+"\n")
  
f.write("-------------------------\n") 
f.write(f"Winner: {winner}"+"\n")


