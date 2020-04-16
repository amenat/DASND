A common pattern in maximizing sum of two numbers is maximize most significant digit of both numbers; then maximze second significant digit and so on.

This structure is very similar to a heap.

Hence my solution:
1. min-heapify array
2. extract-min and add in two numbers; take care of decimal digit position.
3. If one number is left add it in first one.


Time complexity:
    heapify takes at worst O(n log n) time.
    performing extract-min takes O(log n) time and doing that n times means O(n log n)
    Overall time complexity is O(n log n)

Space complexity:
    Whole solution runs in constant space with variables for storing two values to be returned. Hence space complexity is  O(1)