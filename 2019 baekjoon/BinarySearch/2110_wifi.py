n, c = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))
a.sort()


def check(x):
    ans = 1
    last = a[0] # 첫집부터 설치했다고 가정..
    for i in range(n):
        if a[i] - last >= x:
            ans += 1
            last = a[i]
    if ans >= c:
        return True
    else:
        return False


left = 0
right = len(a) - 1
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

