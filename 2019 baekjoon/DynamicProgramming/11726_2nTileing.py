# D(N) = D(N-1) + D(N-2)


# def tileing(n):
#     d = [0] * (n + 1)
#     if n <= 1:
#         return 1
#     if d[n]:
#         return d[n]
#     d[n] = tileing(n-1) + tileing(n-2)
#     return d[n]
#
#
# def main():
#     num = int(input())
#     print(tileing(num))
#
#
# main()


def solve(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1
    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    return d[n]


def main():
    n = int(input())
    print(solve(n))


main()


