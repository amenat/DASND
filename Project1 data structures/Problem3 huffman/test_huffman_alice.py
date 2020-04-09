from huffman import huffman_encoding, huffman_decoding


# ref: https://stackoverflow.com/questions/16887493/write-a-binary-integer-or-string-to-a-file-in-python
def bit_string_to_file(bitstring, filename):
    bit_strings = [bitstring[i:i + 8] for i in range(0, len(bitstring), 8)]
    byte_list = [int(b, 2) for b in bit_strings]

    with open(filename, 'wb') as f:
        f.write(bytearray(byte_list))  # convert to bytearray before writing


def file_to_bitstring(file):
    pass



if __name__ == "__main__":
    with open('alice.txt') as alice:
        data = alice.read()
    bitstring, tree = huffman_encoding(data)
    compressed_file = 'alice.dat'

    bit_string_to_file(bitstring, compressed_file)
    to_decode = file_to_bitstrineg(compressed_file)

    decoded = huffman_decoding(to_decode, tree)

    print(f'Does decoded data match orginal? : {data == decoded}')

