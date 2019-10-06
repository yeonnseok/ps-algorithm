n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a = sorted(a, reverse=True)
print(a)

ans = 0
i = 0
while i < n:
    if i != n-1:
        if (a[i] > 0 and a[i+1] > 0) or (a[i] < 0 and a[i+1] < 0):
            ans += a[i] * a[i+1]
            i += 2
        else:
            ans += a[i]
            i += 1
    else:
        if a[i] < 0 and 0 in a:
            break
        ans += a[i]
        break
print(ans)