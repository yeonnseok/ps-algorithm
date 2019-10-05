from collections import deque

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(mn, mx):
    if mn > a[0][0] or mx < a[0][0]:
        return False
    c = [[False] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    c[0][0] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not c[nx][ny]:
                    if (mn <= a[nx][ny]) and (a[nx][ny] <= mx):
                        c[nx][ny] = True
                        q.append((nx, ny))

    return c[n-1][n-1]


def go(diff):
    mn = 0
    while mn + diff <= 200:
        if bfs(mn, mn + diff):
            return True
        mn += 1
    return False


left = 0
right = 200
ans = 200
while left <= right:
    mid = (left + right) // 2
    if go(mid):
        if ans > mid:
            ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)