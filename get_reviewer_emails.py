# Script for generating a list of grader email addresses

# Download CSV of graders from grading tool rails admin
# Name this CSV 'names.csv'; output will be in 'names2.csv'

import csv

graders = []
emails = []
with open ('names.csv', 'r') as csvfile:
    csv_rows = csv.reader(csvfile)
    
    # Assumes that reviewer's email is in the second column
    for row in csv_rows:
        if row[1] not in emails:
            graders.append(row)
            emails.append(row[1])

with open ('names2.csv', 'w') as writefile:
    written_file = csv.writer(writefile)
    for grader in graders:
        written_file.writerow(grader)


