import os
import csv

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Variables
Total_Votes = 0
Candidates = {}
percentage = 0


# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row first (skip this step if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csv_reader:
    

        # Calculate the total number of votes
        Total_Votes += 1

        # Complete list of candidates who received votes
        Candidate = row[2]
        if not Candidate in Candidates:
            Candidates[Candidate] = 0
        Candidates[Candidate] +=1

Max_Votes = 0
Winner = ""
for key in Candidates.keys():
    votes = Candidates[key]
    if votes > Max_Votes:
        Max_Votes = votes 
        Winner = key
Output = []

# The percentage of votes each candidate won
        
# The total number of votes each candidate won
        
# The winner of the election based on popular vote

# Statements to be printed
Output.append("Election Results")
Output.append("-------------------------")
Output.append(f"Total Votes: {Total_Votes}")
Output.append(f"-------------------------")
Output.append(f"Charles Casper Stockham: {round(Candidates['Charles Casper Stockham'] / Total_Votes * 100,3)}% ({Candidates['Charles Casper Stockham']})")
Output.append(f"Diana DeGette: {round(Candidates['Diana DeGette'] / Total_Votes * 100,3)}% ({Candidates['Diana DeGette']})")
Output.append(f"Raymon Anthony Doane: {round(Candidates['Raymon Anthony Doane'] / Total_Votes * 100,3)}% ({Candidates['Raymon Anthony Doane']})")
Output.append(f"-------------------------")
Output.append(f"Winner: {Winner}")
Output.append(f"-------------------------")
with open('PyPoll/analysis/vote_results.txt', 'w') as output_file:
    for line in Output:
        print(line)
        output_file.write(line + "\n")