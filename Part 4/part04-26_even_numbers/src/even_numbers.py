# Write your solution here
def even_numbers(list):
    new = []
    for value in list:
        if (value % 2 == 0):
            new.append(value)
    return new