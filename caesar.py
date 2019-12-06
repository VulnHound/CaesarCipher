"""
Caesar Cipher
by: @VulnHound
version 1.0.1
Created: 11/10/2019
"""
from functions import *

parser = argparse.ArgumentParser(epilog='\tExample: \r\npython caesar.py ' + '-e [YOUR MESSAGE] -k [1-25]')
group = parser.add_mutually_exclusive_group()
group.add_argument("-e", "--encrypt", type=str, help="Encrypts the message")
group.add_argument("-d", "--decrypt", type=str, help="Decrypts the message")
parser.add_argument("-k", "--key", help="Key used to encrypt/decrypt message", type=int, choices=[1, 2, 3, 4, 5, 6,
                                                                                                  7, 8, 9, 10, 11,
                                                                                                  12, 13, 14, 15,
                                                                                                  16, 17, 18, 19,
                                                                                                  20, 21, 22, 23, 24,
                                                                                                  25])
group.add_argument('-b', '--brute', help="Brute force will use all keys for Caesar Cipher")
args = parser.parse_args()

if args.encrypt:
    banner()
    encrypt(args.encrypt, args.key)
elif args.decrypt:
    banner()
    decrypt(args.decrypt, args.key)
elif args.brute:
    banner()
    brute(args.brute)
else:
    parser_error()
    sys.exit()
