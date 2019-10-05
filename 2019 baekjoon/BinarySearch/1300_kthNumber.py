n = int(input())
k = int(input())
a = [[0]*n for _ in range(n)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a[i-1][j-1] = i * j

for row in a:
    print(' '.join(map(str, row)))


def check(mid):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, mid//i)

    if cnt >= k:
        return True
    else:
        return False


left = 1
right = n * n
ans = 0
while left <= right:
    mid = (left + right) // 2

    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)




