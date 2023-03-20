# Python_Challenge
## PYBANK
## Step 1: Functions
Created a function to find the sum of a list of values
Created a function to find the max of a list of values and its index
Created a function to find the min of a list of values and its index
## Step 2: Reading in our CSV data
Using os to read in csv as well as csv
Using location and temporary file to be read by the csv reader
CSV reader specifies delimiter and variable that holds contents
Since there is a header, storing that as csv_header
Now we designate the rows in the reader
## Step 3: Analysis
First we want the total number of distinct months, this is just the amount of rows we have

Now looking to separate the profit/loss values into a list
Making sure to convert string values into integers as we will want to do math on them later
Now looking for net total of profit/loss, use the sum function from step 1
Then looking for the changes, and then the average of those changes
Stopping the range one before the full length because we are using i+1 in our loop
Then we use a simple sum over length to find the average change based on list of changes

To find the biggest increase and the month of that increase using my max and index function -- need to add one to the index because the second value in our original index to create the change list was i+1

Then do the same looking for biggest decrease this time using the min and index function from step #1
## Step 4: Results
Now to print the analysis to the terminal using fstrings
And using open in writing mode to type results to a text file as well

