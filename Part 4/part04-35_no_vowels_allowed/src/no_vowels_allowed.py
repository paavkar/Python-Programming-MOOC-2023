# Write your solution here
def no_vowels(string: str):
    new_string = string
    for char in string:
        if(char in ["a", "e", "i", "o", "u"]):
            new_string = new_string.replace(char, "")
    return new_string