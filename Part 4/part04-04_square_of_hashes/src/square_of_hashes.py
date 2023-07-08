# Copy here code of line function from previous exercise
def line(length, string):
    i = 0
    s = ""
    while i < length:
        if(string == ""):
            s += "*"
            i += 1
        else:
            s += string[0]
            i += 1
    print(s)

def square_of_hashes(size):
    # You should call function line here with proper parameters
    width = 0
    height = 0
    while height < size:
        while width < size:
            line(size, "#")
            width += 1
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)
