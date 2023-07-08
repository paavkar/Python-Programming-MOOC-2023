# Write your solution here
def older_people(people: list, year: int):
    older_than = []
    for person in people:
        if(person[1] < year):
            older_than.append(person[0])
    return older_than