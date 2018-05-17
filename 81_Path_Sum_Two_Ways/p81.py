# https://projecteuler.net/problem=81
# Idea: Recursive Dynamic Programming
# Consider an arrangement of cells such as:
#       i,j   |   i+1,j
#       i,j+1 |   i+1,j+1
# From cell (i,j) we can go down to (i,j+1) or right (i+1,j). If those cells contained the minimal path sum from each
# of them to the goal, then we could simply choose to go to cell containing the smaller value.
# In the bottom row and right column of the matrix there are no choices to make. So the minimal path sum from one of
# those cells to the goal is the sum of uniquely determined entries along its one and only path.
#
# Following the above operation, the minimal path sum from cell (goal-1, goal-1) to (goal, goal) is simply
# min( (goal-1,goal), (goal,goal-1) ).
# Similarly we can iterate outward from that cell and populate the entire matrix with the minimal path sum from each
# cell to the goal. The answer will then be the upper left entry of the matrix

matrix = []

with open("p081_matrix.txt", 'r') as grid:
    for line in grid:
        row = line.split(',')
        row[-1] = row[-1][:-1]
        row = list(map(int, row))
        matrix.append(row)

for i in range(78,-1,-1):
    matrix[79][i] += matrix[79][i+1]
    matrix[i][79] += matrix[i+1][79]

for i in range(78,-1,-1):
    for j in range(78,-1,-1):
        matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1])
print(matrix[0][0])
