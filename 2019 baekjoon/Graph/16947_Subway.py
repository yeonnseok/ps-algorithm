from collections import deque

# dfs 로 순환선을 찾고
# bfs 로 거리를 계산한다.

# dfs => 인접리스트로 구한다.
n = int(input())
a = [[] for _ in range(n)]
check = [0] * n  # 0: not visited, 1: visited, 2: cycle

# 인접 리스트 구현
for i in range(n):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)


def dfs(x, p):
    # 이미 방문한 점을 만났다면!? => 사이클이나 다름없음
    # -2: found cycle and not included
    # -1: not found cycle
    # 0~n-1: found cycle and start index
    if check[x] == 1:
        return x

    check[x] = 1
    for y in a[x]:
        if y == p:
            continue
        res = dfs(y, x)
        if res == -2:
            return -2
        if res >= 0:
            check[x] = 2  # 사이클에 속하는 정점일 경우,,
            if x == res:
                return -2
            else:
                return res
    return -1


dfs(0, -1)


q = deque()
dist = [-1] * n
for i in range(n):  # n 역과 순환선 사이의 거리를 dist 에 저장한다.
    if check[i] == 2:
        q.append(i)
        dist[i] = 0

while q:
    x = q.popleft()
    for y in a[x]:
        if dist[y] == -1:
            q.append(y)
            dist[y] = dist[x] + 1

print(*dist, sep=" ")
