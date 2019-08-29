def solve(src, n):
    d = [0] * (n + 1)
    if n <= 1:
        return src[0]
    if d[n]:
        return d[n]

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if d[i] == 0 or d[i] > d[i - j] + src[j]:
                d[i] = d[i - j] + src[j]

    return d[n]


def main():
    n = int(input())
    src = [0] + list(map(int, input().split()))
    print(solve(src, n))


main()
