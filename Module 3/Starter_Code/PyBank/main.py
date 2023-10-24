#imprt the os module
import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

#variables
month = []
profit_loss = []

change_profit_loss = []
                      
  #open CSV file                     
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader:
       month.append((row[0]))
       profit_loss.append(int(row[1]))
       total_month = len(month)
       # found sum with this link https://www.w3schools.com/python/ref_func_sum.asp
       net_total = sum(profit_loss)

#calculating the change for profit/loss with the average change
    for i in range(1, len(profit_loss)):
        change_profit_loss.append(profit_loss[i]- (profit_loss[i-1]))
average_change = sum(change_profit_loss) / len(change_profit_loss)

#calculating the greateest increase and decrease
increase = max(change_profit_loss)
decrease = min(change_profit_loss)
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

#export a text file: https://www.pythontutorial.net/python-basics/python-write-text-file/
file = open("output.txt", "w")
file.write("Financial Analysis" + "\n")
file.write(".........................." + "\n")
file.write(f"Total Months: {total_month}" + "\n")
file.write(f"Total: ${net_total}" + "\n")
file.write(f"Average Change: ${average_change:.2f}" + "\n")
file.write(f"Greatest Increase in Profits: {increase_month} (${increase})" + "\n")
file.write((f"Greatest Decrease in Profits: {decrease_month} (${decrease})") + "\n")

