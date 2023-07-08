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

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    return True

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

def sudoku_grid_correct(sudoku: list):
    boolean = False
    for i in range(9):
        if (row_correct(sudoku, i) and column_correct(sudoku, i)):
            boolean = True
        else:
            return False
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            if(block_correct(sudoku, row, column)):
                boolean = True
            else:
                return False
    return boolean

if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_grid_correct(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))

    sudoku3 = [
    [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
    [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
    [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
    [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
    [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
    [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
    [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
    [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
    [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],
    ]
    print(sudoku_grid_correct(sudoku3))