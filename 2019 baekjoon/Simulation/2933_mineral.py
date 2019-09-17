r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
n = int(input())
throw = list(map(int, input().split()))  # 왼쪽/오른쪽 번갈아가며

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, check, group):
    if a[x][y] == ".":
        return
    if check[x][y]:
        return
    check[x][y] = True
    group.append((x, y))
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            dfs(nx, ny, check, group)


def simulate():
    check = [[False]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if a[x][y] == '.':
                continue
            if check[x][y]:
                continue
            group = []
            dfs(x, y, check, group)
            low = [-1] * c
            for gx, gy in group:
                low[gy] = max(low[gy], gx)
                a[gx][gy] = '.'
            lowest = r
            for j in range(c):
                if low[j] == -1:
                    continue
                i = low[j]
                while i < r and a[i][j] == '.':
                    i += 1
                lowest = min(lowest, i-low[j]-1)
            for gx, gy in group:
                gx += lowest
                a[gx][gy] = 'x'
                check[gx][gy] = True


for i in range(len(throw)):
    # 홀수번째 던지기
    height = r - throw[i]
    if i % 2 == 0:
        for j in range(c):
            if a[height][j] == 'x':
                a[height][j] = '.'
                break

    # 짝수번째 던지기
    else:
        for j in range(c-1, -1, -1):
            if a[height][j] == 'x':
                a[height][j] = '.'
                break

    simulate()

for row in a:
    print(row)

