# write your solution here
def matrix_sum():
    sum = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for i in range(len(numbers)):
                sum += int(numbers[i])
    return sum

def matrix_max():
    max = 0
    with open("matrix.txt") as file:
        for line in file:
            line = line.replace("\n", "")
            numbers = line.split(",")
            for i in range(len(numbers)):
                if(int(numbers[i]) > max):
                    max = int(numbers[i])
    return max

def row_sums():
    sums = []
    with open("matrix.txt") as file:
        for line in file:
            sum = 0
            line = line.replace("\n", "")
            numbers = line.split(",")
            for i in range(len(numbers)):
                sum += int(numbers[i])
            sums.append(sum)
    return sums

### Example solution 

def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
# Yhdistää matriisin rivit yhdeksi listaksi
def combine(matriisi: list):
    mlist = []
    for row in matriisi:
        mlist += row
    
    return mlist
 
def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)
 
def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)
 
def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums
        