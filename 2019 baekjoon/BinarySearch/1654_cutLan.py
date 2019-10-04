k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))


def check(x):
    cnt = 0
    for i in range(k):
        cnt += a[i]//x
    if cnt >= n:
        return True
    else:
        return False


left = 1
right = max(a)
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        if ans < mid:
            ans = mid
        left = mid + 1
    else:
        right = mid - 1


print(ans)