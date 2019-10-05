n, m = map(int, input().split())
a = [[] for _ in range(n)]

check = [False] * n
for _ in range(m):
    u, v, w = map(int, input().split())
    a[u-1].append((v-1, w))
    a[v-1].append((u-1, w))
start, end = map(int, input().split())
start -= 1
end -= 1
print(a)
print(start, end)


def dfs(x, limit):
    if check[x]:
        return False
    check[x] = True
    print(end)
    if x == end:
        return True

    for y in a[x]:
        next = y[0]
        cost = y[1]
        if cost >= limit:
            if dfs(next, limit):
                return True
    return False


left = 1
right = 1000000000
ans = 0
while left <= right:
    mid = (left + right) // 2

    for i in range(n):
        check[i] = False

    if dfs(start, mid):
        print(mid)
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
