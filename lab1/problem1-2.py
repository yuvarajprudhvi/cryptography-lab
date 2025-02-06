def encrypt(text, key):
    encrypted_text = ""
    for char in text:
       
        if 'a' <= char <= 'z':
            
            new_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
        else:
          
            new_char = char
        encrypted_text += new_char
    return encrypted_text


input_text = "computerscienceengineeringsrmuniversity"


key = 4


encrypted_output = encrypt(input_text, key)


print(f"Encrypted text: {encrypted_output}")

