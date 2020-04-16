Tries is implemented as usual. To handle slashes and make things simple I've removed them all and split path in sequence of subaddresses. Default test cases are enough to demosntrate all edge cases.


Time complexity:
    lookup and add_handler: Takes O(n) time where n is number of subaddresses in address. e.g. n for `/about/me` is 2; `about` and `me`
    split_path: Takes O(k) time where k is length of path string. splitting a string is O(n) operation.

Space complexity:
    O(sum(len(path) for all path in trie ))

    Roughly speaking worst case space grows linearly with sum of all paths.