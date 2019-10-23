n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]

d = [[False] * m for _ in range(n)]
ans = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            l = 0
            k = 1
            while i + k < n and i - k >= 0 and j + k < m and j - k >= 0:
                if a[i+k][j] == '*' and a[i-k][j] == '*' and a[i][j+k] == '*' and a[i][j-k] == '*':
                    l = k
                else:
                    break
                k += 1
            if l > 0:
                ans.append((i + 1, j + 1, l))
                # d[i][j] = True   #중심
                # for k in range(1, l+1):
                #     d[i+k][j] = True
                #     d[i-k][j] = True
                #     d[i][j+k] = True
                #     d[i][j-k] = True

if ans:
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0], ans[i][1], ans[i][2])
else:
    print(-1)