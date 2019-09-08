from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
g = [[0] * n for _ in range(n)]
d = [[-1] * n for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 섬 그룹 만들기
cnt = 0
q = deque()
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and g[i][j] == 0:
            cnt += 1
            g[i][j] = cnt
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if a[nx][ny] == 1 and g[nx][ny] == 0:
                            g[nx][ny] = cnt
                            q.append((nx, ny))

# 거리 만들기
ans = -1
for l in range(1, cnt + 1):
    q = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == l:
                q.append((i, j))
                d[i][j] = 0

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if d[nx][ny] == -1:
                    d[nx][ny] = d[x][y] + 1
                    q.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and g[i][j] != l:
                if ans == -1 or d[i][j] - 1 < ans:
                    ans = d[i][j] - 1

print(d)

print(ans)


