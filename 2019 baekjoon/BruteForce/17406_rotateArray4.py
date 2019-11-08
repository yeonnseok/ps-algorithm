n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
for _ in range(k):
    r, c, s = map(int, input().split())
    x1, y1 = r-s-1, c-s-1
    temp = a[x1][y1]
    # 2s
    ...........다시