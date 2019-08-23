"""
Mad Cipher
by: @VulnHound
version: 0.1.0
Date: 8/22/2019
"""

from pycipher import *
from pyfiglet import Figlet
import os

# Caesar Cipher Banner


def banner():
    os.system('clear' or 'cls')
    custom_fig = Figlet(font='cyberlarge')
    print(custom_fig.renderText('Caesar Cipher'))
    print("version 0.1.0")
    print("by: @VulnHound")
    print("\n" * 8)


# User Selection Function


def welcome_message():
    print("\n1. Encrypt")
    print("2. Decrypt\n")
    print("\n0. Quit\n")
    selection = input("")
    return selection


# Print out the banner message

banner()
userSelection = welcome_message()

while userSelection.lower() != "0":

    # If selection for user input

    if userSelection == "1":
        plain = input("\nEnter in plain text to encrypt: ")
        key = int(input("Enter a key value between [1-25]: "))

        ciphertext = Caesar(key).encipher(plain)

        banner()
        print("\n" + "-" * 30)
        print(ciphertext)
        print("-" * 30)
        userSelection = welcome_message()

    elif userSelection == "2":
        crypt = input("\nEnter in text to decrypt: ")
        key = int(input("Enter in the key value [1-25]: "))

        plaintext = Caesar(key).decipher(crypt)

        banner()
        print("\n" + "-" * 30)
        print(plaintext)
        print("-" * 30)
        userSelection = welcome_message()

    elif userSelection == "0":
        os.system('clear' or 'cls')
        exit()

    else:
        banner()
        print("\nBad selection...try again.\n")
        userSelection = welcome_message()


