n = int(input())
a = []
for _ in range(n):
    u, v = map(int, input().split())
    a.append((u, v))

ans = 1
now = 2**31 - 1
for i in range(len(a)):
    if now > a[i][1]:
        now = a[i][1]

for i in range(len(a)):
    if a[i][0] >= now:
        now = 2 ** 31 - 1
        for j in range(i, len(a)):
            if now > a[j][1]:
                now = a[j][1]
        ans += 1
print(ans)