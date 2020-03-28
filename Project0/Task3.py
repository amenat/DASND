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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

blr_calls = [call for call in calls if call[0][:5] == '(080)']

blr_dials = set()

for call in blr_calls:
    if call[1][:3] == '140':
        # these are telemarketers;
        blr_dials.add('140')
    elif call[1][0] != '(' and call[1][0] in '789':
        # these are mobile numbers;
        blr_dials.add(call[1][:4])
    else:
        # these have to be fixed lines
        _area_code = call[1].split(')', 1)[0][1:]
        blr_dials.add(_area_code)

blr_dials = sorted(list(blr_dials))

print("The numbers called by people in Bangalore have codes:")

for code in blr_dials:
    print(code)






"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

blr_internal = [call for call in blr_calls if call[1][:5] == '(080)']
blr_internal_ratio = len(blr_internal) / len(blr_calls) * 100

print(f"{blr_internal_ratio:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



