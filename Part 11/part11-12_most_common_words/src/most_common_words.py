# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    helper = {}
    helper2 = []
    with open(filename) as file:
        for line in file:
            helper2.append(line.strip().split(" "))
    for list in helper2:
        for item in list:
            if("." in item or "," in item):
                item = item[:-1]
            if item not in helper:
                helper[item] = 1
            else:
                helper[item] += 1
    return {word: amount for word, amount in helper.items() if amount >= lower_limit}

## Example solution
from string import punctuation
 
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as f:
        content = f.read()
 
        # remove line breaks and punctuation
        content = content.replace("\n", " ")
        for punctuation_mark in punctuation:
            content = content.replace(punctuation_mark, "")
 
        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}