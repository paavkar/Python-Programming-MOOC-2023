# Write your solution here
def everything_reversed(my_list: list):
    result = []
    for item in my_list:
        result.append(item[::-1])
    return result[::-1]