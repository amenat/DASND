
We create 3 pointer for tracking where to insert 0, 1 and 2.

We iterate over till 1s pointer reaches 2s pointer. This way we will only be treversing whole array at maximum 1 time.

while iterating with 1s pointer:
    if number is 0: swap with 0s pointer
    if number is 2: swap with 2s pointer
    else: continue as 1 is in 1s pointer.

    increment relevant pointers

This ensures the invariant and array is sorted in place.

Time complexity: O(n) since we treverse array only once and do O(1) work in each iteration.
Space complexity: O(n) space required for creating copy of list; otherwise we will end up modifying original list. If function instead needs to modify original list the space complexity will be O(1) since no additional space is required.