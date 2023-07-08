# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    avg1 = 0
    avg2 = 0
    avg3 = 0
    avg1 = (person1["result1"] + person1["result2"] + person1["result3"])/3
    avg2 = (person2["result1"] + person2["result2"] + person2["result3"])/3
    avg3 = (person3["result1"] + person3["result2"] + person3["result3"])/3
    lowest = avg1
    person = person1
    if(avg2 < lowest):
        lowest = avg2
        person = person2
    if(avg3 < lowest):
        lowest = avg2 
        person = person3
    return person


### Example solution
# Helper function for one average
def average(person: dict):
    ex_sum = person["result1"]+person["result2"]+person["result3"]
    return ex_sum/3
 
def smallest_average(person1: dict, person2: dict, person3: dict):
    smallest = person1
 
    if average(person2) < average(smallest):
        smallest = person2
 
    if average(person3) < average(smallest):
        smallest = person3
 
    return smallest