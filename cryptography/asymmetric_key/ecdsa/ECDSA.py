from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS

#use secp256k1 elliptical_curve 

key = ECC.generate(curve="P-256") 
public_key_file = "ecc.pub"
private_key_file = "ecc.pem" 

# Create public key
with open(public_key_file, "wt") as f:
    f.write(key.public_key().export_key(format="PEM"))

# Create private key  
with open(private_key_file, "wt") as f:
    f.write(key.export_key(format="PEM"))

#Sign the message 
msg = b"Hello World, Digital Signature"
key = ECC.import_key(open(private_key_file).read())
h = SHA256.new(msg)
signer = DSS.new(key, 'fips-186-3') 
signature = signer.sign(h)  

# Verification
h = SHA256.new(msg)
key = ECC.import_key(open(public_key_file).read())
verifier = DSS.new(key, 'fips-186-3')
try:
    verifier.verify(h, signature)
    print("The message is authentic.")  
except ValueError:
    print("The message is not authentic")
