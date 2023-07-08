# Write your solution here
from random import randint
from string import ascii_lowercase
def generate_password(length: int):
    password = ""
    for i in range(length):
        password += ascii_lowercase[randint(0, len(ascii_lowercase)-1)]
    return password

### Example solution

from random import choice
from string import ascii_lowercase
 
def generate_password(length: int):
    passwd = ""
    for i in range(length):
        passwd += choice(ascii_lowercase)
 
    return passwd
 