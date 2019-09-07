from collections import deque

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dist = [[0] * m for _ in range(n)]
dist[0][0] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 출발점은 (0, 0)


def bfs(x, y):
    q = deque()
    q.append((x, y))
    check[x][y] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if check[nx][ny] == 0 and a[nx][ny] == 1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
                    check[nx][ny] = 1


bfs(0, 0)
print(dist[n-1][m-1])
