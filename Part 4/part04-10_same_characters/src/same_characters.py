# Write your solution here
def same_chars(string, index1, index2):
    if(index2 < (len(string)-1) and index1 < (len(string)-1)):
        if(string[index1] != string[index2]):
            return False
        else:
            return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("programmer", 0, 12))