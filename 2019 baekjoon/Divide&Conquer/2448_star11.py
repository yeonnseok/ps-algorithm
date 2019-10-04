blank = ' '
star = "*"


def go(a, x, y, n, color):
    if color == blank:
        m = 2*n-1
        for i in range(x, x + n):
            for j in range(m):
                a[i][j+i-x+y] = blank
            m -= 2

    elif color == star:
        if n != 1:
            m = n//2
            go(a, x, y, m, star)
            go(a, x+m, y-m, m, star)
            go(a, x+m, y+m, m, star)
            if n == 3:
                go(a, x+1, y, 1, blank)
            else:
                go(a, x+m, y-m+1, m, blank)


n = int(input())
a = [[star]*2*n for _ in range(n)]
go(a, 0, n-1, n, star)
for i in range(n):
    for j in range(n-i-1):
        a[i][j] = blank
        a[i][2*n-j-2] = blank
    a[i][2*n-1] = blank

for row in a:
    print(''.join(row))
