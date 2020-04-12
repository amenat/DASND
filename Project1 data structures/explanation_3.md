Problem 3: Huffman coding

Pseudocode:

Encoding:
    create a dictionary of characters and frequencies.
    Create binary tree nodes for all character and frequencies.
    Sort characters by asending frequencies. I used min-heap to achieve this.
    Greedy creation of huffman tree:
        Pick two smallest item from heap and create an internal node with sum of both.
    create map(characters -> binary string)
    create encoded bitstring by iterating over string and replacing character with respective binary string mapping.
    return encoded string and heap.

Decoding:
    set pointer to root of heap
    Iterate over bitstring one bit at a time:
        if 0: move left
        else if 1: move right
        if arrived at leaf node: append character of that node to decoded string and reset pointer to root of heap
    return decoded string.

Read/write from files:
    encoding:
    read txt file as a long utf-8 string
    run huffman_encode()
    Convert bitstring to bytes and write to file
    pickle the tree for future reference

    decoding:
    read bytes and convert back to bitstring
    load pickled tree
    run huffman_decode()

Complexity analysis:
    encode:
        Overall runtime is O(n logn) where n is length of string/

        Converting list to frequency hash table: takes O(n) time
        Creating internal node in huffman tree takes O(log n) time in min-heap; total n nodes are there hence O(n logn)
        Creating map(char -> binary) takes O(n log n) time.
        Hashing is O(1) hence creating bitstring from data takes O(n) time.


        Overall space complexity is O(n) as data is duplicated between Counter, heap etc. but copies aren't made more than O(n) times.

    decode:
        Each charater takes O(log n) time for retrieval from huffman tree.
        Hence overall runtime is O(n log n)

        Space complexity is trivially O(n) as nothing else is stored other than original data being decoded.

