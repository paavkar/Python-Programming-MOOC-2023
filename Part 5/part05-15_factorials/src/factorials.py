# Write your solution here
def factorials(n: int):
    dictionary = {}
    for i in range(1, n+1):
        dictionary[i] = 1
        for j in range(1, i+1):
            dictionary[i] *= j
    return dictionary