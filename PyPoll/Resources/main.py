#Read CSV
#import os module
import os
#import module for reading CSV
import csv
folder="Resources"
csvtable="election_data.csv"
csvpath = os.path.join("..", folder, csvtable)
print(csvpath)
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        #print(row)
#find total number of votes
        total_votes_initial = sum(1 for row in csvreader)
        total_votes = (total_votes_initial + 1)
        #print(total_votes)
#find list of candidates
        
col1 = set()

with open(csvtable) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', skipinitialspace=True)  
    for row in csv_reader:
        col1.add(row[2])
        

print(list(col1))

#votes per candidate
#I want to go back and make this so it does it for every candidate automatically, will explore in the future

#Charles Casper Stockham
c1 = "Charles Casper Stockham"
def search_csv1(csvtable, c1):
    count_c1=0
    with open(csvtable) as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            if c1 in row:
                #print(row)
                count_c1+=1
    return count_c1

count_c1=search_csv1(csvpath, c1)
#print(count_c1)

#Diana DeGette
c2 = "Diana DeGette"
def search_csv2(csvtable, c2):
    count_c2=0
    with open(csvtable) as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            if c2 in row:
                #print(row)
                count_c2+=1
    return count_c2

count_c2=search_csv2(csvpath, c2)
# print(count_c2)

#Raymon Anthony Doane
c3 = "Raymon Anthony Doane"
def search_csv3(csvtable, c3):
    count_c3=0
    with open(csvtable) as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            if c3 in row:
                #print(row)
                count_c3+=1
    return count_c3

count_c3=search_csv3(csvpath, c3)
print(count_c3)

#find percentages for each candidate

pct_c1 = (count_c1 / total_votes) * 100
pct_c2 = (count_c2 / total_votes) * 100
pct_c3 = (count_c3 / total_votes) * 100

# print(pct_c1)
# print(pct_c2)
# print(pct_c3)

#determine winner
# if pct_c1 > 50:
#     print("Winner: " + c1)
# elif pct_c2 > 50:
#     print("Winner: " + c2)
# elif pct_c3 > 50:
#     print("Winner: "+ c3)
# else:
#     print("No Winner!")

#print results
print("Election Results"),
print("-------------------------"),
print("Total Votes: " + str(total_votes)),
print("-------------------------"),
print(str(c1) + ": " + str(pct_c1) + "% (" + str(count_c1) +")"),
print(str(c2) + ": " + str(pct_c2) + "% (" + str(count_c2) +")"),
print(str(c3) + ": " + str(pct_c3) + "% (" + str(count_c3) +")"),
print("-------------------------")
if int(pct_c1) > 50:
    print("Winner: " + str(c1))
elif int(pct_c2) > 50:
    print("Winner: " + tr(c2))
elif int(pct_c3) > 50:
    print("Winner: "+ str(c3))
else:
    print("No Winner!"),
print("-------------------------"),