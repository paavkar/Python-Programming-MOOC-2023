# Write your solution here
def invert(dictionary: dict):
    spare = {}
    for key, value in dictionary.items():
        spare[value] = key
    dictionary.clear()
    for key, value in spare.items():
        dictionary[key] = value