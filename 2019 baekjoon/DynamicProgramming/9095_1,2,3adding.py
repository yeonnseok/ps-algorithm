# def solve(n):
#     d = [0] * (n + 1)
#     if n <= 1:
#         return 1
#     if n == 2:
#         return 2
#     if d[n]:
#         return d[n]
#
#     d[n] = solve(n-1) + solve(n-2) + solve(n-3)
#     return d[n]


def solve(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1
    d[2] = 2
    for i in range(2, n + 1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]


def main():
    numOfCase = int(input())
    for i in range(numOfCase):
        n = int(input())
        print(solve(n))


main()
