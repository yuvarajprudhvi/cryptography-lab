from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii


def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)  
    encrypted_text = cipher.encrypt(padded_text)
    return encrypted_text

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher.decrypt(ciphertext)
    decrypted_text = unpad(decrypted_padded, DES.block_size)  
    return decrypted_text.decode()


if __name__ == "__main__":  
    key = b'8bytekey'  
    plaintext = "Thanks for connecting!"  

    print("Original Plaintext:", plaintext)

   
    encrypted = des_encrypt(plaintext, key)
    print("Encrypted Text (Hex):", binascii.hexlify(encrypted).decode())

   
    decrypted = des_decrypt(encrypted, key)
    print("Decrypted Plaintext:", decrypted)

