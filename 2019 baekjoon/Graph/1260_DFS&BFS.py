from collections import deque

n, m, start = map(int, input().split())
a = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

# 인접 리스트 구현
for i in range(m):
    u, v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)

# 인접 리스트 정렬
for i in range(n):
    a[i].sort()

print(a)

def dfs(x):
    global check
    check[x] = True
    print(x, end=' ')
    for y in a[x]:
        if check[y] == 0:
            dfs(y)


def bfs(start):
    ch = [0] * (n + 1)
    q = deque()
    q.append(start)
    ch[start] = True
    while q:
        x = q.popleft()
        print(x, end=" ")
        for y in a[x]:
            if ch[y] == 0:
                ch[y] = True
                q.append(y)


dfs(start)
print()
bfs(start)
