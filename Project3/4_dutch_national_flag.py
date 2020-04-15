from typing import List, Union


def sort_012(input_list: List[int]) -> Union[List[int], None]:
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a
    single traversal. Returns None if input list contains any other value than
    0, 1 or 2.

    Args:
       input_list(list): List to be sorted
    """

    # copying list is essential otherwise we will end up modifying the original
    # list object. If we count these as "treversal" then it's impossible to
    # solve the given problem in single traversal.
    input_list = input_list[:]

    lo = 0                    # pointer for 0s
    mid = 0                   # pointer for 1s
    hi = len(input_list) - 1  # pointer for 2s

    while mid <= hi:
        if input_list[mid] == 0:
            input_list[lo], input_list[mid] = input_list[mid], input_list[lo]
            mid, lo = mid + 1, lo + 1
        elif input_list[mid] == 2:
            input_list[mid], input_list[hi] = input_list[hi], input_list[mid]
            hi -= 1
        elif input_list[mid] == 1:
            mid += 1
        else:
            print('Error: List should only contain 0,1,2')
            return None

    return input_list


def test_function(test_case: List[int]) -> None:
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([])               # empty lists should work as expected
test_function([3, 3, 1, 2, 0])  # prints an error
