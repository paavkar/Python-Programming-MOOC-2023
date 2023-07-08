# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for i in range(3):
        numbers.append(sudoku[row_no][column_no+i])
        numbers.append(sudoku[row_no+1][column_no+i])
        numbers.append(sudoku[row_no+2][column_no+i])
    for number in numbers:
        if(number > 0 and numbers.count(number) > 1):
            return False
    return True

### Example solution
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True