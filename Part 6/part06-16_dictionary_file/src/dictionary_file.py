# Write your solution here
with open("dictionary.txt") as dictionary:
    words = {}
    for line in dictionary:
        words[line[:line.find(":")]] = line[line.find(":")+1:].strip()
    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        cmd = int(input("Function: "))
        if(cmd == 1):
            finnish = input("The word in Finnish: ")
            english = input("The word in English: ")
            words[finnish] = english
            with open("dictionary.txt", "a") as file:
                file.write(f"{finnish}: {english}\n")
            print("Dictionary entry added")
        elif(cmd == 2):
            search = input("Search term: ")
            for finnish, english in words.items():
                if(finnish.find(search) != -1 or english.find(search) != -1):
                    print(f"{finnish} - {english}")
        elif(cmd == 3):
            print("Bye!")
            break