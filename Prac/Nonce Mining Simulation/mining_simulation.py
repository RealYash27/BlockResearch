import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(content.encode()).hexdigest()

    def mine_block(self, difficulty):
        print(f"\n[MINING] Block {self.index} | Difficulty: {difficulty}")
        prefix = '0' * difficulty
        start = time.time()

        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.calculate_hash()

        end = time.time()
        print(f"[SUCCESS] Block {self.index} mined!")
        print(f"  ➤ Nonce attempts : {self.nonce}")
        print(f"  ➤ Final Hash     : {self.hash}")
        print(f"  ➤ Time Taken     : {end - start:.4f} sec")


# Run mining simulation directly
if __name__ == "__main__":
    difficulty = 4
    block = Block(1, time.time(), "Sample Data", "0000abc")
    block.mine_block(difficulty)

    # Print final block details
    print("\n[FINAL BLOCK DATA]")
    print(f"Index         : {block.index}")
    print(f"Data          : {block.data}")
    print(f"Nonce         : {block.nonce}")
    print(f"Prev. Hash    : {block.previous_hash}")
    print(f"Final Hash    : {block.hash}")
