def solve(n, k):
    mod = 1000000000
    d = []
    for _ in range(k + 1):
        d.append([0] * (n + 1))
    d[0][0] = 1

    for i in range(1, k + 1):
        for j in range(n + 1):
            for l in range(0, j + 1):
                d[i][j] += d[i-1][j-l] % mod

    return d[k][n]


def main():
    src = list(map(int, input().split()))
    print(solve(src[0], src[1]))


main()
