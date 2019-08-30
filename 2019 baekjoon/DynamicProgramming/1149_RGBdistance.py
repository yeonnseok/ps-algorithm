def solve(src):
    d = []
    for _ in range(len(src[0]) + 1):
        d.append([0] * 3)

    for i in range(1, len(src) + 1):
        for j in range(3):
            if j == 0:
                d[i][j] = min(d[i-1][1], d[i-1][2]) + src[i-1][j]

            if j == 1:
                d[i][j] = min(d[i-1][0], d[i-1][2]) + src[i-1][j]

            if j == 2:
                d[i][j] = min(d[i-1][0], d[i-1][1]) + src[i-1][j]

    return min(d[3])


def main():
    numOfHouse = int(input())
    src = []
    for _ in range(numOfHouse):
        src.append(list(map(int, input().split())))

    print(solve(src))


main()
