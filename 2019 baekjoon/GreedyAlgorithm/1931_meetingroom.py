n = int(input())
a = []
for _ in range(n):
    u, v = map(int, input().split())
    a.append((u, v))

ans = 0
now = 0
for i in range(len(a)):
    if now <= a[i][0]:
        now = a[i][1]
        ans += 1

print(ans)
