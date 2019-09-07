n = int(input())
src = [list(map(int, input().split())) for _ in range(n)]
t, p = zip(*src)
t = [0] + list(t)
p = [0] + list(p)
ans = 0


def solve(day, total):
    global ans
    if day == n:
        if ans < total:
            ans = total
    if day > n:
        return

    solve(day + t[day], total + p[day])
    solve(day + 1, total)


solve(1, 0)
print(ans)
