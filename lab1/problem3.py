
def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():  
            shift = ord(key[key_index % len(key)]) - ord('a') 
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
            key_index += 1
        else:
            ciphertext += char  
    return ciphertext


def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha(): 
            shift = ord(key[key_index % len(key)]) - ord('a')  
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char  
    return plaintext


keyword = "deceptivedeceptivedeceptive"
plaintext = "wearediscoveredsaveyourself"


ciphertext = vigenere_encrypt(plaintext, keyword)
print("Encrypted text:", ciphertext)


decrypted_text = vigenere_decrypt(ciphertext, keyword)
print("Decrypted text:", decrypted_text)

