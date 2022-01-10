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

with open(file_to_load, "r") as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        pass

with open(file_to_save, "w") as outfile:
    outfile.write("Hello World")
