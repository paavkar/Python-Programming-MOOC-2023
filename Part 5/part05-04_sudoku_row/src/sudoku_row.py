# Write your solution here
def row_correct(sudoku: list, row_no: int):
    boolean = True
    for i in range(len(sudoku[row_no])):
        if(boolean):
            if(sudoku[row_no][i] != 0 and sudoku[row_no].count(sudoku[row_no][i]) <= 1):
                boolean = True
            elif(sudoku[row_no][i] == 0):
                continue
            else:
                boolean = False
                return False
    return boolean

### Example solution
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True