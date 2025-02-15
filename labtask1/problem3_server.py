import socket


def create_playfair_matrix(key):
    matrix = []
    key = ''.join([char.upper() for char in key if char.isalpha()]).replace("J", "I")  
    seen = set()

  
    for char in key:
        if char not in seen:
            seen.add(char)
            matrix.append(char)

  
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, len(matrix), 5)]

def prepare_text(text):
    text = ''.join([char.upper() for char in text if char.isalpha()])
    text = text.replace("J", "I")
    if len(text) % 2 != 0:
        text += "X"
    return [text[i:i+2] for i in range(0, len(text), 2)]

def find_position(letter, matrix):
    for row in range(5):
        if letter in matrix[row]:
            return (row, matrix[row].index(letter))

def encrypt_pair(pair, matrix):
    (row1, col1) = find_position(pair[0], matrix)
    (row2, col2) = find_position(pair[1], matrix)
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(pair, matrix):
    (row1, col1) = find_position(pair[0], matrix)
    (row2, col2) = find_position(pair[1], matrix)
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_decrypt(text, key):
    matrix = create_playfair_matrix(key)
    decrypted_text = ""
    for pair in text:
        decrypted_text += decrypt_pair(pair, matrix)
    return decrypted_text


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 9999))
    server_socket.listen(5)
    print("Server is listening for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

       
        encrypted_message = client_socket.recv(1024).decode()
        print(f"Received encrypted message: {encrypted_message}")

       
        key = "MYKEY" 
        decrypted_message = playfair_decrypt([encrypted_message[i:i+2] for i in range(0, len(encrypted_message), 2)], key)
        print(f"Decrypted message: {decrypted_message}")

        
        client_socket.send(decrypted_message.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
