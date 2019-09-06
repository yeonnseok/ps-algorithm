def solve(src):
    d = []
    for _ in range(len(src[0]) + 1):
        d.append([0] * 3)

    ans = 1000*1000 + 1
    for k in range(3):  # house1's color
        for j in range(3):
            if j == k:
                d[1][j] = src[0][j]
            else:
                d[1][j] = 1000*1000+1

        for i in range(2, len(src) + 1):
            d[i][0] = min(d[i-1][1], d[i-1][2]) + src[i-1][0]
            d[i][1] = min(d[i-1][0], d[i-1][2]) + src[i-1][1]
            d[i][2] = min(d[i-1][0], d[i-1][1]) + src[i-1][2]

        for j in range(3):
            if j == k: continue
            ans = min(ans, d[3][j])

    return ans


def main():
    numOfHouse = int(input())
    src = []
    for _ in range(numOfHouse):
        src.append(list(map(int, input().split())))

    print(solve(src))


main()
