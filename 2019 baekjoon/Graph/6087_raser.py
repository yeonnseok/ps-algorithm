from collections import deque

m, n = map(int, input().split())
a = [list(input()) for _ in range(n)]
d = [[-1] * m for _ in range(n)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

s_x, s_y = 0, 0
e_x, e_y = 0, 0

for i in range(n):
    for j in range(m):
        if a[i][j] == 'C':
            if s_x == 0:
                s_x, s_y = i, j
            else:
                e_x, e_y = i, j

q = deque()
q.append((s_x, s_y))
d[s_x][s_y] = 0

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        while 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] == "*":
                break
            if d[nx][ny] == -1:
                q.append((nx, ny))
                d[nx][ny] = d[x][y] + 1

            nx += dx[k]
            ny += dy[k]

print(d[e_x][e_y]-1)