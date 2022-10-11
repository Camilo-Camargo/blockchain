from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes 

# Create random key of 16 bits
with open("keys/aes16.key", "wb") as f:
    key = get_random_bytes(16) 
    f.write(key) 

# Encryption
data = "Hello World, for AES encryption." 
cipher = AES.new(key,AES.MODE_EAX)

cipher_text, tag =  cipher.encrypt_and_digest(data.encode()) 

with open("encrypt/aes_msg.bin", "wb") as f:
    for x in (cipher.nonce, tag, cipher_text):
        f.write(x)

print("Msg encrypted and stored in file.") 

## Decryption
### Read the key first
with open("keys/aes16.key", "rb") as f:
    key = f.read(16)
### Read the binary 
with open("encrypt/aes_msg.bin", "rb") as f:
    nonce, tag, cipher_text = [f.read(x) for x in (16,16,-1)]

cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(cipher_text, tag) 
print(data)
with open("decrypt/aes_msg.txt", "wb") as f:
    f.write(data)


