from collections import deque

dx = [2, 2, 0, 0, -2, -2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
a = [[0] * n for _ in range(n)]
d = [[-1] * n for _ in range(n)]

x1, y1, x2, y2 = map(int, input().split())

q = deque()
q.append((x1, y1))
d[x1][y1] = 0

while q:
    x1, y1 = q.popleft()
    if x1 == x2 and y1 == y2:
        break
    for k in range(6):
        nx1, ny1 = x1 + dx[k], y1 + dy[k]
        if 0 <= nx1 < n and 0 <= ny1 < n:
            if d[nx1][ny1] == -1:
                d[nx1][ny1] = d[x1][y1] + 1
                q.append((nx1, ny1))

print(d[x2][y2])



