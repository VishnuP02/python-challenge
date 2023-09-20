import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row first (skip this step if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read each row of data after the header
    for row in csv_file:
        print()

# Variables
Total_Months = []
Net_Total = []
Average_Change = []
Greatest_Increase = []
Greatest_Decrease = []

# Calculate total number of months


# Calculate net total amount of "Profit/Losses"


# Calculate the Profit/Losses change over entire period
# Average the changes



# Greatest Increase in Profits (Date and Amt.)


# Greatest Decrease in Profits (Date and Amt.)


# Statement to be printed
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: ")