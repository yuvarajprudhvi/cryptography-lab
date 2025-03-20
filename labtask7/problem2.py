from tinyec import registry
import secrets
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def compress(publicKey):
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]


def derive_shared_key(private_key, public_key):
    shared_point = private_key * public_key
    shared_key = hashlib.sha256(str(shared_point.x).encode()).digest()
    return shared_key


def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ct_bytes  


def decrypt_aes(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    ct = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()


curve = registry.get_curve('brainpoolP256r1')


Ka = secrets.randbelow(curve.field.n)  
X = Ka * curve.g  
print("Alice's public key X:", compress(X)) 


Kb = secrets.randbelow(curve.field.n) 
Y = Kb * curve.g  
print("Bob's public key Y:", compress(Y)) 


A_SharedKey = derive_shared_key(Ka, Y)
B_SharedKey = derive_shared_key(Kb, X)


print("Do both shared keys match?", A_SharedKey == B_SharedKey)


message = "Hell0 SRM AP"


encrypted_message = encrypt_aes(message, A_SharedKey[:16]) 
print(f"Encrypted message: {encrypted_message.hex()}")


decrypted_message = decrypt_aes(encrypted_message, A_SharedKey[:16])  
print(f"Decrypted message: {decrypted_message}")
