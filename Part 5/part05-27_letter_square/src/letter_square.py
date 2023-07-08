# Write your solution here
layers = int(input("Layers: "))
letters = [chr(i) for i in range(65, 65+layers)]
    
size = layers*2 - 1
    
square = [['C' for i in range(size)] for j in range(size)]
    
for i in range(layers):
    for j in range(i, size-i):
        square[i][j] = letters[layers - i - 1]
        square[size-i-1][j] = letters[layers - i - 1]
        square[j][i] = letters[layers - i - 1]
        square[j][size-i-1] = letters[layers - i - 1]
    
for row in square:
    print("".join(row))


### Example solution

n = int(input("Layers: "))
 
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between
while k >= 1:
    left = left+alphabets[k]
    right = alphabets[k]+right
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1
while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1