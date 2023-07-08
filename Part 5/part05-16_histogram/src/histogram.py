# Write your solution here
def histogram(string: str):
    result = {}
    for char in string:
        if char not in result:
            result[char] = 0
        result[char] += 1
    for key, value in result.items():
        print(key, "*" * value)