import socket
from rc4 import RC4  # Import the custom RC4 class
import os

def encrypt_file(input_file_path, key):
    # Open and read the file to be encrypted
    with open(input_file_path, 'rb') as f:
        data = f.read()

    # Initialize RC4 cipher with the provided key
    rc4 = RC4(key)
    encrypted_data = rc4.encrypt(data)

    return encrypted_data

def send_file(client_socket, file_path, key):
    # Encrypt the file before sending it
    encrypted_data = encrypt_file(file_path, key)

    # Send the encrypted file to the server
    client_socket.sendall(encrypted_data)
    print(f"Encrypted file sent to server.")

def main():
    server_ip = '127.0.0.1'  # Change this if the server is on a different machine
    server_port = 12345
    key = b"mysecretkey"  # RC4 encryption key

    file_path = "file.txt"  # Name of the file to encrypt and send

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    send_file(client_socket, file_path, key)

    # Close the socket connection
    client_socket.close()

if __name__ == "__main__":
    main()
