n = int(input())
a = []
for _ in range(n):
    u, v = map(int, input().split())
    a.append((u, v))
a = sorted(a, key=lambda x: x[1])

ans = 0
while a:
    if len(a) == 1:
        ans += a[0][0]
        break
    i = 0
    temp = a[i]
    while a[i][1] == a[i+1][1]:
        if temp[1] < a[i+1][1]:
            temp = a[i+1]
        i += 1
    ans += temp[0]
    a = a[i+1:]
print(ans)
