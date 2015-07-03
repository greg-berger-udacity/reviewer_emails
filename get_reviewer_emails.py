# Script for generating a list of grader email addresses and first names

# Download CSV of graders from grading tool rails admin
# Name this CSV 'names.csv'; output will be in 'names2.csv'

import csv

emails = {}
with open ('names.csv', 'r') as csvfile:
   csv_rows = csv.reader(csvfile)
   
   # Assumes that name is in the first column
   # and email address is in the second column
   for row in csv_rows:
       emails[row[1]] = row[0]

# Writes name and email addresses out into csv
with open ('names2.csv', 'w') as writefile:
   for (key, value) in emails.iteritems():
       writefile.write(value + ',' + key + '\r')