Problem 5: block chain

Block chain is implemented by creating a linked list that has pointer to tail instead of head. In a way it's a stack without pop operation.

Block class stores data in string, calculates and udpates unique hash. Uniqueness of hash is ensured by concatinating data with prevous hash and timestamp.


Runtime complexity: O(1) to insert data block into blockchain. There are only constant time operations happening in append.

I couldn't find any info on complexity of sha256 hash calculation. In worst case scenario I think it would be O(n) where n is length of string.

Space complexity: O(n) grows with respect to data blocks and amount of data stored in datablocks. No additional space is required.