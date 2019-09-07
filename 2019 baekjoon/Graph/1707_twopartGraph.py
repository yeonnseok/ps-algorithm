k = int(input())
for _ in range(k):
    n, m = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    color = [0] * (n + 1)

    # 인접 리스트 구현
    for i in range(m):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)

    # color == 0이면 아직 방문 x, color ==> 1 / 2


    def dfs(x, c):
        color[x] = c
        for y in a[x]:
            if color[y] == 0:
                dfs(y, 3 - c)

    ans = True
    for i in range(1, n + 1):
        if color[i] == 0:
            dfs(i, 1)

    for i in range(1, n + 1):
        for j in a[i]:
            if color[i] == color[j]:
                ans = False

    print("YES" if ans else "NO")





