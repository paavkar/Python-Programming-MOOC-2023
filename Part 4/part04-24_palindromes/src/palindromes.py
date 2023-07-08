# Write your solution here
def palindromes(word: str):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
            print("that wasn't a palindrome")
            return False
    print(f"{word} is a palindrome!")
    return True

# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def main():
    condition = False
    while not condition:
        string = input("Please type in a palindrome: ")
        condition = palindromes(string)

main()

#if __name__ == "__main__":
    #condition = False
    #while not condition:
        #string = input("Please type in a palindrome: ")
        #condition = palindromes(string)