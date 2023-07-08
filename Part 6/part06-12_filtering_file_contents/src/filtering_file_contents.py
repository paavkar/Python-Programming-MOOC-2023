# Write your solution here
def filter_solutions():
    open('correct.csv', 'w').close()
    open('incorrect.csv', 'w').close()
    with open("solutions.csv") as file:
        for line in file:
            index = line.find(";")
            name = line[:index]
            line = line[index+1:]
            index = line.find(";")
            result = line[index+1:].strip()
            line = line[:index]
            if(eval(line) == int(result)):
                with open("correct.csv", "a") as correct:
                    correct.write(f"{name};{line};{result}\n")
            else:
                with open("incorrect.csv", "a") as incorrect:
                    incorrect.write(f"{name};{line};{result}\n")


### Example solution
 
def filter_solutions():
    # Open all lines
    with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
        for row in source:
            # Split into pieces
            pieces = row.split(";")
 
            calculation = pieces[1]
            result = pieces[2]
 
            # Addition or subtraction?
            if "+" in calculation:
                operands = calculation.split("+")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) + int(operands[1]) == int(result)
            else:
                operands = calculation.split("-")
                # correct is True or False based on whether the calculation was correct or not
                correct = int(operands[0]) - int(operands[1]) == int(result)
 
            # Write to file
            if correct:
                correct_file.write(row)
            else:
                incorrect_file.write(row)