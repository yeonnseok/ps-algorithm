n, m = map(int, input().split())

ans = 0
if n == 1:
    ans = 1
    print(ans)
    exit()

elif n == 2:
    ans = min(4, (m + 1) // 2)

elif n >= 3:
    if m < 7:
        ans = min(4, m)
    else:
        ans = m - 2

print(ans)
