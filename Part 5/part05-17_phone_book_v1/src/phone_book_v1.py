# Write your solution here
def add(phonebook):
    name = input("name: ")
    number = input("number: ")
    phonebook[name] = number
    print("ok!")

def search(phonebook):
    name = input("name: ")
    if(name in phonebook):
        print(phonebook[name])
    else:
        print("no number")

def main():
    phonebook = {}
    while True:
        command = input("command (1 search, 2 add, 3 quit)")
        if(command == "1"):
            search(phonebook)
        if(command == "2"):
            add(phonebook)
        if(command == "3"):
            print("quitting...")
            break

main()