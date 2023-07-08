# Write your solution here
def list_sum(list1, list2):
    new = []
    i = 0
    while i < len(list1):
        new.append(list1[i] + list2[i])
        i += 1
    return new