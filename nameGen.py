import string 
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

def map1(y):
  h = 0
  inc = 97
  while h < 96:
      if h == y:
          return inc
      else:
          inc+=1
          h+=1
      if inc == 123:
          inc = 97

def map2(y):
    h = 0
    inc = 97
    while h < 256:
        if h == y:
            return inc
        else:
            inc+=1
            h+=1
        if inc == 123:
            inc = 97


plaintext = "SrikantWeller"
crypt_obj = Blowfish.new(SSN_KEY, Blowfish.MODE_ECB)
ciphertext = crypt_obj.encrypt(pad_string(plaintext))

var = ":".join("{:02x}".format(ord(c)) for c in ciphertext)
print "Var : " + var

ohye = var.split(":")

new = []

alph = list(string.ascii_lowercase)

for i in ohye:
    j = int(i, 16)
    print j
    new.append(j)

name = []

for y in new:
    if y < 97:
        name.append(map1(y))
    elif y > 122:
        name.append(map2(y))
    else:
        name.append(y)

for helo in name:
    print str(unichr(helo))

name = []

print "Plaintext: " + plaintext
print "Blowfish Cyphertext: " + ciphertext.encode('hex')
print "Back to Plaintext: " + crypt_obj.decrypt(ciphertext)

