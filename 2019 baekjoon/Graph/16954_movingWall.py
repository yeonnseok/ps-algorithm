from collections import deque

n = 8
a = [list(input()) for _ in range(n)]
check = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

dx = [0, 0, 1, -1, 1, 1, -1, -1, 0]
dy = [1, -1, 0, 0, -1, 1, -1, 1, 0]

check[7][0][0] = True
q = deque()
q.append((7, 0, 0))
ans = False

while q:
    x, y, t = q.popleft()
    if x == 0 and y == 7:
        ans = True
    for k in range(9):
        nx, ny = x + dx[k], y + dy[k]
        nt = min(t + 1, 8)
        if 0 <= nx < n and 0 <= ny < n:
            if nx-t >= 0 and a[nx-t][ny] == '#':
                continue
            if nx-t-1 >= 0 and a[nx-t-1][ny] == '#':
                continue
            if not check[nx][ny][nt]:
                check[nx][ny][nt] = True
                q.append((nx, ny, nt))

print(1 if ans else 0)

