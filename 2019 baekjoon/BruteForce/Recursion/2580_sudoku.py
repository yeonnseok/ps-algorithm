n = 9
a = [list(map(int, input().split())) for _ in range(n)]
check_row = [[False] * (n + 1) for _ in range(n + 1)]
check_col = [[False] * (n + 1) for _ in range(n + 1)]
check_square = [[False] * (n + 1) for _ in range(n + 1)]


def which_square(x, y):
    return (x//3)*3 + (y//3)


def solve(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z // 9
    y = z % 9

    if a[x][y] != 0:
        return solve(z + 1)
    else:
        for i in range(1, n + 1):
            if not check_col[y][i] or not check_row[x][i] or not check_square[which_square(x, y)][i]:
                check_col[y][i] = check_row[x][i] = check_square[which_square(x,y)][i] = True
                a[x][y] = i
                if solve(z + 1):
                    return True
                a[x][y] = 0
                check_col[y][i] = check_row[x][i] = check_square[which_square(x, y)][i] = False
        return False


solve(0)