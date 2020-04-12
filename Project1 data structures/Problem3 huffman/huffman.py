import sys
import heapq
import pickle
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


# ref: https://stackoverflow.com/questions/16887493/write-a-binary-integer-or-string-to-a-file-in-python
def bit_string_to_file(bitstring: str, filename: str) -> None:
    bit_strings = [bitstring[i:i + 8] for i in range(0, len(bitstring), 8)]
    byte_list = [int(b, 2) for b in bit_strings]

    with open(filename, 'wb') as f:
        f.write(bytearray(byte_list))  # convert to bytearray before writing


# debug this
def file_to_bitstring(filename: str) -> str:
    with open(filename, 'rb') as f:
        content = f.read()
    bitstring = ''
    for byte in content:
        bitstring += '{0:08b}'.format(byte)
    return bitstring



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
    print('-- Test case #2: Regular string -- ')

    a_great_sentence = "The bird is the word"

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence))}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data))}")
    print (f"The content of the decoded data is: {decoded_data}")



    print('-- Test case #2: Same character in string -- ')

    a_great_sentence = "aaaaa"

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence))}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data))}")
    print (f"The content of the decoded data is: {decoded_data}")



    print('-- Test case #3: Empty string -- ')

    a_great_sentence = ""

    print (f"The size of the data is: {sys.getsizeof(a_great_sentence))}")
    print (f"The content of the data is: {a_great_sentence}")

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print (f"The size of the encoded data is: {sys.getsizeof(int(encoded_data, base=2))}")
    print (f"The content of the encoded data is: {encoded_data}")

    decoded_data = huffman_decoding(encoded_data, tree)

    print (f"The size of the decoded data is: {sys.getsizeof(decoded_data))}")
    print (f"The content of the decoded data is: {decoded_data}")


    print('-- Test case #4: Alice in WonderLand book -- ')

    with open('alice.txt', 'r', encoding='utf-8') as alice:
        data = alice.read()
    bitstring, tree = huffman_encoding(data)

    compressed_file = 'alice.dat'
    bit_string_to_file(bitstring, compressed_file)

    # Store tree in file
    with open('alice.tree', 'wb') as f:
        pickle.dump(tree, f)

    # create bitstring to decode
    to_decode = file_to_bitstring(compressed_file)

    # retrieve tree in file
    with open('alice.tree', 'rb') as f:
        tree = pickle.load(f)

    decoded = huffman_decoding(to_decode, tree)

    print(len(bitstring))
    print(len(to_decode))
    print(f'Does decoded data match orginal? : {data == decoded}')