# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = []
total_net = []
# Add more variables to track other necessary financial data
monthly_profit_change = []

# Open and read the csv
with open(file_to_load, newline="", encoding="utf-8") as financial_data:
    reader = csv.reader(financial_data, delimiter=",")

    # Skip the header row
    header = next(reader)
    
    # Iterate through each row in the CSV
    for row in reader:
        # Append month and profit to respective lists
        total_months.append(row[0])
        total_net.append(int(row[1]))
    
    # Calculate monthly profit changes
    for i in range(len(total_net) - 1):
        monthly_profit_change.append(total_net[i + 1] - total_net[i])

# Calculate max and min profit changes
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Find corresponding months for max and min profit changes
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print financial analysis to console
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_net)}")
print(f"Average Change: ${round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase_value})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease_value})")

# Write financial analysis to output file
with open(file_to_output, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_net)}\n")
    file.write(f"Average Change: ${round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase_value})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease_value})\n")
