# Script for generating a CSV of unique Udacity reviewer email addresses

# Download CSV of reviewers from review rails admin
# Name this CSV 'all_reviewers.csv'; output will be in 'output.csv'

import csv

reviewers = {}
with open ('all_reviewers.csv', 'r') as csvfile:
    csv_rows = csv.reader(csvfile)
    
    # Skips header row
    csv_rows.next()
    
    # Assumes that email address is in the second column
    # Filters out @udacity.com emails
    # Filters out waitlisted reviewers
    # Skips reviewers with no project listed
    # Checks for iOS projects only
    # Saves entire row as value
    for row in csv_rows:
        if row[0] == ' - ' \
        and '@udacity.com' not in row[2] \
        and row[3] \
        and int(row[3]) in [19, 20, 21, 22, 23, 78]:
            reviewers[row[2]] = row

# Writes rows out to csv using csv.writer
with open ('output.csv', 'w') as writefile:
    written_file = csv.writer(writefile)
    for value in reviewers.values():
        written_file.writerow(value)
