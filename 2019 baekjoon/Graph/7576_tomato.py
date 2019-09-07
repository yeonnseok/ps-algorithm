from collections import deque

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dist = [[-1] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1 and a[nx][ny] == 0:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

# dist 를 [-1]로 초기화 하면 check  배열을 만들지 않아도 된다.
# 스타트 지점을 처음에 q에 집어넣으면 된다.

ans = max([max(row) for row in dist])
for i in range(n):
    for j in range(m):
        if a[i][j] == 0 and dist[i][j] == -1:
            ans = -1
print(ans)
