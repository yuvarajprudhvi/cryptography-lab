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

def playfair_encrypt(text, key):
    matrix = create_playfair_matrix(key)
    text = prepare_text(text)
    encrypted_text = ""
    for pair in text:
        encrypted_text += encrypt_pair(pair, matrix)
    return encrypted_text


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 9999))

   
    message = input("Enter message to send to the server: ")
    key = "MYKEY" 
    encrypted_message = playfair_encrypt(message, key)

 
    client_socket.send(encrypted_message.encode())

 
    decrypted_message = client_socket.recv(1024).decode()
    print(f"Decrypted message from server: {decrypted_message}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
