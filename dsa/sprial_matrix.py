matrix = [[1,2,3],[4,5,6],[7,8,9]]

height = len(matrix)
length = len(matrix[0])

right_wall = length
up_wall = 0
left_wall = -1
down_wall = height
max_elements = height * length
right, down, left, up = 1, 2, 3, 4
itr = 0
output = []
i = 0
j = 0
direction = right
while len(output) != max_elements:
    if direction == right:
        while j < right_wall:
            output.append(matrix[i][j])
            j += 1
        i, j = i+1, j-1
        right_wall -= 1
        direction = down
    elif direction == down:
        while i < down_wall:
            output.append(matrix[i][j])
            i += 1
        i, j = i-1, j-1
        down_wall -= 1
        direction = left
    elif direction == left:
        while j > left_wall:
            output.append(matrix[i][j])
            j -= 1
        i, j = i-1, j+1
        left_wall += 1
        direction = up
    else:
        while i > up_wall:
            output.append(matrix[i][j])
            i -= 1
        i, j = i+1, j+1
        up_wall += 1
        direction = right

for m in range(height):
    for n in range(length):
        print(output[m][n])