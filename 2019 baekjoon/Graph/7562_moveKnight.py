from collections import deque

dx = [1, 2, -1, -2, 1, 2, -1, -2]
dy = [2, 1, 2, 1, -2, -1, -2, -1]


def bfs(q):
    while q:
        x, y = q.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if nx == end[0] and ny == end[1]:
                dist[nx][ny] = dist[x][y] + 1
                return
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 0 and dist[nx][ny] == -1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1


k = int(input())
for _ in range(k):
    n = int(input())
    a = [[0] * n for _ in range(n)]
    dist = [[-1] * n for _ in range(n)]
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    q = deque()
    q.append(start)
    dist[start[0]][start[1]] = 0
    if start != end:
        bfs(q)
        ans = max([max(row) for row in dist])
    else:
        ans = 0
    print(ans)
