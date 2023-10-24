import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Variables
month = []
profit_loss = []
change_profit_loss = []

# Open CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        month.append(row[0])
        profit_loss.append(int(row[1]))

# Calculate the total number of months and net total profit/loss
total_month = len(month)
net_total = sum(profit_loss)

# Calculate the changes in profit/loss and populate the change_profit_loss list
for i in range(1, len(profit_loss)):
    change_profit_loss.append(profit_loss[i] - profit_loss[i - 1])

# Calculate the average change in profit/loss
average_change = sum(change_profit_loss) / len(change_profit_loss)

# Find the greatest increase and decrease in profit/loss
increase = max(change_profit_loss)
decrease = min(change_profit_loss)

# Find the corresponding months for the increase and decrease
increase_month = month[change_profit_loss.index(increase) + 1]
decrease_month = month[change_profit_loss.index(decrease) + 1]

# Print the results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${decrease})")






