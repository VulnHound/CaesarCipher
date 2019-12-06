"""
File to store all of the used functions in Caesar Cipher
"""

from pycipher import *
from pyfiglet import Figlet
import os
import sys
import argparse

# Banner Message


def banner():
    """Function used to display banner"""
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
    custom_fig = Figlet(font='cyberlarge')
    print(custom_fig.renderText('Caesar Cipher'))
    print("version 1.0.1")
    print("by: @VulnHound")
    print("\n" * 3)


# Encryption Function


def encrypt(plain, key):
    """Function used to encrypt message"""
    ciphertext = Caesar(key).encipher(plain)
    banner()
    print("\n" + "-" * 30)
    print(ciphertext)
    print("-" * 30)


# Decryption Function


def decrypt(crypt, key):
    """Function used to decrypt message"""
    plaintext = Caesar(key).decipher(crypt)
    banner()
    print("\n" + "-" * 30)
    print(plaintext)
    print("-" * 30)

    
# Bruteforce Function    
    

def brute(crypt):
    """Function to brute-force decryption"""
    banner()
    print("\n" + "-" * 30 + '\n')
    for key in range(1, 26):
        plaintext = Caesar(key).decipher(crypt)
        print(plaintext + " " * 14 + '|' + '\n')

    print("-" * 30)


# Parse Error


def parser_error():
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] 'use -h for help' ")
    print("-" * 50 + "\n")
    print("Example: python " + sys.argv[0] + " -e vulnhound -k 13")
    print("         python " + sys.argv[0] + " -d IHYAUBHAQ -k 13")
    print("         python " + sys.argv[0] + " -b IHYAUBHAQ\n")
    sys.exit()

