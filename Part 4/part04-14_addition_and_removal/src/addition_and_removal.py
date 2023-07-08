# Write your solution here
list = []
while True:
    print(f"The list is now {list}")
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if(operation == "d"):
        list.append(len(list)+1)
    elif(operation == "r"):
        list.pop(-1)
    elif(operation == "x"):
        print("Bye!")
        break