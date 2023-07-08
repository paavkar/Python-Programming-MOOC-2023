# write your solution here
if True:
    text = input("Write text: ")
else:
    text = "We use ptython to make a spell checker"
with open("wordlist.txt") as file:
    words = text.split(" ")
    parts = []
    for line in file:
        parts.append(line.strip())
    for i in range(len(words)):
        if(words[i].lower() not in parts):
            new = "*"+ words[i] + "*"
            words.remove(words[i])
            words.insert(i, new)
    new_text = ""
    for word in words:
        new_text = new_text + " " + word
    print(new_text.lstrip())

### Example solution
def wordlist():
    words = []
 
    with open("wordlist.txt") as file:
        for row in file:
            words.append(row.strip())
 
    return words
 
words = wordlist()
sentence = input("Write text: ")
 
for word in sentence.split(' '):
    if word.lower() in words:
        print(word + " ", end="")
    else:
        print("*" + word + "* ", end="")
 
print()