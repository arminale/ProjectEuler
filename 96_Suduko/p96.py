# https://projecteuler.net/problem=96 Sudoku
# This program solves Sudoku puzzles using a brute force algorithm.
# A Sudoku grid is represented in a 1D list where board[0] is the top left element in the board, and the element in the
# i-th row and the j-th column of the board is stored in board[(i-1)*9 + (j-1)]. Note the minus one comes from zero
# indexing.
# Empty elements have a value of 0.


def print_board(board):
    for i in range(0, 81, 9):
        print(board[i:i+9])


# Takes a board and determines whether there are duplicates in a row, column or block
def check_rules(board):
    for i in range(0,81,9):
        row = board[i:i+9]
        for num in row:
            if row.count(num) > 1 and num != 0:
                return False

    for i in range(0,9,1):
        col = []
        for j in range(0,81,9):
            col.append(board[i+j])

        for num in col:
            if col.count(num) > 1 and num != 0:
                return False

    for i in range(0, 81, 27):
        for j in range(i, i+9, 3):
            block = [ board[j], board[j+1], board[j+2], board[j+9], board[j+10], board[j+11], board[j+18],
                      board[j+19], board[j+20] ]
            for num in block:
                if block.count(num) > 1 and num != 0:
                    return False

    return True


def solve(board):
    indexes_to_fill = []
    for i in range(len(board)):
        if board[i] == 0:
            indexes_to_fill.append(i)

    i = 0
    while i < len(indexes_to_fill):
        index = indexes_to_fill[i]
        if board[index] < 9:
            board[index] += 1
            if check_rules(board):
                i += 1
            elif board[index] == 9:
                board[index] = 0
                i -= 1
        else:
            board[index] = 0
            i -= 1
    return board


with open("p096_sudoku.txt", 'r') as input_file:
    current_board = []
    sums = 0
    i = 0 #counts the number of puzzles solved
    for line in input_file:

        if line[:-1].isdigit() or line.isdigit():
            # ignores the end of line character. "or" is for the last line which doesn't end with "\n"
            for num in line:
                if num.isdigit():
                    current_board.append(int(num))
            if len(current_board) == 81:
                solve(current_board)
                i += 1
                sums += 100 * current_board[0] + 10 * current_board[1] + current_board[2]
        else:

            current_board = []


print(i)
print(sums)

