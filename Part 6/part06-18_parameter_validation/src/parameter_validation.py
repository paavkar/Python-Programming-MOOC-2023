# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError("Name is an empty string")
    elif name.find(" ") == -1:
        raise ValueError("Name doesn't contain two words")
    elif len(name) > 40:
        raise ValueError("Name too long")
    elif age < 0:
        raise ValueError("Age can't be negative")
    elif age > 150:
        raise ValueError("Age can't be over 150")
    return (name, age)