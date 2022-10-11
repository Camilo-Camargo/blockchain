from Crypto.Hash import SHA256 

hash_obj =  SHA256.new(data=b"Hello World")
print(hash_obj.hexdigest()) 
print(hash("Hello"))
