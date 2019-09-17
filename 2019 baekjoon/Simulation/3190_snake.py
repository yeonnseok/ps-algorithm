
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
d = [[-1]*100 for _ in range(100)]
apple = [[False]*100 for _ in range(100)]
n = int(input())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    apple[x-1][y-1] = True
x = 0
y = 0
direction = 0
length = 1
d[x][y] = 0
m = int(input())
now = 0
for k in range(0, m+1):
    t = n*n+1
    ch = 'L'
    if k < m:
        t, ch = input().split()
        t = int(t)
    while now < t:
        now += 1
        x += dx[direction]
        y += dy[direction]
        if x < 0 or x >= n or y < 0 or y >= n:
            print(now)
            exit()
        if apple[x][y]:
            apple[x][y] = False
            length += 1
        if d[x][y] != -1 and now-d[x][y] <= length:
            print(now)
            exit()
        d[x][y] = now
    if ch == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4

