def solve(n):
    mod = 9901
    d = []
    for _ in range(n + 1):
        d.append([0] * 3)

    d[1][0] = d[1][1] = d[1][2] =  1
    for i in range(2, n + 1):
        for j in range(3):
            if j == 0:
                d[i][j] = (d[i-1][0] + d[i-1][1] + d[i-1][2]) % mod
            if j == 1:
                d[i][j] = (d[i-1][0] + d[i-1][2]) % mod
            if j == 2:
                d[i][j] = (d[i-1][0] + d[i-1][1]) % mod
    return sum(d[-1])


def main():
    n = int(input())
    print(solve(n))


main()
