from collections import deque

n, k = map(int, input().split())
maxi = 100000
check = [0] * maxi
dist = [-1] * maxi
q = deque()
q.append(n)
check[n] = 1
dist[n] = 0
while q:
    x = q.popleft()
    for nxt in [x - 1, x + 1, 2 * x]:
        if (0 <= nxt < maxi) and check[nxt] == 0:
            q.append(nxt)
            check[nxt] = 1
            dist[nxt] = dist[x] + 1

print(dist[k])