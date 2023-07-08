# Copy here code of line function from previous exercise and use it in your solution
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

def shape(width, tchar, height, rchar):
    i = 0
    while i <= width:
        line(i, tchar)
        i += 1
    square_height = 0
    square_width = 0
    while square_width < width:
        while square_height < height:
            line(width, rchar)
            square_height += 1
        square_width += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "X", 3, "*")
    print()
    shape(5, "x", 2, "o")