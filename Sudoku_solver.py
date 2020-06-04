board = [
    # [5, 0, 0, 0, 1, 0, 0, 0, 4],
    # [2, 7, 4, 0, 0, 0, 6, 0, 0],
    # [0, 8, 0, 9, 0, 4, 0, 0, 0],
    # [8, 1, 0, 4, 6, 0, 3, 0, 2],
    # [0, 0, 2, 0, 3, 0, 1, 0, 0],
    # [7, 0, 6, 0, 9, 1, 0, 5, 8],
    # [0, 0, 0, 5, 0, 3, 0, 1, 0],
    # [0, 0, 5, 0, 0, 0, 9, 2, 7],
    # [1, 0, 0, 0, 2, 0, 0, 0, 3]

    [0, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 8, 0, 0, 0, 7, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 5, 0, 0],
    [0, 7, 0, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 9, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 4, 0],
    [0, 0, 5, 0, 0, 0, 6, 0, 3],
    [0, 9, 0, 4, 0, 0, 0, 7, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0]
]


def solver_backtracking(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solver_backtracking(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):

    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(bo[0])):

            if j % 3 == 0:
                print("| ", end='')
            if j == 8:
                print(str(bo[i][j])+' ', end='')
                print("| ")
            else:
                print(str(bo[i][j])+' ', end='')


def find_empty(bo):
    for row in range(len(bo)):
        for col in range(len(bo[0])):
            if bo[row][col] == 0:
                return (row, col)
    return None

    return None


print_board(board)
print("Solving.....")
solver_backtracking(board)
print(" ")
print(" Solution ")
print(" ")
print_board(board)
