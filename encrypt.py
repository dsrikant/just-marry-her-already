 # -*- coding: utf-8 -*-
from Crypto.Cipher import Blowfish
import sys

INPUT_SIZE = 8

plaintext = sys.argv[1]
SSN_KEY = sys.argv[2]
 
def pad_string(str):
    new_str = str
    pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)
 
    if pad_chars != 0:
        for x in range(pad_chars):
            new_str += " "
                
    return new_str
 
crypt_obj = Blowfish.new(SSN_KEY, Blowfish.MODE_ECB)
ciphertext = crypt_obj.encrypt(pad_string(plaintext))

print "Key: " + SSN_KEY
print "Plaintext: " + plaintext
print "Blowfish Cyphertext: " + ciphertext.encode('hex')

