n, m = map(int, input().split())
a = list(map(int, input().split()))


def check(a, mid):
    l = len(a)
    t1 = a[0]
    t2 = a[0]
    ans = 1
    for i in range(1, l):
        if t1 > a[i]:
            t1 = a[i]
            # 최소값만들기
        if t2 < a[i]:
            t2 = a[i]
            # 최대값 만들기
        if t2-t1 > mid:
            ans += 1
            t1 = a[i]
            t2 = a[i]
    return ans


left = 0
right = max(a)
ans = right
while left <= right:
    mid = (left + right) // 2
    if check(a, mid) <= m:
        if ans > mid:
            ans = mid
        right = mid - 1

    else:
        left = mid + 1

print(ans)

