from tinyec import registry 
import secrets 

def compress(publicKey): 
    
    return hex(publicKey.x) + hex(publicKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1') 

Ka = secrets.randbelow(curve.field.n)  
X = Ka * curve.g  
print("Alice's public key X:", compress(X)) 

Kb = secrets.randbelow(curve.field.n) 
Y = Kb * curve.g  
print("Bob's public key Y:", compress(Y)) 

print("Currently exchanging public keys")


A_SharedKey = Ka * Y
print("Alice's shared key:", compress(A_SharedKey))


B_SharedKey = Kb * X
print("Bob's shared key:", compress(B_SharedKey))


print("Do both shared keys match?", A_SharedKey == B_SharedKey)
