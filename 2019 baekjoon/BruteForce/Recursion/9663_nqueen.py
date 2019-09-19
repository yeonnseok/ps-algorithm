def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+n-1]:
        return False
    return True


def calc(row):
    if row == n:
        return 1
    ans = 0
    for col in range(n):
        if check(row, col):
            check_col[col] = True
            check_dig[row+col] = True
            check_dig2[row-col+n-1] = True
            a[row][col] = True
            ans += calc(row+1)
            a[row][col] = False
            check_col[col] = False
            check_dig[row+col] = False
            check_dig2[row-col+n-1] = False
    return ans


n = int(input())
a = [[False]*n for _ in range(n)]
check_col = [False] * n
check_dig = [False] * (2*n - 1)
check_dig2 = [False] * (2*n - 1)

print(calc(0))
