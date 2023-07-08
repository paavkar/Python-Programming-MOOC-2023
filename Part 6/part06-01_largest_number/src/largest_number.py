# write your solution here
def largest():
    
    largest = 0
    with open("numbers.txt") as new_file:

        for line in new_file:
            #line = line.replace("\n", "")
            if(int(line) > largest):
                largest = int(line)
    return largest
