"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

# column definition
incoming, answering, ts, duration = range(4)

callsT = list(zip(*calls))
nums = set(callsT[incoming] + callsT[answering])

# initialize dictionary with 0 duration for all phone numbers
time_spent = {num:0 for num in nums}

for call in calls:
    time_spent[call[incoming]] += int(call[duration])
    time_spent[call[answering]] += int(call[duration])

max_caller = max(time_spent, key=lambda x: time_spent[x])

print(f'{max_caller} spent the longest time, {time_spent[max_caller]} seconds, on the phone during September 2016.')