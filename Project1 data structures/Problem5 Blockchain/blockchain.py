import hashlib
import time
from typing import Union



class Block:

    def __init__(self, timestamp: str,  data: str, previous_hash: Union[str, None]=None, idx=0):

        if not isinstance(timestamp, str): raise ValueError('timestamp should be of type str')
        if not isinstance(data, str): raise ValueError('data should be of type str')
        if not (isinstance(previous_hash, str) or previous_hash is None): raise ValueError('previous_hash should be str or None')
        self.idx = idx
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.prevous_block = None
        self.hash = self._calc_hash()

    def _calc_hash(self) -> str:
        sha = hashlib.sha256()
        sha.update((self.data + self.timestamp + str(self.previous_hash)).encode())
        return '0x' + sha.hexdigest()

    def __repr__(self) -> str:
        return f"Block {self.idx}: (ts: {self.timestamp}, hash: {self.hash[:10]}, data: \'{self.data[:10]}\')"


class BlockChain:
    def __init__(self):
        self.tail = None
        self.size = 0

    def append(self, data: str) -> None:
        if not isinstance(data, str): raise ValueError('Data should be of type `str`')

        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        if self.tail is None:
            new_block = Block(ts, data, None, self.size)
        else:
            new_block = Block(ts, data, self.tail.hash, self.size)
            new_block.prevous_block = self.tail

        self.tail  = new_block
        self.size += 1

    def __repr__(self):
        string = "--- tail of blockchain ---\n"
        tail = self.tail
        while tail:
            string += str(tail) + '\n'
            tail = tail.prevous_block

        string += "--- beginning of blockchain ---\n"
        return string


if __name__ == "__main__":
    chain = BlockChain()
    chain.append('Hello, ')
    time.sleep(1) # to simulate different timestamps
    chain.append('World!')
    time.sleep(1) # to simulate different timestamps

    # to check if two same data generate different hashes.
    chain.append('Foo')
    time.sleep(1) # to simulate different timestamps
    chain.append('Foo')
    time.sleep(1) # to simulate different timestamps
    print(chain)

    print('Append empty string block')
    chain.append('') # appending empty string shouldn't be a problem
    print(chain)

    # blocks can't be manually appended
    new_block = Block('FakeTS', 'Hello world', None, 1)
    chain.append(new_block)   # should raise ValueError

