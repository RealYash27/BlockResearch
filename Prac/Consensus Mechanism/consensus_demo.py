import random

# === MOCK VALIDATORS ===

# PoW: each miner has a random "computational power"
pow_validators = {
    "Miner Alice": random.randint(1, 100),
    "Miner Bob": random.randint(1, 100),
    "Miner Carol": random.randint(1, 100)
}

# PoS: each staker has a random "stake" value
pos_validators = {
    "Staker Alice": random.randint(100, 1000),
    "Staker Bob": random.randint(100, 1000),
    "Staker Carol": random.randint(100, 1000)
}

# DPoS: 3 voter accounts each vote for a delegate
delegates = ["Alice", "Bob", "Charlie"]
voters = {
    "Voter1": random.choice(delegates),
    "Voter2": random.choice(delegates),
    "Voter3": random.choice(delegates)
}

# === SIMULATION LOGIC ===

# --- PoW ---
pow_selected = max(pow_validators, key=pow_validators.get)
print("\n[PoW] Proof of Work Consensus:")
print(f"Validator power levels: {pow_validators}")
print(f"Selected: {pow_selected} (highest computational power: {pow_validators[pow_selected]})")
print("Logic: The miner with the highest hash power wins the right to add the block.")

# --- PoS ---
pos_selected = max(pos_validators, key=pos_validators.get)
print("\n[PoS] Proof of Stake Consensus:")
print(f"Validator stakes: {pos_validators}")
print(f"Selected: {pos_selected} (highest stake: {pos_validators[pos_selected]})")
print("Logic: The staker with the most coins staked is most likely to be chosen.")

# --- DPoS ---
# Count votes for each delegate
vote_counts = {delegate: list(voters.values()).count(delegate) for delegate in delegates}
most_voted = [k for k, v in vote_counts.items() if v == max(vote_counts.values())]
dpos_selected = random.choice(most_voted)  # Randomly select among top-voted in case of tie

print("\n[DPoS] Delegated Proof of Stake Consensus:")
print(f"Voter choices: {voters}")
print(f"Vote counts: {vote_counts}")
print(f"Selected delegate: {dpos_selected}")
print("Logic: Delegates are voted in by token holders. The most-voted delegate validates the block.")

