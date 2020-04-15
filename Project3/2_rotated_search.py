'''Search in a Rotated Sorted Array

You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:
'''

from typing import List

def rotated_array_search(input_list: List[int] , number: int) -> int:
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # find smallest int using binary search
    length = len(input_list) -1
    lo = 0
    hi = length - 1
    pivot = 0
    while hi >= lo:
        mid = (lo + hi) // 2
        if (input_list[mid] < input_list[mid+1]) and (input_list[mid] < input_list[mid-1]):
            pivot = mid
            break
        elif input_list[0] > input_list[mid]:
            hi = mid - 1
        else:
            lo = mid + 1


    # find item index using binary search
    if number >= input_list[0] and pivot != 0:
        lo = 0
        hi = pivot - 1
    else:
        lo = pivot
        hi = length - 1


    while hi >= lo:
        mid = (lo + hi) // 2

        if input_list[mid] == number:   #check instead at + pivot point
            return mid
        elif number > input_list[mid]:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])