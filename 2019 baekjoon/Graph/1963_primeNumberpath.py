from collections import deque

prime = [False] * 10001
d = [-1] * 10001




for i in range(2, 10001):
    if not prime[i]:
        for j in range(i * i, 10001, i):
            prime[j] = True

case = int(input())
for _ in range(case):
    a, b = map(int, input().split())

    q = deque()
    q.append(a)
    d[a] = 0
    while q:
        now = q.popleft()
        check = False
        temp = 0
        for i in range(4):
            for j in range(10):
                next = change(now, i, j)
                if next != -1:
                    if prime[next] and d[next] == -1:
                        q.append(next)
                        d[next] = d[now] + 1


    print(d[b])