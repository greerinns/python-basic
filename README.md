# Python Challenge

## PYBANK

### Step 1: Functions
To analyze financial data, we define the following functions:

- A function to find the sum of a list of values.
- A function to find the maximum value of a list of values and its index.
- A function to find the minimum value of a list of values and its index.

### Step 2: Reading in our CSV data
To read in the CSV data, we follow these steps:

- Use the `os` library to manage file paths and the `csv` library to work with CSV files.
- Specify the location and temporary file to be read by the CSV reader.
- Define the CSV reader, specifying the delimiter and the variable that holds the file's contents.
- Since there is a header in the CSV file, we store it as `csv_header`.
- Next, we designate the rows in the reader.

### Step 3: Analysis

#### Months
- First, we calculate the total number of distinct months, which is equal to the number of rows in our list of data.

#### Profit/Loss
- Next, we separate the profit/loss values into their own list.
- We ensure that string values are converted into integers, as we will perform mathematical operations on them later.
- We calculate the net total of profit/loss using the `sum` function defined in Step 1.
- We then calculate the changes in profit/loss over each month and find the average of those changes.
- We stop the range one step before the full length because we use `i+1` in our loop.
- To calculate the average change, we use a simple sum over the length of the list of changes.

#### Max and Min
- We find the biggest increase and the corresponding month using the `max` and `index` functions defined in Step 1. We add one to the index because the second value in our original index (used to create the change list) was `i+1`.
- Similarly, we find the biggest decrease and the corresponding month using the `min` and `index` functions from Step 1.

### Step 4: Results
- We print the analysis results to the terminal using f-strings.
- Additionally, we write the results to a text file by opening the file in writing mode and writing the results.

## PYPOLL

### Step 1: Functions
- We create a function to find the maximum value of a list of values and its index by comparing and replacing previous values.

### Step 2: CSV Reading
- We use the `os` library to manage file paths and the `csv` library to read the CSV file.
- We read in the CSV file, specifying the location and temporary file for the CSV reader.
- The CSV reader specifies the delimiter and the variable that holds the file's contents.
- Since there is a header in the CSV file, we store it as `csv_header`.
- The rows are then read in and stored as a list under `election_rows`.

### Step 3: Analysis

#### Total Votes
- To find the total number of votes, we calculate the length of `election_rows`.

#### Candidate Votes
- To calculate the total votes cast for each candidate, we use a for loop.
- We create blank arrays for candidate name storage and an empty list for vote counts for each candidate.
- For each row, we check if the candidate is in the list of candidates.
- If the candidate is in the list, we add a tally to the list to count the votes based on the index of the candidate name in the first list.
- If the candidate is not in the list, we add the candidate to the list of candidates and then add a 1 to the list counting the votes to start a count for that candidate.

#### Voting Percentages
- To calculate the percentages of votes won, we divide the tally list by `total_votes` and multiply by 100.

#### Winner Determination
- To find the winner index, we find the maximum of the `candidate_count` list using the function built in Step 1.

### Step 4: Results
- We print the results to the terminal using f-strings and print statements.
- Additionally, we print the results to a text file by opening the text file in writing mode as `f`.
