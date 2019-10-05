n, m = map(int, input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]


def flip(x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            a[i][j] = 1 - a[i][j]


ans = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            ans += 1
            flip(i + 1, j + 1)

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit()

print(ans)
