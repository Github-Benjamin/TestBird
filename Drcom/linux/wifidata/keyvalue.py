import hashlib
import random

def keytoken(key_number):
    m2 = hashlib.md5()
    m2.update(key_number)
    key =  m2.hexdigest()
    return key

number = raw_input('Please input key_number: ')
key_number = number+'Benjamin'+number[5]+number[4]

print keytoken(key_number)