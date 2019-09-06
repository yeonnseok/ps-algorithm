def solve(n, src):
    dl = [0] * (n + 1)
    dr = [0] * (n + 1)

    for i in range(1, n + 1):
        dl[i] = max(dl[i-1] + src[i], src[i])

    for i in reversed(range(n)):
        dr[i] = max(dr[i+1] + src[i], src[i])

    ans = max(dl)
    for i in range(1, n):
        if ans < dl[i - 1] + dr[i + 1]:
            ans = dl[i - 1] + dr[i + 1]
    return ans


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(n, src))


main()
