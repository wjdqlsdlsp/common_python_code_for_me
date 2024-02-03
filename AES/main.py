from aes_cipher import StaticAESCipher
from random_generate_key import random_generate_key


if __name__ == "__main__":
    key = random_generate_key(letter_number=32)
    cipher = StaticAESCipher(key=key)

    data = "Hello, World! This is a test code for AES encryption and decryption."
    encrypted_data = cipher.encrypt(data)
    print(f"Encrypted data: {encrypted_data}")
    decrypted_data = cipher.decrypt(encrypted_data)
    print(f"Decrypted data: {decrypted_data}")
