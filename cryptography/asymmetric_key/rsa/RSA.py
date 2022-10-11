from Crypto.PublicKey import RSA 
from Crypto.Cipher import PKCS1_OAEP 


## Encryption (public key)

msg = "Hello World, Asymmetric-key" 
#Create Private key 
private_key = RSA.generate(2048)
#Create Public key  
public_key  = private_key.publickey()

path = "asymmetric_key/rsa/"
public_key_file = path + "key.pem"
with open(public_key_file, "wb") as f:
    f.write(public_key.export_key("PEM"))

#Create cipher
cipher      = PKCS1_OAEP.new(public_key)
cipher_text = cipher.encrypt(msg.encode())
print("Data is Encrypted") 

## Decryption (private key) 
cipher = PKCS1_OAEP.new(private_key)
msg = cipher.decrypt(cipher_text)
print(f"{msg}")



