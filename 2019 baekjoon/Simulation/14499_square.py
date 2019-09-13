dx = [0, 0, -1, 1]  # 여기서부터 동서 북남을 잘 설정해줘야한다.
dy = [1, -1, 0, 0]
n, m, x, y, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dice = [0]*7
move = list(map(int, input().split()))
print(move)
for k in move:
    k -= 1
    nx, ny = x + dx[k], y + dy[k]
    if 0 <= nx < n and 0 <= ny < n:
        if k == 0:  # 동
            temp = dice[1]
            dice[1] = dice[4]
            dice[4] = dice[6]
            dice[6] = dice[3]
            dice[3] = temp
        elif k == 1:  # 서
            temp = dice[1]
            dice[1] = dice[3]
            dice[3] = dice[6]
            dice[6] = dice[4]
            dice[4] = temp
        elif k == 2:  # 북
            temp = dice[1]
            dice[1] = dice[5]
            dice[5] = dice[6]
            dice[6] = dice[2]
            dice[2] = temp
        elif k == 3:  # 남
            temp = dice[1]
            dice[1] = dice[2]
            dice[2] = dice[6]
            dice[6] = dice[5]
            dice[5] = temp

        x, y = nx, ny
        if a[x][y] == 0:
            a[x][y] = dice[6]
        else:
            dice[6] = a[x][y]
            a[x][y] = 0
        print(dice[1])

