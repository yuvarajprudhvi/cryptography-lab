import random
from sympy import isprime

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1


def rsa_keygen(p, q):
  
    n = p * q
    
    phi_n = (p - 1) * (q - 1)
    
    e = 65537 
    d = mod_inverse(e, phi_n)
   
    return ((n, e), (n, d))


def encrypt(message, public_key):
    n, e = public_key
    return pow(message, e, n)


def decrypt(ciphertext, private_key):
    n, d = private_key
    return pow(ciphertext, d, n)


if __name__ == "__main__":
    
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    
  
    if not isprime(p) or not isprime(q):
        print("Both p and q must be prime numbers.")
    else:
        print("Generating RSA keys...")
        public_key, private_key = rsa_keygen(p, q)
        
        print("\nPublic Key: (n, e) = ", public_key)
        print("Private Key: (n, d) = ", private_key)
        
     
        number = int(input("\nEnter a number to encrypt: "))
        ciphertext = encrypt(number, public_key)
        decrypted_number = decrypt(ciphertext, private_key)
        
        print(f"Encrypted number: {ciphertext}")
        print(f"Decrypted number: {decrypted_number}")
        
      
        letter = input("\nEnter a single alphabet letter to encrypt: ")
        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single alphabet letter.")
        else:
      
            letter_ascii = ord(letter.lower())  
            encrypted_letter = encrypt(letter_ascii, public_key)
            decrypted_letter_ascii = decrypt(encrypted_letter, private_key)
            decrypted_letter = chr(decrypted_letter_ascii)
            
            print(f"Encrypted letter: {encrypted_letter}")
            print(f"Decrypted letter: {decrypted_letter}")

