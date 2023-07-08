# Write your solution here
numbers = []
while True:
    number = int(input("New item: "))
    if(number == 0):
        break
    numbers.append(number)
    print(f"The list now: {numbers}")
    sorted_list = sorted(numbers)
    print(f"The list in order: {sorted_list}")
print("Bye!")