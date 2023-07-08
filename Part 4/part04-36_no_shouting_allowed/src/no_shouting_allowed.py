# Write your solution here
def no_shouting(strings: list):
    result = []
    for item in strings:
        if(not item.isupper()):
            result.append(item)
    return result