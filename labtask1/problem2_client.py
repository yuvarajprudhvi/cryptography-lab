import socket


def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_value = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_value + shift) % 26 + shift_value)
        else:
            encrypted += char
    return encrypted

def client_program():
    host = "127.0.0.1"  
    port = 12345 

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    shift = 3  

    while True:
        message = input("Enter message to send to server: ")  

       
        encrypted_message = caesar_encrypt(message, shift)
        client_socket.send(encrypted_message.encode())  
        
        data = client_socket.recv(1024).decode()  
        print("Server:", data)

        if message.lower() == "exit":
            break  

    client_socket.close()  

if __name__ == '__main__':
    client_program()
