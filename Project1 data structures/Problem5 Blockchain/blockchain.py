import hashlib
import time



class Block:

    def __init__(self, timestamp: str,  data: str, previous_hash: str = '0') -> None:
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self._calc_hash()
      self.prevous_block = None

    def _calc_hash(self) -> str:
        sha = hashlib.sha256()
        sha.update((self.data + self.timestamp + self.previous_hash).encode())
        return '0x' + sha.hexdigest()

    def __repr__(self):
        return f"Block: (data: {self.data[:5]}, hash: {self.hash[:7]})"


class BlockChain:
    def __init__(self):
        self.tail = None

    def append(self, data: str) -> None:
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        if self.tail is None:
            new_block = Block(ts, data, '0')
            self.tail = new_block
        else:
            new_block = Block(ts, data, self.tail.hash)
            new_block.prevous_block = self.tail
            self.tail  = new_block

    def __str__(self):
        string = ""
        tail = self.tail
        while tail:
            string = str(tail) + ' <- ' + string
            tail = tail.prevous_block
        return string


if __name__ == "__main__":
    chain = BlockChain()
    chain.append('Hello, ')
    chain.append('World!')

    # to check if two same datablocks generate different hashes.
    chain.append('Foo')
    chain.append('Foo')
    print(chain)
