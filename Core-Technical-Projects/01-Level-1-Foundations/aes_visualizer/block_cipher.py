import random
import string

def encrypt_message(plaintext):
    xor_key = random.randint(0, 100)
    cipher_blocks = [str(ord(char) ^ xor_key).zfill(3) for char in plaintext]
    binary_key = bin(xor_key)[2:].zfill(10)
    full_payload = "".join(cipher_blocks) + binary_key
    
    encrypted_stream = []
    for char in full_payload:
        encrypted_stream.append(char)
        encrypted_stream.append(random.choice(string.ascii_lowercase))

    return "".join(encrypted_stream)

def decrypt_message(encrypted_stream):
    data_stream = "".join([char for char in encrypted_stream if char.isdigit()])
    xor_key = int(data_stream[-10:], 2)
    decrypted_chars = []
    message_data = data_stream[:-10]

    for i in range(0, len(message_data), 3):
        block = message_data[i : i + 3]
        decrypted_chars.append(chr(int(block) ^ xor_key))

    return "".join(decrypted_chars)

