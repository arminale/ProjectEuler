alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
            "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19,
            "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
with open("names.txt", 'r') as inputFile:
    line = inputFile.read().strip().split(',')
    totalScore = 0
    for i in range(len(line)):
        line[i] = line[i][1:len(line[i]) - 1]
    line.sort()
    for i in range(len(line)):
        temp  = 0
        for j in line[i]:
            temp += alphabet[j]
        totalScore += temp * (i+1)
    print(totalScore)