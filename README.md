# BlockResearch

# 1. Blockchain Basics
Blockchain is an immutable decentralized ledger which records and stores transactions in a transparent, secure and tamper-proof way,
These transactions are stored in blocks, these blocks are hashed with the transactions in it,
These hashes of block is connected to the previous block, making a merkle tree,
So in order to tamper any block, the hashes of all previous blocks need to be changed which is mathematically impossible.

And unlike traditional DB, which is controlled by a central authority,
 blockchain is a p2p network in which every user has a copy of the ledger and users agree to reach consensus to decide the state of blockchain.

Use Case:

Blockchain In Real Estate
Tokenized real estate transactions and digital ownership transfer through smart contracts.

Cross-Border Payments
Fast, low-cost, and transparent cross-border money transfers.

# 2 Block Anatomy


+---------------------------------------------------------+
|                      BLOCK                              |
+---------------------------------------------------------+
| Previous Hash : 00xx....                                |
| Timestamp     : 07-06-2025 10:45:30                     |
| Nonce         : 102938                                  |  
| Merkle Root   : 00yy....                                |
+---------------------------------------------------------+
|                     DATA                                |
+---------------------------------------------------------+
| Transaction 1: Alice → Bob: 2 BTC                       |
| Transaction 2: Raj → Prem: 1.5 BTC                      |
| ....                                                    |
+---------------------------------------------------------+
(refer to Theory/Block Anatomy for better diagram)

Merkle Root & Data Integrity
The Merkle Root is a single hash that summarizes all transactions in a block using a Merkle Tree. 
Each transaction is hashed, then pairs of hashes are combined and hashed again, recursively, until one final root hash remains.

It helps verify data integrity by enabling quick and efficient validation that the data has not been altered. 
If any transaction within the block is changed, the Merkle root will also change, signaling that the data has been tampered with.
 This allows nodes to confirm the integrity of the entire dataset without checking every individual transaction.


# 3.  Consensus Conceptualization

Proof of Work (PoW) is a consensus algorithm used by blockchains like Bitcoin to validate transactions and secure the network. 
The process is intentionally resource-intensive to make it costly and time-consuming to manipulate the blockchain. 
It requires participants (miners) to solve complex mathematical puzzles, which involves repeatedly hashing data until a valid result is found. 
This heavy computation demands significant electricity and specialized hardware, leading to its high energy consumption.


Proof of Stake (PoS) replaces computational work with financial commitment. Instead of miners, 
validators are chosen to create new blocks based on the amount of cryptocurrency they "stake" or lock up as collateral.
This model drastically reduces energy usage since no intense computations are required. 
Unlike PoW, where computing power determines block creation chances, PoS uses the amount of stake and sometimes the duration of staking as the primary selection criteria, 
making it more energy-efficient and accessible.

Delegated Proof of Stake (DPoS) is a variation of PoS where token holders vote to elect a fixed number of delegates or validators to produce blocks and maintain the network. 
The voting power is proportional to the amount of tokens held, making it a representative system. 
Validators are incentivized to perform honestly since voters can replace them if they act maliciously or inefficiently. 
This method increases transaction throughput and governance flexibility, but can introduce centralization concerns.
