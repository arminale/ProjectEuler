with open("triangle.txt", 'r') as input:
    triangle = []
    for line in input:
        line = list(map(int,line.strip().split(' ')))
        triangle.append(line)
    for i in range(len(triangle) - 1, 0, -1):
        for j in range(len(triangle[i]) - 1):
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
        del(triangle[i])
    print(triangle)