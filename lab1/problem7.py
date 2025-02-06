def preprocess_text(text):
   
    text = text.upper().replace("J", "I").replace(" ", "")
    processed = ""
    i = 0
    while i < len(text):
        processed += text[i]
        
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed += "X"
        elif i + 1 >= len(text) and len(processed) % 2 == 1:
            processed += "X"
        i += 1
    return processed


def find_position(matrix, char):
   
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None


def encrypt_pair(pair, matrix):
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:  
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2: 
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]


def encrypt_playfair(plaintext, matrix):
    
    ciphertext = ""
    plaintext_pairs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    for pair in plaintext_pairs:
        ciphertext += encrypt_pair(pair, matrix)
    return ciphertext


def generate_playfair_key_matrix(key):
    
    key = key.upper().replace("J", "I")  
    unique_key = []
    for char in key:
        if char not in unique_key and char.isalpha():  
            unique_key.append(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in unique_key:
            unique_key.append(char)
    
    return [unique_key[i:i + 5] for i in range(0, 25, 5)]



key = "srmapuniversity"
plaintext = "wearediscoveredsaveyourself"


key_matrix = generate_playfair_key_matrix(key)


processed_plaintext = preprocess_text(plaintext)


ciphertext = encrypt_playfair(processed_plaintext, key_matrix)

# Display the key matrix and ciphertext
print("Key Matrix:")
for row in key_matrix:
    print(" ".join(row))

print("\nCiphertext:", ciphertext)
