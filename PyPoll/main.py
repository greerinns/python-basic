# Using os to read in csv as well as csv
import os
import csv

#create a function to find the max of a list of values and its index
def max0(list):
    max = 0
    for i in range(len(list)):
        if list[i]>=max:
            max = list[i]
            max_and_index = [max, i]
    return max_and_index

#csv now reading in 
csvpath = os.path.join('Resources', 'election_data.csv')
#using location and temporary file to be read by the csv reader
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # there is a header, storing that as csv_header
    csv_header = next(csvreader)

    # now for the rows in the reader
    election_rows = []
    for row in csvreader:
        election_rows.append(row)
# The CSV has been read in, and values have been stored as a lits of rows in election_rows

# The total amount of votes would be the number of rows, therefore the length of election_rows
total_votes = len(election_rows)

#The total votes cast for each candidate

unique_candidates = []
candidate_count = []
#Make blank arrays for candidate name storage and vote counts for each candidate
for i in range(len(election_rows)):
    if election_rows[i][2] in unique_candidates:
        candidate_index = unique_candidates.index(election_rows[i][2])
        candidate_count[candidate_index] = candidate_count[candidate_index] + 1
    # checking if the candidate is in the list of candidates
    # if it is in the list, adding a tally to the list counting the votes based on indices
    else:
        unique_candidates.append(election_rows[i][2])
        candidate_count.append(1)
    # if the candidate is not in the list, we add it to the list of candidates
    # then we add a 1 to the list counting the votes to start a count for that candidate

#to get percentages of votes won, we divide our tally list by total_votes and multiply by 100
candidate_percents = [(x/total_votes)*100 for x in candidate_count ]

#to find the winner index we find the max of the candidate_count list using the function built above and grab the index value
winner_index = max0(candidate_count)[1]
winner_name = unique_candidates[winner_index]

#now to print the analysis to the terminal

print('Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}' )
print('----------------------------')
print(f'{unique_candidates[0]}: {candidate_percents[0]}% ({candidate_count[0]})')
print(f'{unique_candidates[1]}: {candidate_percents[1]}% ({candidate_count[1]})')
print(f'{unique_candidates[2]}: {candidate_percents[2]}% ({candidate_count[2]})')
print('----------------------------')
print(f'Winner: {winner_name}')
print('----------------------------')

#now to print results to a text file as well
#opening the text file in writing mode as f
with open('analysis/results.txt', 'w') as f:
    f.write('Election Results\n')
    f.write('----------------------------\n')
    f.write(f'Total Votes: {total_votes}\n' )
    f.write('----------------------------\n')
    f.write(f'{unique_candidates[0]}: {candidate_percents[0]}% ({candidate_count[0]})\n')
    f.write(f'{unique_candidates[1]}: {candidate_percents[1]}% ({candidate_count[1]})\n')
    f.write(f'{unique_candidates[2]}: {candidate_percents[2]}% ({candidate_count[2]})\n')
    f.write('----------------------------\n')
    f.write(f'Winner: {winner_name}\n')
    f.write('----------------------------')



#variable storage:
#total votes cast = total_votes
#list of unique candidates = unique_candidates
#list containing candidate votes in the same order as the unique candidate list = candidate_count
#candidate percentage of votes = candidate_percents
#winner name = winner_name









