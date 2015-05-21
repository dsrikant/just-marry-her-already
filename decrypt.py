 # -*- coding: utf-8 -*-
from Crypto.Cipher import Blowfish
import sys

SSN_KEY = sys.argv[2]
ciphertext = sys.argv[1]

crypt_obj = Blowfish.new(SSN_KEY, Blowfish.MODE_ECB)

print "Back to Plaintext: " + crypt_obj.decrypt(ciphertext.decode('hex'))
