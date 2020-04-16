import heapq
from typing import List, Tuple

def rearrange_digits(input_list: List[int]) -> Tuple[int, int]:
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # heapify input list
    heapq.heapify(input_list)
    first = second = 0
    power = 0
    while len(input_list) >= 2:
        first += heapq.heappop(input_list) * 10 ** power
        second += heapq.heappop(input_list) * 10 ** power
        power += 1

    if len(input_list) > 0:
        first += heapq.heappop(input_list) * 10 ** power

    return int(first), int(second)




def test_function(test_case: List[List[int]]) -> None:
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])     # pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # pass
test_function([[0,1, 2], [20, 1]])              # pass
test_function([[0, 0], [0, 0]])                 # pass
test_function([[1,0, 0, 1, 0], [100, 100]])     # fail