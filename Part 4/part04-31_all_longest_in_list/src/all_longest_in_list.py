# Write your solution here
def all_the_longest(list):
    new = []
    longest = ""
    for item in list:
        if(len(item) >= len(longest)):
            longest = item
    for item in list:
        if(len(item) >= len(longest)):
            new.append(item)
    return new