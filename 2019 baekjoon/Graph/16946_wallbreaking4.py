from collections import deque

n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
c = [[False] * m for _ in range(n)]
g = [[0] * m for _ in range(n)]
g_size = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    g_l = len(g_size)
    g[x][y] = g_l
    c[x][y] = True
    cnt = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if not c[nx][ny] and a[nx][ny] == 0:
                    q.append((nx, ny))
                    c[nx][ny] = True
                    g[nx][ny] = g_l
                    cnt += 1
    g_size.append(cnt)


for i in range(n):
    for j in range(m):
        if not c[i][j] and a[i][j] == 0:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(0, end='')
        else:
            near = set()  # 중복없이 저장,,
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        near.add(g[nx][ny])
            ans = 1
            for p in near:
                ans += g_size[p]
            print(ans % 10, end='')
    print()

