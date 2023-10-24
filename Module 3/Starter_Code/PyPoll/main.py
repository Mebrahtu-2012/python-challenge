#imprt the os module
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

counter = 0
candidates = {
        "Charles Casper Stockham": 0,
        "Diana DeGette": 0,
        "Raymon Anthony Doane": 0
        }

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    for row in csvreader :
        votes = row[2]
        counter = counter + 1
        if votes == "Charles Casper Stockham":
            candidates["Charles Casper Stockham"] = candidates["Charles Casper Stockham"] + 1
        elif votes == "Diana DeGette":
            candidates["Diana DeGette"] = candidates["Diana DeGette"] +1
        else:
            candidates["Raymon Anthony Doane"] = candidates["Raymon Anthony Doane"] +1

Charles_vote_percentage = (candidates["Charles Casper Stockham"] / counter) * 100
Diana_vote_percentage = (candidates["Diana DeGette"] / counter) * 100
Raymon_vote_percentage = (candidates["Raymon Anthony Doane"] / counter) * 100

formatted_charles = "{:.3f}".format(Charles_vote_percentage)
formatted_diana = "{:.3f}".format(Diana_vote_percentage)
formatted_raymon = "{:.3f}".format(Raymon_vote_percentage)

# found max with this function https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-80.php
winner = max(candidates, key = candidates.get)

# Print the results
print("Election Results")
print("------------------------")
print(f"Total Votes: {str(counter)}")
print("------------------------")
print(f'Charles Casper Stockham: {formatted_charles} % ({candidates["Charles Casper Stockham"]})' )
print(f'Diana DeGette: {formatted_diana} % ({candidates["Diana DeGette"]})' )
print(f'Raymon Anthony Doane: {formatted_raymon} % ({candidates["Raymon Anthony Doane"]})' )
print("------------------------")
print("Winner: winner")
print("------------------------")

#export a text file: https://www.pythontutorial.net/python-basics/python-write-text-file/
file = open("output.txt", "w")
file.write("Election Results" + "\n")
file.write("------------------------" + "\n")
file.write(f"Total Votes: {str(counter)}" + "\n")
file.write("------------------------" + "\n")
file.write(f'Charles Casper Stockham: {formatted_charles} % ({candidates["Charles Casper Stockham"]})' + "\n")
file.write(f'Diana DeGette: {formatted_diana} % ({candidates["Diana DeGette"]})' + "\n")
file.write(f'Raymon Anthony Doane: {formatted_raymon} % ({candidates["Raymon Anthony Doane"]})' + "\n")
file.write("------------------------" + "\n")
file.write("Winner: winner" + "\n")
file.write("------------------------" + "\n")