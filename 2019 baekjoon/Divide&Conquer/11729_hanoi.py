n = int(input())
cnt = 0


def solve(n, x, y):
    global cnt
    if n == 0:
        return
    solve(n-1, x, 6 - (x + y))
    cnt += 1
    print(x, y)
    solve(n-1, 6 - (x + y), y)


solve(n, 1, 3)
print(cnt)