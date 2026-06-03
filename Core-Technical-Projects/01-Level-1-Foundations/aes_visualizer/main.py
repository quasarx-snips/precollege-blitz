# main.py
from block_cipher import encrypt_message, decrypt_message

def main():
    word = input("Enter secret message: ")
    encrypted = encrypt_message(word)
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypt_message(encrypted)}")

if __name__ == "__main__":
    main()


#DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
