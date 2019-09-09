from collections import deque

MAX = 100111
n = int(input())
a = [[] for _ in range(MAX)]
check = [0] * MAX
parent = [0] * MAX
depth = [0] * MAX
dist = [0] * MAX


# 인접 리스트 구현
for i in range(n-1):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

depth[1] = 0
check[1] = 1

q = deque()
q.append(1)  # 루트 1 부터 시작
while q:
    x = q.popleft()
    for y in a[x]:
        if check[y] == 0:
            depth[y] = depth[x] + 1
            check[y] = 1
            parent[y] = x
            q.append(y)


for i in range(2, n + 1):
    print(parent[i], end=' ')

