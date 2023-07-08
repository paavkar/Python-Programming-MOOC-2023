# write your solution here
def read_fruits():
    fruits = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "")
            fruit = line.split(";")
            fruits[fruit[0]] = float(fruit[1])
    return fruits