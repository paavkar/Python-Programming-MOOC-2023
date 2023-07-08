# Write your solution here
def transpose(matrix: list):
    copy_matrix = []
    for row in matrix:
        copy_matrix.append(row[:])
    for row in range(len(matrix)):
        for number in range(len(matrix)):
            matrix[row][number] = copy_matrix[number][row]
