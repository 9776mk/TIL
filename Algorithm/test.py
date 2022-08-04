from pprint import pprint

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

n = 3

left_matrix = [[0] * n for I in range(n)]
right_matrix = [[0] * n for I in range(n)]


for i in range(n):
    for j in range(n):
        left_matrix[i][j] = matrix[j][n-i-1]

for i in range(n):
    for j in range(n):
        right_matrix[i][j] = matrix[n-j-1][i]


pprint(left_matrix)
pprint(right_matrix)