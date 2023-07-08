# Write your solution here
from random import choice
from string import ascii_lowercase, digits
def generate_strong_password(length: int, number: bool, special: bool):
    spec_chars = "!?=+-()#"
    password = ""
    for i in range(length-1):
        if(number and special):
            password += choice(digits+spec_chars)
        elif(number):
            password += choice(digits)
        elif(special):
            password += choice(spec_chars)
        else:
            password += choice(ascii_lowercase)
    password += choice(ascii_lowercase)
    return password

#for i in range(10):
    #print(generate_strong_password(8, True, True))

### Example solution

from random import choice, randint
from string import ascii_lowercase, digits
 
def generate_strong_password(length: int, numbers: bool, special_characters: bool):
    special_chars = "!?=+-()#"
    # One letter at beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase
 
    # If numbers is wanted, add at least one number
    if numbers:
        passwd = add_character(passwd, digits)
        choice_set += digits
 
    # same for special characters
    if special_characters:
        passwd = add_character(passwd, special_chars)
        choice_set += special_chars
 
    # build the rest of the password from the whole set
    while (len(passwd) < length):
        passwd = add_character(passwd, choice_set)
 
    return passwd
 
# Add a random character from the given set either
# at the beginning or end of the string
def add_character(passwd: str, characters):
    character = choice(characters)
    if randint(1,2) == 1:
        return character + passwd
    else:
        return passwd + character