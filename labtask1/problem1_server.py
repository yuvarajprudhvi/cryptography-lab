import socket

def server_program():
 
    host = "127.0.0.1"  
    port = 12345  

    server_socket = socket.socket() 
    server_socket.bind((host, port))  

    server_socket.listen(1) 
    print(f"Server is listening on {host}:{port}...")
    
    conn, address = server_socket.accept() 
    print(f"Connection from {address}")

    while True:
      
        data = conn.recv(1024).decode()
        if not data:
            break 

        print("Received message:", data)
        response = "Server response: " + data
        conn.send(response.encode())  

    conn.close()  

if __name__ == '__main__':
    server_program()

