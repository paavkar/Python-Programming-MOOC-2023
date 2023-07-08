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

def triangle(size):
    # You should call function line here with proper parameters
    i = 0
    while i <= size:
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
