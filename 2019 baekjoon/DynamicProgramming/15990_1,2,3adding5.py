def solve(n):
    limit = 100000
    mod = 1000000009
    d = []
    for _ in range(limit + 1):
        d.append([0] * 4)

    for i in range(1, limit + 1):
        if i - 1 >= 0:
            d[i][1] = d[i-1][2] + d[i-1][3]
            if i == 1:
                d[i][1] = 1

        if i - 2 >= 0:
            d[i][2] = d[i-2][1] + d[i-2][3]
            if i == 2:
                d[i][2] = 1

        if i - 3 >= 0:
            d[i][3] = d[i-3][1] + d[i-3][2]
            if i == 3:
                d[i][3] = 1

        d[i][1] %= mod
        d[i][2] %= mod
        d[i][3] %= mod

    return (d[n][1] + d[n][2] + d[n][3]) % mod


def main():
    numOfCase = int(input())
    for i in range(numOfCase):
        n = int(input())
        print(solve(n))


main()
