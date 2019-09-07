n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

# 인접 리스트 구현
for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# 인접 리스트 정렬(필수는 아님)
for i in range(n):
    a[i].sort()


def dfs(x):
    global check
    check[x] = True
    for y in a[x]:
        if check[y] == 0:
            dfs(y)


ans = 0
for i in range(1, n + 1):
    if not check[i]:
        dfs(i)
        ans += 1
print(ans)
