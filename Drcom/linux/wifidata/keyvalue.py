import hashlib

def keytoken(key_number):
    m2 = hashlib.md5()
    m2.update(key_number)
    key =  m2.hexdigest()
    return key

key_number = '482950'+'Benjamin'+'05'

print keytoken(key_number)