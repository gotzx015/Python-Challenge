# Insert Modules
import os
import csv

# Store the file path
budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
date = []
profit = []

# Open and read csv file
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Loop through all rows in csv file
    for row in csv_reader:

        # Store data in arrays
        date.append(row[0])

        profit.append(int(row[1]))


# Print Data Summary Header
print("Financial Analysis")
print("----------------------------")

# Print number of months
print(f'Total Months: {len(date)}')

# Find net total of profit and print
sum_of_profit = sum(profit)
print(f'Total: ${sum_of_profit}')

# List to store change in profit data
profit_change = []

# Loop through profit list and store the change in profit in profit change list
for x in range(1, len(profit)):
    profit_change.append(profit[x] - profit[x-1])
    
# Find average of profit change list and print
sum_of_profit_change = sum(profit_change)
average_of_profit_change = sum_of_profit_change / len(profit_change)
format_average = "{:.2f}".format(average_of_profit_change)
print(f'Average Change: ${format_average}')

# Set intial values to 0 for a comparison
greatest_profit_change = 0
smallest_profit_change = 0

# Loop through profit change list
for x in range(0, len(profit_change)):

    # Sets new greatest profit change and store associated date
    if profit_change[x] > greatest_profit_change:
        greatest_profit_change = profit_change[x]
        greatest_profit_change_date = date[x + 1]

    # Sets new smallest profit change and store associated date
    if profit_change[x] < smallest_profit_change:
        smallest_profit_change = profit_change[x]
        smallest_profit_change_date = date[x + 1]

# Print greatest and smallest profit change and associated date
print(f'Greatest Increase in Profits: {greatest_profit_change_date}  (${greatest_profit_change})')
print(f'Greatest Decrease in Profits: {smallest_profit_change_date}  (${smallest_profit_change})')

# Open and export output to txt file
with open("Analysis/output.txt", "w") as f:

    f.write("Financial Analysis")
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')
    f.write(f'Total Months: {len(date)}')
    f.write('\n')
    f.write(f'Total: ${sum_of_profit}')
    f.write('\n')
    f.write(f'Average Change: ${format_average}')
    f.write('\n')
    f.write(f'Greatest Increase in Profits: {greatest_profit_change_date}  (${greatest_profit_change})')
    f.write('\n')
    f.write(f'Greatest Decrease in Profits: {smallest_profit_change_date}  (${smallest_profit_change})')