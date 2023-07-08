# Write your solution here
def sum_of_positives(list):
    sum = 0
    for value in list:
        if(value > 0):
            sum += value
    return sum