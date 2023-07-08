# Write your solution here
def spruce(size):
    print("a spruce!")
    n = size
    row = "*"
    while n > 0:
        print(" " * (n - 1) + row)
        row += "**"
        n -= 1
    print(" " * (size - 1) + "*")
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)