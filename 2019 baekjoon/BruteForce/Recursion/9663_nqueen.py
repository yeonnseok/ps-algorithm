n = int(input())
check_col = [False] * n
check_dig1 = [False] * (2*n - 1)
check_dig2 = [False] * (2*n - 1)


def check(row, col):
    if check_col[col]:
        return False
    if check_dig1[row + col]:
        return False
    if check_dig2[row - col + n - 1]:
        return False
    return True


def nqueen(row):
    ans = 0
    if row == n:
        return 1

    for col in range(n):
        if check(row, col):
            check_col[col] = True
            check_dig1[row + col] = True
            check_dig2[row - col + n - 1] = True
            ans += nqueen(row + 1)
            check_col[col] = False
            check_dig1[row + col] = False
            check_dig2[row - col + n - 1] = False

    return ans


print(nqueen(0))
