# Kelby Hubbard
# Started: 2022-02-13
# Updated: 
# generate.py
#
# Password generator script

import string
import random

def random_password(lower, upper, symbol, length):
    characters = []
    if (lower == True):
        characters += list(string.ascii_lowercase)
    if (upper == True):
        characters += list(string.ascii_uppercase)
    if (symbol == True):
        characters += list("~`! @#$%^&*()_-+={[}]|\:;\"'<,>.?/")

    # Shuffle all characters
    random.shuffle(characters)

    # Add random characters to password
    passwordList = []
    for i in range (length):
        passwordList.append(random.choice(characters))
    
    # Shuffle password again
    random.shuffle(passwordList)
    
    password = ''.join(passwordList)
    
    return password