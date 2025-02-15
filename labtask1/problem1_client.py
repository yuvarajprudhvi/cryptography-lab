import socket

def client_program():
    host = "127.0.0.1" 
    port = 12345  

    client_socket = socket.socket()  
    client_socket.connect((host, port)) 

    while True:
        message = input("Enter message to send to server: ")  

        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode()  

        print("Server:", data)

        if message.lower() == "exit":
            break  

    client_socket.close() 

if __name__ == '__main__':
    client_program()
