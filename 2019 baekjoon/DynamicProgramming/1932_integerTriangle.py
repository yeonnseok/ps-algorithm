def solve(n, src):
    d = []
    for i in range(n + 1):
        d.append([0] * i)

    d[1][0] = src[1][0]
    for i in range(2, n + 1):
        for j in range(len(d[i])):
            if j == 0:
                d[i][j] = d[i - 1][j] + src[i][j]
            elif j == len(d[i]) - 1:
                d[i][j] = d[i - 1][j - 1] + src[i][j]
            else:
                d[i][j] = max(d[i-1][j-1], d[i-1][j]) + src[i][j]

    return max(d[-1])


def main():
    n = int(input())
    src = [[]]
    for _ in range(n):
        aa = list(map(int, input().split()))
        src.append(aa)


    print(solve(n, src))


main()
