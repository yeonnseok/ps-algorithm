n, m = map(int, input().split())
a = list(map(int, input().split()))


def check(x):
    ans = 0
    for i in range(n):
        if a[i] - x > 0:  # 이게 중요한 조건!!
            ans += (a[i] - x)

    if ans >= m:
        return True
    else:
        return False


upper = max(a)
lower = 0
ans = 0
while lower <= upper:
    mid = (lower + upper) // 2

    if check(mid):
        if ans < mid:
            ans = mid
        lower = mid + 1
    else:
        upper = mid - 1

print(ans)