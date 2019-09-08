from collections import deque

n = int(input())
a = [[] for _ in range(n)]
check = [False] * n
parent = [-1] * n


# 인접 리스트 구현
for i in range(n-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    a[u].append(v)
    a[v].append(u)

order = list(map(int, input().split()))
order = [x-1 for x in order]

q = deque()
q.append(0)
check[0] = True

m = 1
for i in range(n):
    if not q:  # 아직 BFS 가 진행중인데 큐가 비어있음.
        print(0)
        exit()

    # order 의 순서대로 하나씩 검사
    x = q.popleft()
    if x != order[i]:  # 순서가 올바르지 않음.
        print(0)
        exit()

    cnt = 0  # 이번에 큐에 넣어야할 정점의 수
    for y in a[x]:
        if check[y] is False:
            parent[y] = x
            cnt += 1

    for j in range(cnt):
        if m + j >= n or parent[order[m+j]] != x:
            # X와 연결되지 않은 정점이 큐에 들어가 있으니 올바르지 않음.
            print(0)
            exit()
        q.append(order[m+j])
        check[order[m+j]] = True
    m += cnt
print(1)

