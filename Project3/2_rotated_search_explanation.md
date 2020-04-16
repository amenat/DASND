
To perform rotated array search I've solved the problem in two parts:
    1. Find pivot
    2. Check if number might exist in left or right subarray (divided by the pivot)
    3. Perform binary search.


Time complexity:
    Since binary search is essentially performed twice once for finding pivot and once for number the runtime complexity is O(log n)

Space complexity:
    Only fixed countable variables are used in the problem and length of array doesn't have impact on them. Therefore space complexity is O(1)