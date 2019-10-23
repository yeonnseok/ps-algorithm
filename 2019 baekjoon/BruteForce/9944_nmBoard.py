dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]




def go(x, y, cnt):
    ans = -1
    if cnt == 0:
        return 0

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        while 0 <= nx < n and 0 <= ny < m and a[nx][ny] == '.':
            a[nx][ny] = '#'
            cnt -= 1
            nx += dx[k]
            ny += dy[k]
        nx -= dx[k]
        ny -= dy[k]
        if x != nx and y != ny:
            temp = go(nx, ny, cnt)
            if temp != -1:
                if ans == -1 or ans > temp + 1:
                    ans = temp + 1

        while x != nx and y != ny:   # 다시 원상 복구
            a[nx][ny] = '.'
            cnt += 1
            nx -= dx[k]
            ny -= dy[k]

    return ans


n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
d = [[False] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == '.':
            cnt += 1

ans = -1
for i in range(n):
    for j in range(m):
        if a[i][j] == '.':
            a[i][j] = '#'
            temp = go(i, j, cnt - 1)
            if temp != -1:
                if ans == -1 or ans > temp:
                    ans = temp
            a[i][j] = '.'

print(ans)