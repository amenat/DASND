import sys
import os
import heapq
import pickle
from collections import Counter
from typing import Any, Dict, Tuple
from functools import total_ordering


@total_ordering
class Node:
    def __init__(self, char: str, freq: int, is_internal=False, right=None, left=None) -> None:
        if not (isinstance(char, str) and len(char) == 1):
            raise ValueError('char of node should be of type str and length 1')
        if not isinstance(freq, int): raise ValueError('freq should be integer')
        if not isinstance(is_internal, bool): raise ValueError('in_internal should be boolean')
        if not all(map(lambda child: isinstance(child, Node) or child is None, [right, left])):
            raise ValueError('right and left should be Node or None.')

        self.char = char
        self.freq = freq
        self.is_internal = is_internal
        self.right = right
        self.left = left

    # dunder methods to ensure heapq works
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Node): raise ValueError(f'Can\'t compare Node to {type(other)}')
        return self.freq == other.freq

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Node): raise ValueError(f'Can\'t compare Node to {type(other)}')
        return self.freq < other.freq

    # Create an internal node based on two nodes
    def __add__(self, other: object):
        if not isinstance(other, Node): raise ValueError(f'Can\'t add Node to {type(other)}')

        total_freq = self.freq + other.freq
        return Node('*', total_freq, is_internal=True, right=other, left=self)

    def __repr__(self):
        return f'({self.char} : {self.freq})'


def map_tree_to_dict(tree: Node, binary: str='') -> Dict:
    mapping = dict()
    if not tree.is_internal:
        mapping[tree.char] = binary
    else:
        if tree.left:
            mapping.update(map_tree_to_dict(tree.left, binary + '0'))
        if tree.right:
            mapping.update(map_tree_to_dict(tree.right, binary + '1'))
    return mapping


# Adapted from: https://stackoverflow.com/questions/16887493/write-a-binary-integer-or-string-to-a-file-in-python
def bit_string_to_file(bitstring: str, filename: str) -> None:
    bit_strings = [bitstring[i:i + 8] for i in range(0, len(bitstring), 8)]
    byte_list = [int(b, 2) for b in bit_strings]

    with open(filename, 'wb') as f:
        f.write(bytearray(byte_list))  # convert to bytearray before writing


def file_to_bitstring(filename: str) -> str:
    with open(filename, 'rb') as f:
        content = f.read()
    bitstring = ''
    for byte in content[:-1]:
        bitstring += '{0:08b}'.format(byte)

    # handle trailing byte seperately
    bitstring += '{}'.format(bin(content[-1])[2:])
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
        right_node = Node('*', 0, False)       # dummy node
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
    mapping = map_tree_to_dict(tree)

    # encode data
    char_data = list(data)

    compressed = ''
    for char in char_data:
        compressed += mapping[char]

    return compressed, tree



def huffman_decoding(data:str, tree: Node) -> str:
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

    # Change: size of tree should also be considered as without it we can't decode
    # this demonstrate that huffman coding is not very effective on very small strings with no repetition.
    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2)) + sys.getsizeof(tree)}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
    print (f"The content of the decoded data is: {decoded_data}")



    print('\n-- Test case #2: Same character in string -- ')

    a_great_sentence = "aaaaaaa"

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence)}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2)) + sys.getsizeof(tree)}")
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

        print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2)) + sys.getsizeof(tree)}")
        print (f"The content of the encoded data is: {encoded_data}")

        decoded_data = huffman_decoding(encoded_data, tree)

        print (f"The size of the decoded data is: {sys.getsizeof(decoded_data)}")
        print (f"The content of the decoded data is: {decoded_data}")
    except ValueError as v:
        print(f'Expected Exception caught: {v}')
        pass


    print('\n-- Test case #4: Alice in WonderLand full book -- ')

    book = 'alice.txt'
    with open(book, 'r', encoding='utf-8') as alice:
        data = alice.read()
    bitstring, tree = huffman_encoding(data)

    compressed_file = 'alice.dat'
    bit_string_to_file(bitstring, compressed_file)

    # Store tree in file
    treefile = 'alice.tree'

    with open(treefile, 'wb') as f:
        pickle.dump(tree, f)

    # create bitstring to decode
    to_decode = file_to_bitstring(compressed_file)

    # retrieve tree in file
    with open(treefile, 'rb') as f:
        tree = pickle.load(f)

    decoded = huffman_decoding(to_decode, tree)

    original_file_size = os.stat(book).st_size
    compressed_file_size = os.stat(compressed_file).st_size + os.stat(treefile).st_size

    print(f'Original file size: {original_file_size} bytes')
    print(f'Compressed file size: {compressed_file_size} bytes')
    print(f'Compression file is : {100*(1 - compressed_file_size/original_file_size):.2f}% smaller')

    print(f'Does decoded data match orginal? : {data == decoded}')