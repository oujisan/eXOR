import argparse
import sys

banner = r'''


'''

def xor_cipher(msg, key, hexkey=False):
    key = bytes.fromhex(key) if hexkey else key = key.encode('utf-8')
    xor = bytes(b ^ key[i % len(key)] for i, b in enumerate(msg))
    return xor

def encyrpt(msg, key):
    msg_bytes = msg.encode('utf-8')
    encrypted = xor_cipher(msg_bytes,key).hex()
    hex_key = key.encode('utf-8').hex()
    return encrypted,hex_key

def decrypt(msg,key, hexkey=False):
    msg_bytes = bytes.fromhex(msg)
    decrypted = xor_cipher(msg_bytes,key,hexkey=hexkey)
    return decrypted.decode('utf-8')

def transform_file(file, key, output, hexkey=False):
    with open(file,'rb') as document:
        data = document.read()
    mod = xor_cipher(msg=data,key=key,hexkey=hexkey)
    with open(output, 'wb') as mod_document:
        mod_document.write(mod)
        
def main():
    msg = 'HelloWorld'
    key = 'ouji'

if __name__ == '__main__':
    main()
