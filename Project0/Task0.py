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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# column definition
incoming, answering, ts, duration = range(4)

first_txt = texts[0]
last_call = calls[-1]

print(f"First record of texts, {first_txt[incoming]} texts {first_txt[answering]} at time {first_txt[ts]}")
print(f"Last record of calls, {last_call[incoming]} calls {last_call[answering]} at time {last_call[ts]}, lasting {last_call[duration]} seconds")

'''
Big-Oh analysis:

Since we have only used list indexing in this which is O(1); runtime of this whole program is O(1).

'''