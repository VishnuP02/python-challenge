import os
import csv

budget_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Variables
Total_Months = []
Total_Profit = []
Monthly_Profit_Change = []

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read header row first (skip this step if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read each column of data after the header
    for row in csv_reader:
        
        # Append number of months and profit
        Total_Months.append(row[0])
        Total_Profit.append(int(row[1]))

    # Calculate monthly change through iteration of profit
    for i in range(len(Total_Profit)-1):

        # Calculate difference
        Monthly_Profit_Change.append(Total_Profit[i+1]-Total_Profit[i])

# Max and Min of monthly profit change
max_increase_value = max(Monthly_Profit_Change)
max_decrease_value = min(Monthly_Profit_Change)

max_increase_month = Monthly_Profit_Change.index(max(Monthly_Profit_Change)) + 1
max_decrease_month = Monthly_Profit_Change.index(min(Monthly_Profit_Change)) + 1

# Statements to be printed
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: $ {sum(Total_Profit)}")
print(f"Average Change: ${round(sum(Monthly_Profit_Change)/len(Monthly_Profit_Change),2)}")
print(f"Greatest Increase in Profits: {Total_Months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {Total_Months[max_decrease_month]} (${(str(max_decrease_value))})")