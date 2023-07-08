# Write your solution here:
from random import choices
def word_generator(characters: str, length: int, amount: int):
    s = ("".join(choices(characters, k=length)) for i in range(amount))
    return s

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)