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

def square(size, character):
    # You should call function line here with proper parameters
    width = 0
    height = 0
    while height < size:
        while width < size:
            line(size, character)
            width += 1
        height += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")