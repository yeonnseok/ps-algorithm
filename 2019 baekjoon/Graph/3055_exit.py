from collections import deque

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
water = [[-1] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


end_x, end_y = 0, 0

q = deque()
w = deque()

for i in range(n):
    for j in range(m):
        if a[i][j] == 'S':
           q.append((i, j))
           dist[i][j] = 0

        elif a[i][j] == '*':
           w.append((i, j))
           water[i][j] = 0

        elif a[i][j] == 'D':
            end_x, end_y = i, j


while w:
    x, y = w.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if water[nx][ny] == -1 and a[nx][ny] != "X" and a[nx][ny] != 'D':
                w.append((nx, ny))
                water[nx][ny] = water[x][y] + 1


ans = False
while q:
    x, y = q.popleft()
    if end_x == x and end_y == y:
        ans = True
        break
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if a[nx][ny] != "X" and dist[nx][ny] == -1:
                if (dist[nx][ny] < water[nx][ny]) or a[nx][ny] == 'D':
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1


print(dist[end_x][end_y] if ans else "KAKTUS")


