from collections import deque

n = int(input())
a = [list(input()) for _ in range(n)]
d = [[-1] * n for _ in range(n)]
d2 = [[-1] * n for _ in range(n)]

g = [[0] * n for _ in range(n)]
g2 = [[0] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def blind(nx, ny, x, y):
    ans = False
    if a[nx][ny] == a[x][y]:
        ans = True
    elif a[nx][ny] == 'R' and a[x][y] == 'G':
        ans = True
    elif a[nx][ny] == 'G' and a[x][y] == 'R':
        ans = True
    return ans


def bfs(a, x, y, cnt, is_bl):
    q = deque()
    q.append((x, y))
    if is_bl:
        d[x][y] = 0
        g[x][y] = cnt
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if blind(nx, ny, x, y) and d[nx][ny] == -1:
                        q.append((nx, ny))
                        d[nx][ny] = d[x][y] + 1
                        g[nx][ny] = cnt
    else:
        d2[x][y] = 0
        g2[x][y] = cnt
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if a[nx][ny] == a[x][y] and d2[nx][ny] == -1:
                        q.append((nx, ny))
                        d2[nx][ny] = d2[x][y] + 1
                        g2[nx][ny] = cnt


cnt = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if d[i][j] == -1:
            cnt += 1
            bfs(a, i, j, cnt, True)
        if d2[i][j] == -1:
            cnt2 += 1
            bfs(a, i, j, cnt2, False)


print(cnt2, cnt)