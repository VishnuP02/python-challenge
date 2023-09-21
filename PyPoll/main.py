import os
import csv

election_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row first (skip this step if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_file:
        print()


# Statements to be printed
print("Election Results")
print("-------------------------")
print(f"Total Votes: ")
print(f"-------------------------")
print(f"Charles Casper Stockham: ")
print(f"Diana DeGette: ")
print(f"Raymon Anthony Doane: ")
print(f"-------------------------")
print(f"Winner: ")
print(f"-------------------------")