# Write your solution here
def distinct_numbers(list):
    new = []
    for value in list:
        if(value not in new):
            new.append(value)
    new = sorted(new)
    return new