n, m = 3, 7
a = [['#', '.', '.', '.', '.', '.', '#'],
     ['#', '.', '.', '.', '.', '.', '#'],
     ['#', '#', '.', '.', '#', '#', '#']]


coverType = [[[0, 0], [1, 0], [0, 1]],
             [[0, 0], [1, 0], [1, 1]],
             [[0, 0], [0, 1], [1, 1]],
             [[0, 0], [1, 0], [1, -1]]]

b = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] == '#':
            b[i][j] = 1

for row in b:
    print(' '.join(map(str, row)))


def setting(board, x, y, type, delta):
    ok = True
    for k in range(3):
        nx = x + coverType[type][k][0]
        ny = y + coverType[type][k][1]
        if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]):
            ok = False
        board[nx][ny] += delta
        if board[nx][ny] > 1:
            ok = False
    return ok


def cover(board):
    x, y = -1, -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                x, y = i, j
                break
        if x != -1:
            break

    if x == -1:
        return 1
    ret = 0
    for type in range(4):
        if setting(board, x, y, type, 1):
            ret += cover(board)

        setting(board, x, y, type, -1)
    return ret


print(cover(b))
