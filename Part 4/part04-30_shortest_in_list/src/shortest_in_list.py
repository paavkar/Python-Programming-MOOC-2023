# Write your solution here
def shortest(list):
    shortest = list[0]
    for item in list:
        if(len(item) < len(shortest)):
            shortest = item
    return shortest