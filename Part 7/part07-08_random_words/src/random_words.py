# Write your solution here
from random import choice
def words(n: int, beginning: str):
    words_found = []
    words_in_file = []
    words_starting = []
    with open("words.txt") as file:
        for line in file:
            words_in_file.append(line.strip())
    for word in words_in_file:
        if(word.startswith(beginning)):
            words_starting.append(word)
    while len(words_found) < n:
        if(n > len(words_starting)):
            raise ValueError
        word = choice(words_in_file)
        if (word.startswith(beginning) and word not in words_found):
            words_found.append(word)
    if(len(words_found) == 0):
        raise ValueError
    return words_found


### Example Solution
import random
 
def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
    return random.sample(word_list, n)
# Write your solution here