import sys
import heapq
import pickle
from collections import Counter
from typing import Any, Dict, Tuple
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
        return Node('*', total_freq, is_internal=True, right=other, left=self)

    def __repr__(self):
        return f'({self.char} : {self.freq})'


def traverse_tree(tree: Node, binary: str='') -> Dict:
    mapping = dict()
    if not tree.is_internal:
        mapping[tree.char] = binary
    else:
        if tree.left:
            mapping.update(traverse_tree(tree.left, binary + '0'))
        if tree.right:
            mapping.update(traverse_tree(tree.right, binary + '1'))
    return mapping


def bit_string_to_file(bitstring: str, filename: str) -> None:
    bit_strings = [bitstring[i:i + 8] for i in range(0, len(bitstring), 8)]
    byte_list = [int(b, 2) for b in bit_strings]

    with open(filename, 'wb') as f:
        f.write(bytearray(byte_list))  # convert to bytearray before writing


def file_to_bitstring(filename: str) -> str:
    with open(filename, 'rb') as f:
        content = f.read()
    bitstring = ''
    for byte in content:
        bitstring += '{0:08b}'.format(byte)
    return bitstring



def huffman_encoding(data: str) -> Tuple[str, Node]:
    # convert data to dictionary with character frequency
    if not isinstance(data, str): raise ValueError('data should of type str')
    if len(data) == 0: raise ValueError('data must not be empty')

    char_freq = Counter(data)
    list_chars = [Node(char, freq, False) for char, freq in char_freq.items()]

    # convert to min-heap
    heapq.heapify(list_chars)

    # Special case of single string with same repeating character
    # a small optimization; since doing this for all cases means adding 1 extra unnecessary bit to all
    # characters and thus losing optimality of prefix codes.
    if len(list_chars) == 1:
        left_node = heapq.heappop(list_chars)
        right_node = Node('', 0, False)       # dummy node
        new_internal_node = left_node + right_node
        heapq.heappush(list_chars, new_internal_node)
    else:
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
    print('-- Test case #1: Regular string -- ')

    a_great_sentence = "The bird is the word"

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print (f"The content of the decoded data is: {decoded_data}")



    print('\n-- Test case #2: Same character in string -- ')

    a_great_sentence = "aaaaaaa"

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print (f"The content of the decoded data is: {decoded_data}")



    print('\n-- Test case #3: Empty string -- ')

    a_great_sentence = ""

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print (f"The content of the data is: {a_great_sentence}")
    # this will throw ValueError as expected; we will continue running program to next error
    try:
        encoded_data, tree = huffman_encoding(a_great_sentence)

        print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
        print (f"The content of the encoded data is: {encoded_data}")

        decoded_data = huffman_decoding(encoded_data, tree)

        print (f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
        print (f"The content of the decoded data is: {decoded_data}")
    except ValueError as v:
        print(f'Expected Exception caught: {v}')
        pass


    print('\n-- Test case #4: Alice in WonderLand book -- ')

    with open('alice.txt', 'r', encoding='utf-8') as alice:
        data = alice.read()
    bitstring, tree = huffman_encoding(data)
    print(bitstring[-180:])

    compressed_file = 'alice.dat'
    bit_string_to_file(bitstring, compressed_file)

    # Store tree in file
    treefile = 'alice.tree'

    with open(treefile, 'wb') as f:
        pickle.dump(tree, f)

    # create bitstring to decode
    to_decode = file_to_bitstring(compressed_file)
    print(to_decode[-180:])

    # retrieve tree in file
    with open(treefile, 'rb') as f:
        tree = pickle.load(f)

    decoded = huffman_decoding(to_decode, tree)

    print(f'Does decoded data match orginal? : {data == decoded}')