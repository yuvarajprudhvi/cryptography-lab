def decrypt(cipher_text, mapping):
  
    reverse_mapping = {v: k for k, v in mapping.items()}
    
   
    plain_text = ''.join(reverse_mapping[char] for char in cipher_text)
    return plain_text


mapping = {
    'A': 'A', 'B': 'N', 'C': 'D', 'D': 'R', 'E': 'E', 'F': 'W',
    'G': 'I', 'H': 'C', 'I': 'K', 'J': 'S', 'K': 'O', 'L': 'H',
    'M': 'T', 'N': 'B', 'O': 'F', 'P': 'G', 'Q': 'J', 'R': 'L',
    'S': 'M', 'T': 'P', 'U': 'Q', 'V': 'U', 'W': 'V', 'X': 'X',
    'Y': 'Y', 'Z': 'Z'
}


cipher_text = "SEEMSEAOMEDSAMHL"


plain_text = decrypt(cipher_text, mapping)
print("Decrypted message:", plain_text)
