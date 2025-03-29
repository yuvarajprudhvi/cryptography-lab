from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import hashlib


def generate_dh_parameters():
    return dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())


def generate_dh_keys(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    return shared_key


def derive_aes_key(shared_key):
    salt = os.urandom(16)  
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    return kdf.derive(shared_key)

#
def encrypt_message(message, aes_key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + encrypted_message  


def decrypt_message(encrypted_message, aes_key):
    iv = encrypted_message[:16]
    cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_message = decryptor.update(encrypted_message[16:]) + decryptor.finalize()
    return decrypted_message.decode()

def compute_hash(message):
    return hashlib.sha512(message.encode()).hexdigest()

if __name__ == "__main__":
    
    parameters = generate_dh_parameters()

    
    private_key_a, public_key_a = generate_dh_keys(parameters)
    
    
    private_key_b, public_key_b = generate_dh_keys(parameters)

    
    shared_key_a = derive_shared_key(private_key_a, public_key_b)
    shared_key_b = derive_shared_key(private_key_b, public_key_a)

    
    assert shared_key_a == shared_key_b

    
    aes_key = derive_aes_key(shared_key_a)

  
    message = input("Enter the message to send: ")
    hash_code = compute_hash(message)
    combined_message = f"{message}||{hash_code}"
    encrypted_message = encrypt_message(combined_message, aes_key)

  
    received_message = encrypted_message  

   
    decrypted_message = decrypt_message(received_message, aes_key)
    original_message, received_hash_code = decrypted_message.split("||")

   
    if compute_hash(original_message) == received_hash_code:
        print("Integrity verified!")
    else:
        print("Integrity check failed!")

    
    print(f"Original message: {original_message}")
