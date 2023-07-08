# Write your solution here
import json
def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()
    people = json.loads(data)
    for person in people:
        if(len(person["hobbies"]) == 0):
            print(f"{person['name']} {person['age']} years ()")
        elif(len(person["hobbies"]) == 1):
            print(f"{person['name']} {person['age']} years ({person['hobbies'][0]})")
        elif(len(person["hobbies"]) == 2):
            print(f"{person['name']} {person['age']} years ({person['hobbies'][0]}, {person['hobbies'][1]})")
        elif(len(person["hobbies"]) == 3):
            print(f"{person['name']} {person['age']} years ({person['hobbies'][0]}, {person['hobbies'][1]}, {person['hobbies'][2]})")


### Example solution

import json
def print_persons(filename: str):
    with open(filename) as f:
        content = f.read()
    persons = json.loads(content)
    for person in persons:
        name = person['name']
        age = person['age']
        hobbies = ", ".join(person['hobbies'])
        print(f"{name} {age} years ({hobbies})")