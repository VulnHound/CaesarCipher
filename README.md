caesar.py is a simple CLI script where you can encrypt, decrypt, and bruteforce crack 
caesar ciphers. 

# Installation
``git clone https://github.com/VulnHound/CaesarCipher.git``

``cd CaesarCipher``

``pip3 install -r requirements.txt``

# Usage
- Encrypt:
    
    ``python caesar.py -e vulnhound -k 13``
- Decrypt:
    
    ``python caesar.py -d IHYAUBHAQ -k 13``
- Brute Force:
    
    ``python caesar.py -b IHYAUBHAQ``


* If Python 3 is not your default interpreter then use: 

    ``python3 caesar.py -e vulnhound -k 13``

# Notes
- For multiple word strings use [BACKSLASH] instead of [SPACES]

Example:

    python caesar.py -e I\love\cryptography -k 23
    
- The -k, --key argument will only accept key numbers 1-25 due to the 
    function of the Caesar cipher itself
