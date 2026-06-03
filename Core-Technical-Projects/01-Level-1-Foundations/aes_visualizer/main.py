# main.py
from block_cipher import encrypt_message, decrypt_message
import sys

def main():
    # Use command-line argument if provided, otherwise use a default test value
    word = sys.argv[1] if len(sys.argv) > 1 else "test_message"
    
    encrypted = encrypt_message(word)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt_message(encrypted)}")

if __name__ == "__main__":
    main()
