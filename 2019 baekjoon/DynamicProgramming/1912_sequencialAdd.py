import operator
from functools import reduce


def solve(n, src):
    d = []
    for _ in range(n + 1):
        d.append([0] * (n + 1))

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            d[i][j] = d[i][j-1] + src[j-1]

    d = reduce(operator.add, d)
    return max(d)


def main():
    n = int(input())
    src = list(map(int, input().split()))
    print(solve(n, src))


main()
