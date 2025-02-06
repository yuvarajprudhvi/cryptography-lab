from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# Function to encrypt a file
def encrypt_file(file_name, key):
    # Open the file in read mode
    with open(file_name, 'rb') as f:
        data = f.read()

    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(AES.block_size)
    
    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data to make sure it's a multiple of block size
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    # Write encrypted data to file (including IV at the beginning)
    with open(file_name + ".enc", 'wb') as f:
        f.write(iv + encrypted_data)
    
    print(f"File '{file_name}' encrypted successfully!")

# Function to decrypt a file
def decrypt_file(file_name, key):
    # Open the encrypted file in read mode
    with open(file_name, 'rb') as f:
        data = f.read()

    # Extract the IV from the encrypted file (first 16 bytes)
    iv = data[:AES.block_size]
    encrypted_data = data[AES.block_size:]

    # Create AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt and unpad the data
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Write decrypted data to a file
    with open(file_name.replace(".enc", ".dec"), 'wb') as f:
        f.write(decrypted_data)
    
    print(f"File '{file_name}' decrypted successfully!")

# Main function to run the encryption and decryption process
def main():
    # Define a 256-bit AES key (32 bytes)
    key = get_random_bytes(32)  # AES-256 key
    
    # File path of the text file you want to encrypt/decrypt
    file_name = "plain_text.txt"  # Replace with your file path
    
    # Encrypt the file
    encrypt_file(file_name, key)
    
    # Decrypt the file (use the same key for decryption)
    decrypt_file(file_name + ".enc", key)

if __name__ == '__main__':
    main()

