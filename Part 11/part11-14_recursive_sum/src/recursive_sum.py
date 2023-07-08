# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    if number <= 1:
        return number
    return recursive_sum(number - 1) + number