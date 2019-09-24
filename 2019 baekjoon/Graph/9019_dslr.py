from collections import deque

t = int(input())


def go(n, m):
    if n == m:
        return
    go(n, _from[m])
    print(_how[m], end=' ')


# 정점의 갯수 0 ~ 100000
a = [i for i in range(10001)]
for _ in range(t):
    x, y = map(int, input().split())
    d = [-1] * 10001
    _from = [-1] * 10001
    _how = [''] * 10001

    q = deque()
    q.append(x)
    d[x] = 0
    _from[x] = -1
    while q:
        x = q.popleft()
        if x == y:
            break

        l_calc = (x % 1000)*10 + x//1000
        r_calc = x // 10 + (x % 10)*1000

        for nxt in [(2 * x) % 10000, x - 1, l_calc, r_calc]:
            if nxt == (2 * x) % 10000:
                if 0 <= nxt <= 10000:
                    if d[nxt] == -1:
                        q.append(nxt)
                        d[nxt] = d[x] + 1
                        _from[nxt] = x
                        _how[nxt] = 'L'
            if nxt == x - 1:
                if nxt == -1:
                    nxt = 9999
                if 0 <= nxt <= 10000:
                    if d[nxt] == -1:
                        q.append(nxt)
                        d[nxt] = d[x] + 1
                        _from[nxt] = x
                        _how[nxt] = 'S'
            if nxt == l_calc:
                if 0 <= nxt <= 10000:
                    if d[nxt] == -1:
                        q.append(nxt)
                        d[nxt] = d[x] + 1
                        _from[nxt] = x
                        _how[nxt] = 'L'
            if nxt == r_calc:
                if 0 <= nxt <= 10000:
                    if d[nxt] == -1:
                        q.append(nxt)
                        d[nxt] = d[x] + 1
                        _from[nxt] = x
                        _how[nxt] = 'R'

    go(x, y)
    print()





