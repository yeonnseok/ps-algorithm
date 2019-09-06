def solve(n, src):
    d = [0] * (n + 1)

    for i in range(1, n + 1):
        d[i] = src[i]
        for j in range(i):
            if src[i] > src[j] and d[j] + src[i] > d[i]:
                d[i] = d[j] + src[i]

    return max(d)


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(n, src))


main()
