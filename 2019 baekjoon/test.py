n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
check = [False] * 26
check[ord(a[0][0]) - ord('A')] = True

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def go(a, x, y, check):
    ans = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            ch = ord(a[nx][ny]) - ord('A')
            if not check[ch]:
                check[ch] = True
                temp = go(a, nx, ny, check)
                if ans < temp:
                    ans = temp
                check[ch] = False
    return ans + 1


print(go(a, 0, 0, check))

