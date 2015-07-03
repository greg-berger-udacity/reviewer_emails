# reviewer_emails

This script reads a CSV of Udacity project reviewer data and generates a spreadsheet that can be used to email all project reviewers, or reviewers for specific projects only, via SendGrid.

### Defaults (can be changed while running the script)
* Only iOS ND reviewers are in the spreadsheet
* Udacity email addresses are not included
* Waitlisted reviewers are not included.

### How to use this script
* Download a CSV of all project reviewers
* Rename the CSV 'all_reviewers.csv' and move it to the same directory as the script
* Modify the script as needed for your desired custom output
* Run the script. The output will be in 'output.csv'.

### Step 1: Downloading the CSV from reviews-api
* Go to https://review-api.udacity.com/admin/project_grader
* Click on 'Export found Project graders'
* In the tab that opens, deselect 'Select All Fields'
* Under 'Fields from project graders', select 'Waitlisted at'
* Under 'Fields from associated grader', select 'Name' and 'Email'
* Under 'Fields from associated project', select 'ID'
* At the bottom of the page, click on 'Export to CSV' to initiate the download.

Note: You can select any or all the fields, but choosing the ones mentioned above will require the least amount of massaging of the source code for your desired output. 

### Step 2: Renaming and moving the CSV
* Locate the downloaded CSV.
* Rename it 'all_reviewers.csv' (required for the script to run properly)
* Move it to the same directory as the 'get\_reviewer\_emails.py' script

### Step 3: Modifying the defaults for custom output
* Open the source code file 'get\_reviewer\_emails.py'
* If your downloaded CSV contains additional fields than the ones listed in Step 1, check the row subscripts on lines 19–23 of the script to make sure that they accurately reflect the columns in the downloaded CSV: Line 19 should have the column with the waitlisted date; Lines 20 and 23, the one with the email address; lines 21 and 22, the one with the Project ID
* On line 22 the default `in range(19, 24)` will provide iOS ND reviewers. Type in a list of the project IDs for the projects whose reviewers you wish to email. E.g., if you want to email just the Spotify Streamer and Popular Movies reviewers, replace `in range(19, 24)` with `in [59, 60, 66, 67]`
* If you want to retain reviewers with an @udacity.com address, delete line 20
* If you want to retain waitlisted reviewers, remove `row[0] == ' - '` from the conditional
* Save your changes and close the source code file. 

### Step 4: Running the script and getting the output
* At the command line, `cd` to the directory that has the 'get\_reviewer\_email.py' script
* Type `python get_reviewer_email.py`
* The script will run and generate a list of unique reviewers for the projects specified.
* The output will be in 'output.csv'. This can be used in SendGrid.

### Known Issues
* No error checking. The script will crash if the CSV has any errors, or if the above instructions are not followed exactly
* Modifications being needed to the source code is undesirable
* The output file has a useless column for Project ID. Since reviewers typically can review multiple projects, the column has just one of those projects. 

### Support, bug reports, feature requests, etc
Email surajit@udacity.com or hit him up in the Udacious office.