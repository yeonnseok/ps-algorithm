n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [[False] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, cnt):
    if check[x][y]:
        if cnt - dist[x][y] >= 4:
            return True
        else:
            return False
    dist[x][y] = cnt
    check[x][y] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n and 0 <= x < n and 0 <= y < n:
            if a[nx][ny] == a[x][y]:
                if dfs(nx, ny, cnt + 1):
                    return True
    return False


for i in range(n):
    for j in range(m):
        if check[i][j]:
            continue
        dist = [[0]*m for _ in range(n)]
        ok = dfs(i, j, 1)
        if ok:
            print("YES")
            exit()
print('No')
