import socket
from rc4 import RC4  
import os

def encrypt_file(input_file_path, key):

    with open(input_file_path, 'rb') as f:
        data = f.read()


    rc4 = RC4(key)
    encrypted_data = rc4.encrypt(data)

    return encrypted_data

def send_file(client_socket, file_path, key):

    encrypted_data = encrypt_file(file_path, key)


    client_socket.sendall(encrypted_data)
    print(f"Encrypted file sent to server.")

def main():
    server_ip = '127.0.0.1'  
    server_port = 12345
    key = b"mysecretkey"  

    file_path = "file.txt" 


    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    send_file(client_socket, file_path, key)


    client_socket.close()

if __name__ == "__main__":
    main()
