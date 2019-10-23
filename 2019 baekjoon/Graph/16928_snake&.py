from collections import deque

n, m = map(int, input().split())
next = [i for i in range(101)]
d = [-1] * 101

for _ in range(n):
    u, v = map(int, input().split())
    next[u] = v

for _ in range(m):
    u, v = map(int, input().split())
    next[u] = v

x = 1
q = deque()
q.append(x)
d[1] = 0
while q:
    x = q.popleft()
    for i in range(1, 7):
        y = x + i
        if y > 100:
            continue
        y = next[y]
        if d[y] == -1:
            d[y] = d[x] + 1
            q.append(y)

print(d[100])
