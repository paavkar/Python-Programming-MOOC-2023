# Write your solution here
def greatest_number(x, y, z):
    greatest = x
    if(y > greatest):
        greatest = y
    if(z > greatest):
        greatest = z
    return greatest
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(3, 5, 8)
    print(greatest)