n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def tetromino(x, y, total, cnt):
    global ans
    if cnt == 4:
        if ans < total:
            ans = total
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if not check[nx][ny]:
                check[nx][ny] = True
                tetromino(nx, ny, total + board[nx][ny], cnt + 1)
                check[nx][ny] = False


for i in range(n):
    for j in range(m):
        tetromino(i, j, 0, 0)

        if j + 2 < m:
            temp1 = board[i][j] + board[i][j+1] + board[i][j+2]
            if i + 1 < n:
                temp2 = temp1 + board[i+1][j+1]
                if ans < temp2:
                    ans = temp2
            if i - 1 >= 0:
                temp2 = temp1 + board[i-1][j+1]
                if ans < temp2:
                    ans = temp2

        if i + 2 < n:
            temp1 = board[i][j] + board[i+1][j] + board[i+2][j]
            if j + 1 < m:
                temp2 = temp1 + board[i+1][j+1]
                if ans < temp2:
                    ans = temp2
            if j - 1 >= 0:
                temp2 = temp1 + board[i+1][j-1]
                if ans < temp2:
                    ans = temp2
print(ans)