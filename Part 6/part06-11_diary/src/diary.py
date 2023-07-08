# Write your solution here
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    cmd = int(input("Function: "))
    if(cmd == 1):
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as file:
            file.write(entry+"\n")
            print("Diary saved")
    elif(cmd == 2):
        with open("diary.txt") as file:
            lines = []
            for line in file:
                lines.append(line.strip())
            print("Entries:")
            for line in lines:
                print(line)
    elif(cmd == 0):
        print("Bye now!")
        break