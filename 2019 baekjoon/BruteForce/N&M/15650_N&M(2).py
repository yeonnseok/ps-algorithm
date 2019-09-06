def solve(index, n, m, selected, ans):
    if selected == m:
        return print(' '.join(map(str, ans)))

    if index > n: return
    ans[selected] = index
    solve(index + 1, n, m, selected + 1, ans)
    ans[selected] = 0
    solve(index + 1, n, m, selected, ans)


def main():
    src = list(map(int, input().split()))
    n, m = src[0], src[1]

    ans = [0] * m

    solve(1, n, m, 0, ans)


main()
