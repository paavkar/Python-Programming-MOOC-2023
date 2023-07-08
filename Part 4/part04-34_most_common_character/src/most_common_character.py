# Write your solution here
def most_common_character(string: str):
    most_common = ""
    count = 0
    for char in string:
        if(string.count(char) > count):
            count = string.count(char)
            most_common = char
    return most_common