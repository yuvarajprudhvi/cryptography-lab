from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os

# Function to encrypt a given file
def encrypt_file(file_name, key):
    # Open the file in read mode (binary)
    with open(file_name, 'rb') as f:
        data = f.read()

    # Generate a random IV (Initialization Vector)
    iv = get_random_bytes(AES.block_size)
    
    # Create AES cipher object in CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the data to make sure its length is a multiple of AES block size
    encrypted_data = cipher.encrypt(pad(data, AES.block_size))
    
    # Write the IV and the encrypted data to a new file
    with open(file_name + ".enc", 'wb') as f:
        f.write(iv + encrypted_data)  # Store the IV followed by the encrypted content
    
    print(f"File '{file_name}' encrypted successfully!")

# Function to decrypt the given file
def decrypt_file(file_name, key):
    # Open the encrypted file in read mode (binary)
    with open(file_name, 'rb') as f:
        data = f.read()

    # Extract the IV from the first 16 bytes
    iv = data[:AES.block_size]
    encrypted_data = data[AES.block_size:]

    # Create AES cipher object in CBC mode with the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the data and remove the padding
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Write the decrypted data to a new file
    with open(file_name.replace(".enc", ".dec"), 'wb') as f:
        f.write(decrypted_data)
    
    print(f"File '{file_name}' decrypted successfully!")

# Main function to encrypt and decrypt the file
def main():
    # Define a 256-bit AES key (32 bytes)
    key = get_random_bytes(32)  # AES-256 key
    
    # Path to the file you want to encrypt and decrypt
    file_name = "file.txt"  # Make sure this file exists in your directory

    # Encrypt the file
    encrypt_file(file_name, key)
    
    # Decrypt the file (use the same key for decryption)
    decrypt_file(file_name + ".enc", key)

if __name__ == '__main__':
    main()

