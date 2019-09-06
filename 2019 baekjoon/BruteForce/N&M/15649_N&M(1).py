def solve(index, n, m, ans, check):
    if index == m:
        return print(' '.join(map(str, ans)))

    for i in range(1, n + 1):
        if check[i]: continue
        check[i] = True
        ans[index] = i
        solve(index + 1, n, m, ans, check)
        check[i] = False


def main():
    src = list(map(int, input().split()))
    n, m = src[0], src[1]

    ans = [0] * m
    check = [0] * (n + 1)

    solve(0, n, m, ans, check)


main()
