# main.py snippet
from block_cipher import encrypt_message, decrypt_message

# Simple interface to capture input
secret = input("Enter your message to secure: ")
print(f"Encrypted Output: {encrypt_message(secret)}")
print(f"Decrypted Output: {decrypt_message(encrypt_message(secret))}")
