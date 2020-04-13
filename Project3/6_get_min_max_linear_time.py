from typing import List, Tuple, Callable

## for testing
import random

def get_min_max(ints: List[int]) -> Tuple[int, int]:
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        print('Error: get_max_min must list of more than 0 elements')
        return None

    small = big = ints[0]

    for num in ints:
        if num > big:
            big = num
        if num < small:
            small = num
    return small, big


# a more random test
l = [random.randint(-1000, 1000) for i in range(1000)]
random.shuffle(l)

def test_min_max(func: Callable, samples: int, arrsize: int) -> bool:
    for _ in range(samples):
        l = [random.randint(-arrsize, arrsize) for i in range(arrsize)]
        random.shuffle(l)
        if (min(l), max(l)) != get_min_max(l):
            return False
    return True


if __name__ == "__main__":
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

    # do multiple randomized test
    print('all test passed' if test_min_max(get_min_max, 1000, 1000) else 'test failed')

    # check empty list
    get_min_max([])