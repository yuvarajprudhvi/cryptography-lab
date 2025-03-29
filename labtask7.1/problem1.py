import hashlib

def generate_hash(text):
    
    sha512_hash = hashlib.sha512()
    
   
    sha512_hash.update(text.encode())
    
   
    return sha512_hash.hexdigest()

if __name__ == "__main__":
   
    text = input("Enter the text to hash: ")
    
   
    hash_code = generate_hash(text)
    
   
    print(f"SHA-512 Hash: {hash_code}")
