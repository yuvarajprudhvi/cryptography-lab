import socket
from rc4 import RC4  # Import the custom RC4 class

def decrypt_file(encrypted_data, key):
    # Initialize RC4 cipher with the provided key
    rc4 = RC4(key)
    decrypted_data = rc4.decrypt(encrypted_data)
    return decrypted_data

def save_file(file_path, data):
    # Save the received or decrypted file data to disk
    with open(file_path, 'wb') as f:
        f.write(data)
    print(f"File saved at: {file_path}")

def main():
    server_ip = '127.0.0.1'  # Localhost, change this for remote server
    server_port = 12345
    key = b"mysecretkey"  # RC4 decryption key

    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Server listening on {server_ip}:{server_port}")

    # Wait for a connection from the client
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive the encrypted file data
    encrypted_data = conn.recv(1024*1024)  # Adjust the buffer size if needed
    print(f"Received encrypted data from client.")

    # Save the encrypted file to disk
    save_file("encrypted_file.enc", encrypted_data)

    # Decrypt the received data
    decrypted_data = decrypt_file(encrypted_data, key)

    # Save the decrypted file to disk
    save_file("decrypted_file.txt", decrypted_data)

    # Close the server connection
    conn.close()

if __name__ == "__main__":
    main()
