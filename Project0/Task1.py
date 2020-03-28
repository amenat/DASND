"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""

# transpose to get columns as single list
textsT = list(zip(*texts))
callsT = list(zip(*calls))

nums = set(textsT[0] + textsT[1] + callsT[0] + callsT[1])

print(f"There are {len(nums)} different telephone numbers in the records.")