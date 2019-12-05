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
    os.system('clear' or 'cls')
    custom_fig = Figlet(font='cyberlarge')
    print(custom_fig.renderText('Caesar Cipher'))
    print("version 1.0.0")
    print("by: @VulnHound")
    print("\n" * 3)


# Welcome Message


def welcome_message():
    """Function used to display welcome message and accept user input"""
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. BruteForce")
    print("\n0. Quit\n")
    selection = input("")
    return selection


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
    print("         python " + sys.argv[0] + " -b IHYAUBHAQ")
    sys.exit()


# Parse Arguments


def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.arg[0] + '-e [YOUR MESSAGE] -k [1-25]')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e', '--encrypt', action="store_true", help="Encrypts the message")
    group.add_argument('-d', '--decrypt', action="store_true", help="Decrypts the message")
    parser.add_argument('-k', '--key', help="Key used to encrypt/decrypt message", type=int, choices=[1, 2, 3, 4, 5, 6,
                                                                                                      7, 8, 9, 10, 11,
                                                                                                      12, 13, 14, 15,
                                                                                                      16, 17, 18, 19,
                                                                                                      20, 21, 22, 23,
                                                                                                      24, 25])
    group.add_argument('-b', '--brute', help="Brute force will use all keys for Caesar Cipher")
    parser.add_argument('-f', '--file', help="Input file to encrypt or decrypt")
    parser.add_argument('-o', '--outfile', help="Output file to print results out to")
    parser.add_argument('-h', '--help', help="Typing this gets you this pretty menu")
