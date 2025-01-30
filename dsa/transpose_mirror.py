matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix[0])

for i in range(n):
    for j in range(n):
        print(matrix[i][j])

for i in range(n):
    for j in range(i+1,n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

print("Transpose + reflection")
for i in range(n):
    for j in range(n):
        print(matrix[i][j])