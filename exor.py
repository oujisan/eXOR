#!/usr/bin/env python3

import argparse
import sys

banner = r'''
     __  _____  ___ 
  ___\ \/ / _ \| _ \
 / -_)>  < (_) |   /
 \___/_/\_\___/|_|_\

 by: oujisan        
'''

def xor_cipher(msg, key, hexkey=False):
    key = bytes.fromhex(key) if hexkey else key.encode('utf-8')
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
    try:
        parser = argparse.ArgumentParser(
            prog='eXOR',
            description='eXOR is a tool for XOR encryption and decryption of text and files using custom keys (string or hex).',
            usage='exor [OPTION] <"text" | file> [OPTION KEY] <key> [-o | --output (for files)]',
            epilog='Example: exor -e "HelloWorld" -k "oujisan" | exor -d file.png.enc -kh "6f756a6973616e"'
        )

        options_group = parser.add_mutually_exclusive_group(required=True)
        options_group.add_argument(
            '-e', '--encrypt',
            type=str,
            help='Encrypt text input. Example: -e "HelloWorld"'
        )
        options_group.add_argument(
            '-d', '--decrypt',
            type=str,
            help='Decrypt text input. Example: -d "EncryptedText"'
        )
        options_group.add_argument(
            '-ef', '--encryptfile',
            type=str,
            help='Encrypt a file. Example: -ef input.txt'
        )
        options_group.add_argument(
            '-df', '--decryptfile',
            type=str,
            help='Decrypt a file. Example: -df file.txt.enc'
        )

        key_name = parser.add_argument_group('Key Type')
        key_group = key_name.add_mutually_exclusive_group(required=True)
        key_group.add_argument(
            '-k', '--key',
            type=str,
            help='Key in plain text format. Example: -k "mysecretkey"'
        )
        key_group.add_argument(
            '-kh', '--keyhex',
            type=str,
            help='Key in hexadecimal format. Example: -kh "6d797365637265746b6579"'
        )

        parser.add_argument(
            '-o', '--output',
            type=str,
            help='Output file (only for file encryption/decryption). Example: -o output.txt'
        )

        if len(sys.argv) == 1:
            print(banner)
            parser.print_help()
            raise SystemExit
        
        args = parser.parse_args()

        if args.output and not (args.encryptfile or args.decryptfile):
            parser.error("--output can be used with --encryptfile or --decryptfile")
            raise SystemExit
        if (args.encrypt or args.encryptfile) and args.keyhex:
            parser.error("-kh or --keyhex can be used with --decrypt or --decryptfile")
            raise SystemExit
        
        switch = True if args.keyhex else False
        switch_key = args.keyhex if switch else args.key

        if args.encrypt:
            enc, hkey = encyrpt(msg=args.encrypt,key=args.keyhex if switch else args.key)
            display_key = f"Key:{bytes.fromhex(args.keyhex).decode('utf-8')}" if args.keyhex else f"Hex Key: {hkey}"
            print(f"{enc} ({display_key})")
        elif args.decrypt:
            dec = decrypt(msg=args.decrypt,key=switch_key,hexkey=switch)
            print(dec)
        elif args.encryptfile:
            print(f"encrypt file: '{args.encryptfile}' using key: '{args.key}'")
            try:
                transform_file(file=args.encryptfile,key=switch_key,output=args.output ,hexkey=switch)
                print(f"\nEncrypt completed! Output saved as '{args.output}'")
            except Exception as e:
                print(f"Error: {e}")
        elif args.decryptfile:
            print(f"Decrypt file: '{args.decryptfile}' using key: '{switch_key}'")
            try:
                transform_file(file=args.decryptfile,key=switch_key,output=args.output ,hexkey=switch)
                print(f"\nDecrypt completed! Output saved as '{args.output}'")
            except Exception as e:
                print(f"Error: {e}")
    except SystemExit:
        sys.exit(1)

if __name__ == '__main__':
    main()
