Finding floored square root.


Typical method of searching square root is Newton/Heron method but since we don't care about precisiona and just need floored square we can perform binary search. Usual binary search termination condition is finding item equal to key but here I've modified to find a number who'se square is not bigger than number and next integer's square will be bigger than number. Due to closure properties and quadratic growth this identifies floor square root correctly.


Asymptotic analysis (assuming number fits in word length of computer)

Time complexity:
    Every iteration we divide the search space by half. Hence runtime will be θ(lg n) or O(log n)


Space complexity:
    No additional memory is used other than 3 variables. Space complexity is O(1)