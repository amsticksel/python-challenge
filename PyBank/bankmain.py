# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
#make the txt file where we will print the results
f = open("pybank-results.txt", "w")
#set containers for the total, months, and change which we will use later
total = []
months = []
change = []

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

#add the months to a container
#add the revenue rows to the container and sum them up
    for row in csvreader:
        months.append(row[0])
#total earn/loss float so it is a number
        total.append(float(row[1]))
#print it out
    print("-----Financial Analysis-----")
    print("----------------------------")
    #caclulate the number of months in the months container with len
    print(f"Total Months:      {len(months)} months")
    #calculate the sum in total
    print(f"Total Sum:         ${round(sum(total))}")
#print to our file
    f.write("-----Financial Analysis-----\n")
    f.write("----------------------------\n")
    f.write(f"Total Months:      {len(months)} months\n")
    f.write(f"Total Sum:         ${round(sum(total))}\n")

#do a loop through the totals amount
    for x in range(1, len(total)):
    #calculate the change between the total and the total in the iteration before it which we will add to the change container
        change.append(total[x] - total[x-1])
#the average change is the sum of all the changes divided by the number of changes there were
        avgchange = sum(change)/len(change)
#from the change list find the largest number
        maxchange = max(change)
#from the change list find smallest number
        minchange = min(change)
#to find date compare dates list to the max number in the change list
        maxdate = str(months[change.index(max(change))])
#to find date compare date to min
        mindate = str(months[change.index(min(change))])
#now we will print it out
#we set the format for currency to have 2 decimals and a dollar sign
    txt = "${:.2f}"
    print(f"Average Change:    {txt.format(avgchange)}")
    print(f"Greatest Increase: {txt.format(maxchange)} on {maxdate}")
    print(f"Greatest Decrease: {txt.format(minchange)} on {mindate}")
    f.write(f"Average Change:    {txt.format(avgchange)}\n")
    f.write(f"Greatest Increase: {txt.format(maxchange)} on {maxdate}\n")
    f.write(f"Greatest Decrease: {txt.format(minchange)} on {mindate}\n")
