import random

def generate_mapping():
    """
    Generate a random one-to-one mapping between the plain alphabet and a cipher alphabet.
    """
    plain_alphabet = list("abcdefghijklmnopqrstuvwxyz")
    cipher_alphabet = plain_alphabet.copy()
    random.shuffle(cipher_alphabet)
    return {plain: cipher for plain, cipher in zip(plain_alphabet, cipher_alphabet)}

def encrypt(plaintext, mapping):
    """
    Encrypt the plaintext using the provided one-to-one mapping.
    
    Args:
        plaintext (str): The text to encrypt.
        mapping (dict): The one-to-one mapping for the cipher.

    Returns:
        str: The ciphertext.
    """
    return "".join(mapping[char] for char in plaintext if char in mapping)

def main():
   
    mapping = generate_mapping()
    
   
    print("One-to-One Mapping:")
    for plain, cipher in sorted(mapping.items()):
        print(f"{plain} -> {cipher}")
    
   
    plaintext = "wewishtoreplaceplayer"
    print(f"\nPlaintext: {plaintext}")
    ciphertext = encrypt(plaintext, mapping)
    print(f"Ciphertext: {ciphertext}")


if __name__ == "__main__":
    main()

