# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of votes each candidate won
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
#. 5. The winner of the election based on popular vote.

import os
import csv

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:

        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

for candidate in candidate_options:

    vote_count = candidate_votes[candidate]
    percentage_of_votes = vote_count/total_votes * 100

    print(f"{candidate_name}: {percentage_of_votes:.1f}% ({vote_count:,})\n")
    
    if vote_count > winning_count and percentage_of_votes > winning_percentage:
        winning_candidate = candidate
        winning_count = vote_count
        winning_percentage = percentage_of_votes

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

with open(file_to_save, "w") as outfile:
    outfile.write("Hello World")
