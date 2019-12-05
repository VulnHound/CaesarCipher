caesar.py is a simple CLI script where you can encrypt, decrypt, and bruteforce crack 
caesar ciphers. 

# Installation
- git clone https://github.com/VulnHound/CaesarCipher.git
- cd CaesarCipher
- pip3 install -r requirements.txt

# Usage
- Encrypt
    - python caesar.py -e vulnhound -k 13
- Decrypt
    - python caesar.py -d IHYAUBHAQ -k 13
- Brute Force
    - python caesar.py -b IHYAUBHAQ
