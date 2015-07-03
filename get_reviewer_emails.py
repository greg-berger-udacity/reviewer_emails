# Script for generating a CSV of unique, non-Udacity grader email addresses

# Download CSV of graders from grading tool rails admin
# Name this CSV 'names.csv'; output will be in 'names2.csv'

import csv

emails = {}
with open ('names.csv', 'r') as csvfile:
   csv_rows = csv.reader(csvfile)
   
   # Assumes that email address is in the second column
   # Filters out @udacity.com emails
   # Saves entire row as value
   for row in csv_rows:
        if '@udacity.com' not in row[1]:
            emails[row[1]] = row

# Writes rows out to csv using csv.writer
with open ('names2.csv', 'w') as writefile:
    written_file = csv.writer(writefile)
    for value in emails.values():
        written_file.writerow(value)
