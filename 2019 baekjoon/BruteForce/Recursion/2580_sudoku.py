def square(x, y):
    return (x//3)*3 + (y//3)


def calc(z):
    if z == 81:
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z // 9
    y = z % 9
    if a[x][y] != 0:
        return calc(z+1)
    else:
        for i in range(1, 10):
            if check[x][i] is False and check2[y][i] is False and check3[square(x, y)][i] is False:
                check[x][i] = check[y][i] = check3[square(x, y)][i] = True
                a[x][y] = i
                if calc(z+1):
                    return True
                a[x][y] = 0
                check[x][i] = check[y][i] = check3[square(x, y)][i] = False
    return False


a = [list(map(int, input().split())) for _ in range(9)]
check = [[False]*10 for _ in range(9)]
check2 = [[False]*10 for _ in range(9)]
check3 = [[False]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if a[i][j] != 0:
            check[i][a[i][j]] = True
            check2[j][a[i][j]] = True
            check3[square(i, j)][a[i][j]] = True
calc(0)

