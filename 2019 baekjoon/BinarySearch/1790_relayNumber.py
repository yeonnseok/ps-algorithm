n, k = map(int, input().split())


def jaritsu(n):
    ans = 0
    start = 1
    len = 1
    while start <= n:
        end = start * 10 - 1
        if end > n:
            end = n
        ans += (end - start + 1) * len
        start *= 10
        len += 1
    return ans


left = 1
right = n
ans = 0
while left <= right:
    mid = (left + right) // 2
    if jaritsu(n) < k:
        print(-1)
        exit()

    if jaritsu(mid) == k:
        ans = mid
        break
    elif jaritsu(mid) < k:
        left = mid + 1
    else:
        right = mid - 1

s = str(ans)
l = jaritsu(ans)
print(s[len(s) - (l-k) - 1])
