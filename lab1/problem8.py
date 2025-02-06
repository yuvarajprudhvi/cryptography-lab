def find_position(matrix, char):
   
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char or (char in "IJ" and matrix[row][col] in "IJ"):
                return row, col
    return None, None

def generate_playfair_key_matrix(key):
   
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    key = key.upper().replace("J", "I")  
    unique_key = []
    
    for char in key:
        if char not in unique_key and char in alphabet:
            unique_key.append(char)
    
    for char in alphabet:
        if char not in unique_key:
            unique_key.append(char)
    
   
    matrix = [unique_key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def decrypt_pair(pair, matrix):
  
    row1, col1 = find_position(matrix, pair[0])
    row2, col2 = find_position(matrix, pair[1])

    if row1 == row2:  
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_playfair(ciphertext, matrix):
    
    plaintext = ""
    ciphertext_pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    for pair in ciphertext_pairs:
        plaintext += decrypt_pair(pair, matrix)
    return plaintext


key = "srmapuniversity"
ciphertext = "LIIUDLTQNSLIZETQVTPKZEZFVBVZ"


key_matrix = generate_playfair_key_matrix(key)


decrypted_plaintext = decrypt_playfair(ciphertext, key_matrix)


print("Key Matrix:")
for row in key_matrix:
    print(" ".join(row))

print("\nDecrypted Plaintext:", decrypted_plaintext)
