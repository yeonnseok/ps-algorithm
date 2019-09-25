from collections import deque

n, m, l = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
d = [[[0] * (l+1) for _ in range(m)] for _ in range(n)]

q = deque()
q.append((0, 0, 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

d[0][0][0] = 1
while q:
    x, y, z = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if d[nx][ny][z] == 0 and a[nx][ny] == 0:
                q.append((nx, ny, z))
                d[nx][ny][z] = d[x][y][z] + 1

            if z < l and a[nx][ny] == 1 and d[nx][ny][z+1] == 0:
                d[nx][ny][z+1] = d[x][y][z] + 1
                q.append((nx, ny, z+1))

for row in d:
    print(' '.join(map(str, row)))

ans = -1
for p in range(l + 1):
    if d[n-1][m-1][p] == 0:
        continue
    if ans == -1:
        ans = d[n-1][m-1][p]
    elif ans > d[n-1][m-1][p]:
        ans = d[n-1][m-1][p]
print(ans)
