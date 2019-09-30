n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
new = []
a_idx = 0
b_idx = 0
while a_idx < n and b_idx < m:
    if a[a_idx] >= b[b_idx]:
        new.append(b[b_idx])
        b_idx += 1
    elif a[a_idx] < b[b_idx]:
        new.append(a[a_idx])
        a_idx += 1

if a[a_idx:]:
    for i in range(a_idx, n):
        new.append(a[i])
if b[b_idx:]:
    for i in range(b_idx, m):
        new.append(b[i])
print(new)