def solve(n, src):
    d = [0] * (n + 1)
    for i in range(1, n + 1):
        d[i] = 1
        for j in range(i + 1):
            if src[i] < src[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1

    return max(d)


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(n, src))


main()
