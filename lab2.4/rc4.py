# rc4.py
class RC4:
    def __init__(self, key):
        self.key = key
        self.S = list(range(256))  # Create the state vector (S)
        j = 0

        # Key-scheduling algorithm (KSA)
        for i in range(256):
            j = (j + self.S[i] + self.key[i % len(self.key)]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def encrypt(self, data):
        # The PRGA (Pseudo-Random Generation Algorithm)
        i = j = 0
        output = []

        for byte in data:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            output.append(byte ^ self.S[(self.S[i] + self.S[j]) % 256])

        return bytes(output)

    def decrypt(self, data):
        # RC4 encryption and decryption are symmetric
        return self.encrypt(data)
