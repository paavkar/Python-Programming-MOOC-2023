# Write your solution here
def length_of_longest(list):
    longest = ""
    for item in list:
        if(len(item) > len(longest)):
            longest = item
    return len(longest)