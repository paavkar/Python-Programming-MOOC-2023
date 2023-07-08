# Write your solution here
def oldest_person(people: list):
    oldest = 0
    name = ""
    for person in people:
        if(2023 - person[1]) > oldest:
            oldest = 2023 - person[1]
            name = person[0]
    return name