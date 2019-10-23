n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

#서 북 동 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    # 현재 위치 청소가 안되어 있으면 청소하라
    if a[x][y] == 0:
        a[x][y] = 2  # 청소완료
        cnt += 1

    # 네 방향 모두 청소가 되어있을경우
    if a[x+1][y] != 0 and a[x-1][y] != 0 and a[x][y-1] != 0 and a[x][y+1] != 0:
        # 벽이면 동작그만
        if a[x-dx[d]][y-dy[d]] == 1:
            print(cnt)
            exit()
        # 벽이 아니면 바로 후진
        else:
            x -= dx[d]
            y -= dy[d]

    # 네 방향 중 한방향이라도 청소가 안되어 있을경우
    else:
        # 반시계 방향으로 돈다.
        d = (d + 3) % 4
        if a[x + dx[d]][y + dy[d]] == 0:  # 직진했을때 청소가 안되어있으면
            x += dx[d]
            y += dy[d]

print(cnt)
