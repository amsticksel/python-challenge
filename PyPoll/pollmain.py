# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
#make the txt file where we will print the results
f = open("pypoll-results.txt", "w")
#set containers for the votes, candidates, and set totals for the candidates
votes = []
candidate = ["Khan", "Correy", "Li","O'Tooley"]
totalk = 0
totalc = 0
totall = 0
totalo = 0
totalvotes = []
#counting when they vote for each candidate
vkhan = "Khan"
vcorrey = "Correy"
vli = "Li"
votooley = "O'Tooley"
# Open the CSV

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

#add the votes to the container
    for row in csvreader:
        votes.append(row[0])
#add the candidate choice to the container
        candidate.append(row[2])
#print it out
    print("-----Election  Analysis-----")
    print("----------------------------")
    print(f"Votes Cast:      {len(votes)} votes")

    f.write("-----Election  Analysis-----\n")
    f.write("----------------------------\n")
    f.write(f"Votes Cast:      {len(votes)} votes\n")

#do a loop through the candidate container to see who was voted for and add that to their total votes
    for x in candidate:
        if x == vkhan:
            totalk += 1
            totalvotes.append(totalk)
        elif x == vcorrey:
            totalc += 1
            totalvotes.append(totalc)
        elif x == vli:
            totall +=1
            totalvotes.append(totall)
        else:
            totalo +=1
            totalvotes.append(totalo)
#now print the results and round it to the nearest .00%
#Also printing to a txt file we created at the beginning
    txt = "{:.2f}%"
    print(f"Votes for Khan:     {totalk} --- {txt.format(totalk/len(votes)*100)}")
    f.write(f"Votes for Khan:     {totalk} --- {txt.format(totalk/len(votes)*100)}\n")
    print(f"Votes for Correy:   {totalc} --- {txt.format(totalc/len(votes)*100)}")
    f.write(f"Votes for Correy:   {totalc} --- {txt.format(totalc/len(votes)*100)}\n")
    print(f"Votes for Li:       {totall} --- {txt.format(totall/len(votes)*100)}")
    f.write(f"Votes for Li:       {totall} --- {txt.format(totall/len(votes)*100)}\n")
    print(f"Votes for O'Tooley: {totalo} --- {txt.format(totalo/len(votes)*100)}")
    f.write(f"Votes for O'Tooley: {totalo} --- {txt.format(totalo/len(votes)*100)}\n")

#we are finding the winner by calculating the highest number in totalvotes and matching it to the string of candidate
    winvotes = max(totalvotes)
    winner = str(candidate[totalvotes.index(max(totalvotes))])
#printing it to terminal and to txt file
    print(f"Winner: {winner} with {winvotes} total votes!")
    f.write(f"Winner: {winner} with {winvotes} votes!\n")
