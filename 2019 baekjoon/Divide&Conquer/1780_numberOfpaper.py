n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cnt = [0] * 3

def same(x, y, n):
    for i in range(n):
        for j in range(n):
            if a[x + i][y + j] != a[x][y]:
                return False
    return True


def solve(x, y, n):
    if same(x, y, n):
        cnt[a[x][y] + 1] += 1
        return
    m = n//3
    for i in range(3):
        for j in range(3):
            solve(x + i*m, y + j*m, m)


solve(0, 0, n)
print(cnt)