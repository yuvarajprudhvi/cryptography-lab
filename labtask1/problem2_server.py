import socket


def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - shift_value - shift) % 26 + shift_value)
        else:
            decrypted += char
    return decrypted

def server_program():
    host = "127.0.0.1"  
    port = 12345  

    server_socket = socket.socket()  
    server_socket.bind((host, port))  

    server_socket.listen(1) 
    print(f"Server is listening on {host}:{port}...")
    
    conn, address = server_socket.accept()  
    print(f"Connection from {address}")

    shift = 3  
    
    while True:
       
        data = conn.recv(1024).decode()
        if not data:
            break 

        print("Encrypted message received:", data)

      
        decrypted_message = caesar_decrypt(data, shift)
        print("Decrypted message:", decrypted_message)

      
        response = "Server response: " + decrypted_message
        conn.send(response.encode()) 

    conn.close()  

if __name__ == '__main__':
    server_program()
