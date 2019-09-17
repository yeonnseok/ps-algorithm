# 동 북 서 남 순서
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
d = [[False] * 101 for _ in range(101)]


def curve(dir, gen):
    ans = [dir]  # 현재 방향 추가
    for g in range(1, gen + 1):  # 전체 G의 횟수만큼 돌면서
        temp = ans[:]
        temp = temp[::-1]
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 4  # 이전 세대까지의 방향을 모두 회전시킴
        ans += temp
    return ans


n = int(input())
for _ in range(n):
    y, x, dir, gen = map(int, input().split())
    dirs = curve(dir, gen)
    d[x][y] = True
    for direction in dirs:
        x += dx[direction]
        y += dy[direction]
        d[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if d[i][j] and d[i][j+1] and d[i+1][j] and d[i+1][j+1]:  # 정사각형 갯수세기
            ans += 1
print(ans)
