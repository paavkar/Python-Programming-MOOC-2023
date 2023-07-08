# Write your solution here
from string import ascii_letters, punctuation
def separate_characters(my_string: str):
    ascii = ""
    punct = ""
    other = ""
    for char in my_string:
        if char in ascii_letters:
            ascii += char
        elif(char in punctuation):
            punct += char
        else:
            other += char
    return (ascii, punct, other)