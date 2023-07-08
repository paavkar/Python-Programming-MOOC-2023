# Write your solution here
def print_sudoku(sudoku: list):
    for j in range(9):
        print()
        if(j == 3 or j == 6):
            print()
        for i in range(9):
            
            if(i == 3 or i == 6):
                print(" ", end="")
            if (sudoku[j][i] == 0):
                print("_ ", end="")
            else:
                print(sudoku[j][i], "", end="")
        
    print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy_sudoku = []
    for row in sudoku:
        copy_sudoku.append(row[:])
    copy_sudoku[row_no][column_no] = number
    return copy_sudoku

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)