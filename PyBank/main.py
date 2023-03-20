# Using os to read in csv as well as csv
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#create a function to sum a list of values
def sum0(list):
    sum = 0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

#create a function to find the max of a list of values and its index
def max0(list):
    max = 0
    for i in range(len(list)):
        if list[i]>=max:
            max = list[i]
            max_and_index = [max, i]
    return max_and_index

#create a function to find the min of a list of values and its index
def min0(list):
    min = 0
    for i in range(len(list)):
        if list[i]<=min:
            min = list[i]
            min_and_index = [min, i]
    return min_and_index

#using location and temporary file to be read by the csv reader
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # there is a header, storing that as csv_header
    csv_header = next(csvreader)

    # now for the rows in the reader
    budget_rows = []
    for row in csvreader:
        budget_rows.append(row)

#first we want the total number of distinct months, this is just the amount of rows we have
month_total = len(budget_rows)

#now looking to separate the profit/loss values into a list
profit_loss = []
for i in range(len(budget_rows)):
    #making sure to convert string values into integers as we will want to do math on them later
    int_convert = int(budget_rows[i][1])
    profit_loss.append(int_convert)

#looking for net total of profit/loss
pl_total = sum0(profit_loss)

#now looking for the changes, and then the average of those changes
changes = []
for i in range(len(profit_loss)-1):
    #stopping one before the end because we are using i+1 in our loop
    change = profit_loss[i+1] - profit_loss[i]
    changes.append(change)

#finding the average change based on list of changes
avg_change = sum0(changes)/len(changes)

#now looking for biggest increase
#using my max and index function
max_change = max0(changes)
max_val = max_change[0]
#need to add one to the index because the second value in our original index to create the change list was i+1
max_month = budget_rows[max_change[1]+1][0]

#now looking for biggest decrease
#using my min and index function
min_change = min0(changes)
min_val = min_change[0]
#need to add one to the index because the second value in our original index to create the change list was i+1
min_month = budget_rows[min_change[1]+1][0]

#now to print the analysis to the terminal

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {month_total}' )
print(f'Total: ${pl_total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {max_month} (${max_val})')
print(f'Greatest Decrease in Profits: {min_month} (${min_val})')

#now to print results to a text file as well
#opening the text file in writing mode as f
with open('analysis/results.txt', 'w') as f:
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write(f'Total Months: {month_total}\n' )
    f.write(f'Total: ${pl_total}\n')
    f.write(f'Average Change: ${avg_change}\n')
    f.write(f'Greatest Increase in Profits: {max_month} (${max_val})\n')
    f.write(f'Greatest Decrease in Profits: {min_month} (${min_val})\n')

#result variable tracking:
#total months = month_total
#total = pl_total
#list of profit/loss changes = changes
#average of profit/loss changes = avg_change
#max change = max_val
#max month = max_month
#min change = min_val
#min month = min_month