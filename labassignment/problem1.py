
import os
from py_ecc.bls.ciphersuites import G2ProofOfPossession as BLS

def main():
   
    client_keys = []
    for i in range(3):
        
        private_key = BLS.KeyGen(os.urandom(32))
        public_key = BLS.SkToPk(private_key)
        client_keys.append((private_key, public_key))
        print(f"Client {i+1} keys generated")
    
   
    print("\n")
    
   
    messages = [
        b"Message from client 1",
        b"Message from client 2",
        b"Message from client 3"
    ]
    
    
    signatures = []
    for i in range(3):
        private_key = client_keys[i][0]
        message = messages[i]
        signature = BLS.Sign(private_key, message)
        signatures.append(signature)
        print(f"Client {i+1} signed: {message.decode()}")
    
  
    print("\n")
    
   
    for i in range(3):
        public_key = client_keys[i][1]
        message = messages[i]
        signature = signatures[i]
        is_valid = BLS.Verify(public_key, message, signature)
        print(f"Client {i+1}'s signature valid: {is_valid}")
    
   
    print("\n")
    
   
    aggregate_signature = BLS.Aggregate(signatures)
    print("Created signature for all messages")
    
   
    print()
    
    
    public_keys = [keys[1] for keys in client_keys]
    
   
    is_valid = BLS.AggregateVerify(public_keys, messages, aggregate_signature)
    print(f"Signature verification: {is_valid}")
    
   
    print()
    
    
    same_message = b"We all agree to this document"
    same_message_signatures = []
    
    for i in range(3):
        private_key = client_keys[i][0]
        signature = BLS.Sign(private_key, same_message)
        same_message_signatures.append(signature)
    
    
    same_message_aggregate = BLS.Aggregate(same_message_signatures)
    
   
    same_message_valid = BLS.FastAggregateVerify(public_keys, same_message, same_message_aggregate)
    print(f"Same-message signature valid: {same_message_valid}")

if __name__ == "__main__":
    main()
