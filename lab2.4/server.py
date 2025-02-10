import socket
from rc4 import RC4  

def decrypt_file(encrypted_data, key):

    rc4 = RC4(key)
    decrypted_data = rc4.decrypt(encrypted_data)
    return decrypted_data

def save_file(file_path, data):

    with open(file_path, 'wb') as f:
        f.write(data)
    print(f"File saved at: {file_path}")

def main():
    server_ip = '127.0.0.1'  
    server_port = 12345
    key = b"mysecretkey"  


    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    print(f"Server listening on {server_ip}:{server_port}")


    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")


    encrypted_data = conn.recv(1024*1024)  
    print(f"Received encrypted data from client.")


    save_file("encrypted_file.enc", encrypted_data)


    decrypted_data = decrypt_file(encrypted_data, key)


    save_file("decrypted_file.txt", decrypted_data)


    conn.close()

if __name__ == "__main__":
    main()
