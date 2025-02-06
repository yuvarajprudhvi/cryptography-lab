def generate_key_matrix(key):
   
    key = key.upper().replace("J", "I")  
    unique_chars = []
    for char in key:
        if char not in unique_chars and char.isalpha():  
            unique_chars.append(char)

   
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    for char in alphabet:
        if char not in unique_chars:
            unique_chars.append(char)

   
    key_matrix = [unique_chars[i:i + 5] for i in range(0, 25, 5)]
    return key_matrix


key = "srmapuniversity"
key_matrix = generate_key_matrix(key)


print("Key Matrix:")
for row in key_matrix:
    print(" ".join(row))
