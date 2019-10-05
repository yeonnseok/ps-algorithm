n, m = map(int, input().split())
a = list(map(int, input().split()))


def check(x):
    cnt = 1
    sum = 0
    for i in range(n):
        if sum + a[i] > x:
            cnt += 1
            sum = a[i]
        else:
            sum += a[i]
    if cnt <= m:
        return True
    else:
        return False


left = max(a)  # 레슨 크기의 최대값,
right = sum(a)  # 레슨 크기의 합
ans = 0
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        if ans < mid:
            ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)

