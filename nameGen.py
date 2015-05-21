 # -*- coding: utf-8 -*-
from Crypto.Cipher import Blowfish
INPUT_SIZE = 8
SSN_KEY = '123456789987654321'
 
def pad_string(str):
    new_str = str
    pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)
 
    if pad_chars != 0:
        for x in range(pad_chars):
            new_str += " "
                
    return new_str
 
plaintext = "DushyantSrikant"
crypt_obj = Blowfish.new(SSN_KEY, Blowfish.MODE_ECB)
ciphertext = crypt_obj.encrypt(pad_string(plaintext))

var = ":".join("{:02x}".format(ord(c)) for c in ciphertext)
print var

ohye = var.split(":")

for i in ohye:
    print int(i, 16)
    

print "Plaintext: " + plaintext
print "Blowfish Cyphertext: " + ciphertext.encode('hex')
print "Back to Plaintext: " + crypt_obj.decrypt(ciphertext)

