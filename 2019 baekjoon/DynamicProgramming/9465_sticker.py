def solve(n, src):
    d = []
    for _ in range(n + 1):
        d.append([0] * 3)

    d[1][1] = d[2][1] = 0
    d[1][2] = src[0][1]
    d[2][2] = src[1][1]

    for i in range(1, n + 1):
        d[i][0] = max(d[i - 1][0], d[i - 1][1], d[i - 1][2])
        d[i][1] = max(d[i - 1][0], d[i - 1][2]) + src[0][i - 1]
        d[i][2] = max(d[i - 1][0], d[i - 1][1]) + src[1][i - 1]

    return max(d[-1])


def main():
    numOfCase = int(input())
    for _ in range(numOfCase):
        n = int(input())
        src = []
        for _ in range(2):
            src.append(list(map(int, input().split())))
        print(solve(n, src))


main()
