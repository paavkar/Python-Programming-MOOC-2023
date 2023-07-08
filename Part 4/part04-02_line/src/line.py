# Write your solution here
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
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")