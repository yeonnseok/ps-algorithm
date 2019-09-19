r, c = map(int, input().split())
a = [list(input()) for _ in range(r)]
check = [False] * 26
check[ord(a[0][0]) - ord('A')] = True
x, y = 0, 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solve(a, check, x, y):
    ans = 0
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            ch = ord(a[nx][ny]) - ord('A')
            if check[ch] is False:
                check[ch] = True
                temp = solve(a, check, nx, ny)
                if ans < temp:
                    ans = temp
                check[ch] = False
    return ans + 1


print(solve(a, check, 0, 0))
