from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os


def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext, DES.block_size)  # Pad plaintext to match block size
    encrypted_data = cipher.encrypt(padded_plaintext)
    
    with open(output_file, 'wb') as f:
        f.write(encrypted_data)

    print(f"File '{input_file}' has been encrypted and saved as '{output_file}'.")


def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()
    
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher.decrypt(encrypted_data)
    decrypted_data = unpad(decrypted_padded, DES.block_size)  # Remove padding
    
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

    print(f"File '{input_file}' has been decrypted and saved as '{output_file}'.")


if __name__ == "__main__": 
    key = b'8bytekey' 
    
    
    plaintext_file = "plaintext.txt"
    encrypted_file = "encrypted_file.des"
    decrypted_file = "decrypted_file.txt"
    
 
    encrypt_file(plaintext_file, encrypted_file, key)
    
   
    decrypt_file(encrypted_file, decrypted_file, key)

