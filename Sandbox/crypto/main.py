import matplotlib.pyplot as plt
from cryptography.fernet import Fernet
from collections import Counter

def plot_side_by_side(plaintext, ciphertext):
    # Prepare data for plotting
    plain_counts = Counter(list(plaintext.encode()))
    cipher_counts = Counter(list(ciphertext))

    # Create subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Plot Plaintext
    ax1.bar(plain_counts.keys(), plain_counts.values(), color='blue')
    ax1.set_title("Plaintext (Patterned)")
    ax1.set_xlabel("Byte Value")
    ax1.set_ylabel("Frequency")

    # Plot Ciphertext
    ax2.bar(cipher_counts.keys(), cipher_counts.values(), color='red')
    ax2.set_title("Ciphertext (Randomized)")
    ax2.set_xlabel("Byte Value")
    ax2.set_ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("crypto.png")

# 1. Setup Encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# 2. The Secret Message
secret_msg = "ABBBCDEFGGGHIJJJJJJJJJKLMNOPQRSTUVWXYZZZZZZZZZZZZZZZZZ"
encrypted_msg = cipher_suite.encrypt(secret_msg.encode())

# 3. Visualize
print(f"Original: {secret_msg}")
print(f"Encrypted: {encrypted_msg[:30]}...") # Printing partial
plot_side_by_side(secret_msg, encrypted_msg)
