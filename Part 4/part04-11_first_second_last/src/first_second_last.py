# Write your solution here
def last_word(sentence):
    while sentence.find(" ") != -1:
        index = sentence.find(" ")
        sentence = sentence[index+1:]
    return sentence

def second_word(sentence):
    index = sentence.find(" ")
    sentence = sentence[index+1:]
    index = sentence.find(" ")
    if(index == -1):
        sentence += " "
    return sentence[:index]

def first_word(sentence):
    index = sentence.find(" ")
    return sentence[:index]
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))