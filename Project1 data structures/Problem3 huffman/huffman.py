'''
Here is one type of pseudocode for this coding schema:

    Take a string and determine the relevant frequencies of the characters.
    Build and sort a list of tuples from lowest to highest frequencies.
    Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
    Trim the Huffman Tree (remove the frequencies from the previously built tree).
    Encode the text into its compressed form.
    Decode the text from its compressed form.

You then will need to create encoding, decoding, and sizing schemas.
'''

import sys
import heapq
from collections import Counter
from typing import Any, Dict
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, char: str, freq: int, is_internal=False, right=None, left=None) -> None:
        self.char = char
        self.freq = freq
        self.is_internal = is_internal
        self.right = right
        self.left = left

    # dunder methods to ensure heapq works
    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    # Create an internal node based on two nodes
    def __add__(self, other):
        total_freq = self.freq + other.freq
        return Node('*', total_freq, is_internal=True, right=self, left=other)

    def __str__(self):
        return f'({self.char} : {self.freq})'

    def __repr__(self):
        return f'({self.char} : {self.freq})'


def traverse_tree(tree: Node, binary='') -> Dict:
    mapping = dict()
    if not tree.is_internal:
        mapping[tree.char] = binary
    else:
        if tree.left:
            mapping.update(traverse_tree(tree.left, binary + '0'))
        if tree.left:
            mapping.update(traverse_tree(tree.right, binary + '1'))
    return mapping





def huffman_encoding(data: str):
    # convert data to
    char_freq = Counter(data)
    list_chars = [Node(char, freq, False) for char, freq in char_freq.items()]

    # convert to min-heap
    heapq.heapify(list_chars)

    while len(list_chars) >= 2:
        left_node = heapq.heappop(list_chars)
        right_node = heapq.heappop(list_chars)
        new_internal_node = left_node + right_node
        heapq.heappush(list_chars, new_internal_node)

    tree = list_chars[0]

    # treverse and and create mapping
    mapping = traverse_tree(tree)
    # encode data
    char_data = list(data)

    compressed = ''
    for char in char_data:
        compressed += mapping[char]

    return compressed, tree



def huffman_decoding(data:str, tree: Node):
    string = ''
    ptr = tree
    for i in range(len(data)):
        if data[i] == '0':
            ptr = ptr.left
        elif data[i] == '1':
            ptr = ptr.right
        if not ptr.is_internal:
            string += ptr.char
            ptr = tree
            continue



    return string
        

if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))