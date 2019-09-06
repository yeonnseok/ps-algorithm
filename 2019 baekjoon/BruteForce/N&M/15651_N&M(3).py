def solve(index, n, m, ans):
    if index == m:
        return print(' '.join(map(str, ans)))

    for i in range(1, n + 1):
        ans[index] = i
        solve(index + 1, n, m, ans)


def main():
    src = list(map(int, input().split()))
    n, m = src[0], src[1]

    ans = [0] * m

    solve(0, n, m, ans)


main()
