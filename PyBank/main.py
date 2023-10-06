import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Variables
Total_Months = 0
Total_PL = 0
Previous_PL = 0
monthly_change = []
avg_change = 0
minimum = {"date": "", "amount":0}
maximum = {"date": "", "amount":0}

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row first (skip this step if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    minimum = None
    maximum = None
    minimumdate = ""
    maximumdate = "" 
    for row_number, row in enumerate(csv_reader):
        print(row)

        # Calculate the total number of months
        Total_Months += 1
        
        # Calculate the net total amount of "Profit/Losses" over the entire period
        Total_PL = Total_PL + int(row[1])

        # Calculate the changes in "Profit/Losses" over entire period and then average of the changes
        current_PL = int(row[1])
        if row_number > 0:
            change = current_PL - Previous_PL
            monthly_change.append(change)

            if (minimum == None) or (change < minimum):
                minimum = change
                minimumdate = row[0]
        
            if (maximum == None) or (change > maximum):
                maximum = change
                maximumdate = row[0]

        Previous_PL = current_PL
if len(monthly_change) > 0:
    avg_change = sum(monthly_change) / len(monthly_change)

# Statements to be printed
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: $ {Total_PL}")
print(f"Average Change: $ {avg_change: .2f}")
print(f"Greatest Increase in Profits: {maximumdate} ({maximum})")
print(f"Greatest Decrease in Profits: {minimumdate} ({minimum}) ")