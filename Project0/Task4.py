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

incoming, answering, ts, duration = range(4)

callsT = list(zip(*calls))
textsT = list(zip(*texts))

numbers = set(callsT[incoming] + callsT[answering] + textsT[incoming] + textsT[answering])

# initialize
count_og = {num:0 for num in numbers}
count_ic = {num:0 for num in numbers}
sends_text = {num:0 for num in numbers}


# I can convert a caller to a class but that will make searching very bad compared to doing just hashing in dict.

for call in calls:
    count_og[call[0]] += 1
    count_ic[call[1]] += 1

for text in texts:
    sends_text[text[0]] += 1

telemarketers = set()

for num in numbers:
    if count_og[num] > 0 and count_ic[num] == 0 and sends_text[num] == 0 and num[:3] != '140':
        telemarketers.add(num)

print("These numbers could be telemarketers: ")

telemarketers = sorted(list(telemarketers))

for num in telemarketers:
    print(num)

