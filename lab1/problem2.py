def decrypt_caesar_cipher(ciphertext, key):
    decrypted_text = ""
    for char in ciphertext:
        if 'A' <= char <= 'Z':  
          
            new_char = chr(((ord(char) - ord('A') - key) % 26) + ord('A'))
        else:
          
            new_char = char
        decrypted_text += new_char
    return decrypted_text


ciphertext = "PHHW PH DIWHU WKH WRJD SDUWB"


for key in range(1, 26):
    decrypted_message = decrypt_caesar_cipher(ciphertext, key)
    print(f"Key {key}: {decrypted_message}")

