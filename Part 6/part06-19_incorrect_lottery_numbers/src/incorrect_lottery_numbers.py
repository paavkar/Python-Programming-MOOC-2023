# Write your solution here
def filter_incorrect():
    open("correct_numbers.csv", "w").close()
    with open("lottery_numbers.csv") as file:
        for line in file:
            parts = line.strip().split(";")
            week_index = parts[0].find(" ")
            numbers = parts[1].split(",")
            week = parts[0][week_index+1:]
            try:
                error = False
                week = int(week)
                for number in numbers:
                    number = int(number)
                    if(number > 39 or number < 1 or numbers.count(str(number)) > 1):
                        error = True
                if(len(numbers) < 7):
                    error = True
            except ValueError:
                error = True
            if not error:
                with open("correct_numbers.csv", "a") as correct:
                    correct.write(line)

if __name__ == "__main__":
    filter_incorrect()