import hashlib
import os
 
#https://www.askpython.com/python/examples/storing-retrieving-passwords-securely
 
PEPPER = 'h1pZ20z4'
def create_secure_password(password):
  salt = os.urandom(16)  
  iterations = 100_000
  hash_value = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8') + PEPPER.encode('utf-8'),  
        salt,
        iterations
  )  
  password_hash = salt + hash_value
  return password_hash 
 
 
print(create_secure_password("HelloWorld"))
#print(hash_password("HelloWorld"))