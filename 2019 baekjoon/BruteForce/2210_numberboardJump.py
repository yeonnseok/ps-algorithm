dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def go(x, y, num, length):
    if length == 6:  # 6자리 숫자가 된다.
        ans.add(num)
        return

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            go(nx, ny, num*10 + a[nx][ny], length + 1)

n = 5
a = [list(map(int, input().split())) for _ in range(n)]
ans = set()  # 중복저장을 막는다. 서로다른 6자리 수들의 갯수
for i in range(n):
    for j in range(n):
        go(i, j, a[i][j], 1)
print(len(ans))
