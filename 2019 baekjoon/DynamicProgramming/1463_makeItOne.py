# def makeOne(n):
#     d = [0] * (n+1)
#     if n == 1:
#         return 0
#     if d[n]:
#         return d[n]
#
#     d[n] = makeOne(n - 1) + 1
#
#     if n % 3 == 0:
#         temp = makeOne(n//3) + 1
#         if d[n] > temp:
#             d[n] = temp
#
#     if n % 2 == 0:
#         temp = makeOne(n//2) + 1
#         if d[n] > temp:
#             d[n] = temp
#
#     return d[n]
#
#
# def main():
#     num = int(input())
#     print(makeOne(num))
#
#
# main()


def solve(n):
    d = [0] * (n + 1)
    d[1] = 0
    for i in range(2, n + 1):
        d[i] = d[i-1] + 1
        if (i % 2 == 0) and (d[i] > d[i // 2] + 1):
            d[i] = d[i // 2] + 1
        if (i % 3 == 0) and (d[i] > d[i // 3] + 1):
            d[i] = d[i // 3] + 1
    return d[n]


def main():
    num = int(input())
    print(solve(num))


main()