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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Updated as per feedback from code review. This is a much cleaner solution.

incoming, answering, ts, duration = range(4)

nums_dict = {}

# everyone who calls is a suspect
for call in calls:
    nums_dict[call[incoming]] = True

# everyone who recieves call is not a suspect.
for call in calls:
    nums_dict[call[answering]] = False

# everyone who sends/recieves text is not a suspect.
for text in texts:
    nums_dict[text[incoming]] = False
    nums_dict[text[answering]] = False


telemarketers = [num for num in nums_dict.keys() if nums_dict[num]]
telemarketers = sorted(telemarketers)

print("These numbers could be telemarketers: ")

print(*telemarketers, sep='\n')