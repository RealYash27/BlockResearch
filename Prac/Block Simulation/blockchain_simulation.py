import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index                  # Block number
        self.timestamp = timestamp          # Creation time
        self.data = data                    # Arbitrary block data
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = 0                      
        self.hash = self.calculate_hash()   # Generate current block hash

    def calculate_hash(self):
        # Combine all data into a string and hash it using SHA-256
        block_content = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]  # Initialize with first block

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        # Link new block to the chain
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
        print(f"[INFO] Block {new_block.index} added with hash: {new_block.hash}")

    def is_chain_valid(self):
        # Verify the integrity of the blockchain
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                print(f"[ERROR] Block {i}'s hash is invalid.")
                return False
            if curr.previous_hash != prev.hash:
                print(f"[ERROR] Block {i}'s previous hash does not match.")
                return False
        print("[INFO] Blockchain is valid.")
        return True

    def display_chain(self):
        print("\n[CHAIN DATA] -------------------------------")
        for block in self.chain:
            print(f"Index       : {block.index}")
            print(f"Timestamp   : {block.timestamp}")
            print(f"Data        : {block.data}")
            print(f"Nonce       : {block.nonce}")
            print(f"Prev. Hash  : {block.previous_hash}")
            print(f"Hash        : {block.hash}")
            print("--------------------------------------------")

# Initialize blockchain
my_chain = Blockchain()
my_chain.add_block(Block(1, time.time(), "Block 1 Data"))
my_chain.add_block(Block(2, time.time(), "Block 2 Data"))

# Display original chain
print("\n[STATUS] Original Blockchain:")
my_chain.display_chain()
my_chain.is_chain_valid()

# Tamper with Block 1
print("\n[ATTACK] Tampering with Block 1's data...")
my_chain.chain[1].data = "Tampered Data"
my_chain.chain[1].hash = my_chain.chain[1].calculate_hash()  # Recalculate Block 1 only

# Display tampered chain
print("\n[STATUS] Blockchain after tampering:")
my_chain.display_chain()
my_chain.is_chain_valid()
