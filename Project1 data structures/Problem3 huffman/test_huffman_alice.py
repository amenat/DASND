from huffman import huffman_encoding, huffman_decoding
import pickle

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


if __name__ == "__main__":
    # TODO: Fix trailing newline issue
    with open('alice.txt', 'r', encoding='utf-8') as alice:
        data = alice.read()
    bitstring, tree = huffman_encoding(data)

    compressed_file = 'alice.dat'
    bit_string_to_file(bitstring, compressed_file)

    # Store tree in file
    with open('alice.tree', 'wb') as f:
        pickle.dump(tree, f)


    # create bitstring
    to_decode = file_to_bitstring(compressed_file)

    # retrieve tree in file
    with open('alice.tree', 'rb') as f:
        tree = pickle.load(f)

    decoded = huffman_decoding(to_decode, tree)

    print(len(bitstring))
    print(len(to_decode))
    print(f'Does decoded data match orginal? : {data == decoded}')

