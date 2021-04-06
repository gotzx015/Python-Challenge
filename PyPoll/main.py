# Insert Modules
import os
import csv

# Store the file path
election_csv = os.path.join("Resources", "election_data.csv")

# Lists to store data
candidate = []

# Open and read csv file
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Loop through all rows in csv file
    for row in csv_reader:

        # Store data in arrays
        candidate.append(row[2])

# Print Data Summary Header
print("Election Results")
print("----------------------------")

# Print number of months
print(f'Total Votes: {len(candidate)}')
print("----------------------------")

# Create empty list to store number of votes for each candidate
# Used filter tool in excel to see only four candidates received votes (Correy, Khan, Li, O'Tooley)
candidate_vote_count = [0, 0, 0, 0]
candidate_name = ["Correy", "Khan", "Li", "O'Tooley"]

# Loop through candidate list and store amount of votes for each candidate
for x in range(0, len(candidate)):
    if candidate[x] == "Correy":
        candidate_vote_count[0] = candidate_vote_count[0] + 1
    
    if candidate[x] == "Khan":
        candidate_vote_count[1] = candidate_vote_count[1] + 1
    
    if candidate[x] == "Li":
        candidate_vote_count[2] = candidate_vote_count[2] + 1

    if candidate[x] == "O'Tooley":
        candidate_vote_count[3] = candidate_vote_count[3] + 1

# Calculate percentage of votes
correy_pct = (candidate_vote_count[0] / len(candidate)) * 100
khan_pct = (candidate_vote_count[1] / len(candidate)) * 100
li_pct = (candidate_vote_count[2] / len(candidate)) * 100
otooley_pct = (candidate_vote_count[3] / len(candidate)) * 100

# Format percentage of votes
correy_pct = "{:.3f}".format(correy_pct)
khan_pct = "{:.3f}".format(khan_pct)
li_pct = "{:.3f}".format(li_pct)
otooley_pct = "{:.3f}".format(otooley_pct)

# Print candidates, percentage of votes, and amount of votes for each candidate
print(f'Khan: {khan_pct}% ({candidate_vote_count[1]})')
print(f'Correy: {correy_pct}% ({candidate_vote_count[0]})')
print(f'Li: {li_pct}% ({candidate_vote_count[2]})')
print(f'O\'Tooley: {otooley_pct}% ({candidate_vote_count[3]})')
print("----------------------------")

# Find largest vote count
largest_vote_count = 0
for x in range(0, 3):
    if candidate_vote_count[x] > largest_vote_count:
        largest_vote_count = candidate_vote_count[x]

# Find candidate associated with largest vote count
for x in range(0, 3):
    if largest_vote_count == candidate_vote_count[0]:
        winner = 0

    if largest_vote_count == candidate_vote_count[1]:
        winner = 1
    
    if largest_vote_count == candidate_vote_count[2]:
        winner = 2
    
    if largest_vote_count == candidate_vote_count[3]:
        winner = 3

# Print winner
print(f'Winner: {candidate_name[winner]}')
print("----------------------------")

# Open and export output to txt file
with open("Analysis/output.txt", "w") as f:

    f.write("Election Results")
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')
    f.write(f'Total Votes: {len(candidate)}')
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')
    f.write(f'Khan: {khan_pct}% ({candidate_vote_count[1]})')
    f.write('\n')
    f.write(f'Correy: {correy_pct}% ({candidate_vote_count[0]})')
    f.write('\n')
    f.write(f'Li: {li_pct}% ({candidate_vote_count[2]})')
    f.write('\n')
    f.write(f'O\'Tooley: {otooley_pct}% ({candidate_vote_count[3]})')
    f.write('\n')
    f.write("----------------------------")
    f.write('\n')
    f.write(f'Winner: {candidate_name[winner]}')
    f.write('\n')
    f.write("----------------------------")