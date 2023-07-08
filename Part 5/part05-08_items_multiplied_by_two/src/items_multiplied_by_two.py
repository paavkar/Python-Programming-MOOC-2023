# Write your solution here
def double_items(numbers: list):
    new = []
    for item in numbers:
        new.append(item*2)
    return new

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)


### Example solution
def double_items(numbers: list):
    double = numbers[:]
    for i in range(len(double)):
        double[i] *= 2
    
    return double